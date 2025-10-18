#!/usr/bin/env python3

import argparse
import re
import subprocess
import sys
import tomllib
from pathlib import Path


class SemverPublisher:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).absolute()
        self.pyproject_path = self.project_root / "pyproject.toml"

    def get_current_version(self) -> str:
        if not self.pyproject_path.exists():
            raise FileNotFoundError("pyproject.toml not found")

        with open(self.pyproject_path, "rb") as f:
            data = tomllib.load(f)

        return data["project"]["version"]

    def parse_semver(self, version: str) -> tuple[int, int, int]:
        pattern = r"^(\d+)\.(\d+)\.(\d+)(?:-.*)?(?:\+.*)?$"
        match = re.match(pattern, version)
        if not match:
            raise ValueError(f"Invalid semver format: {version}")
        return int(match.group(1)), int(match.group(2)), int(match.group(3))

    def increment_version(self, version: str, bump_type: str) -> str:
        major, minor, patch = self.parse_semver(version)

        if bump_type == "major":
            return f"{major + 1}.0.0"
        elif bump_type == "minor":
            return f"{major}.{minor + 1}.0"
        elif bump_type == "patch":
            return f"{major}.{minor}.{patch + 1}"
        else:
            raise ValueError(f"Invalid bump type: {bump_type}")

    def update_pyproject_version(self, new_version: str) -> None:
        with open(self.pyproject_path) as f:
            content = f.read()

        pattern = r'(\[project\][\s\S]*?)version\s*=\s*"[^"]+"'

        def replacement_func(match):
            project_section = match.group(1)
            return f'{project_section}version = "{new_version}"'

        new_content = re.sub(pattern, replacement_func, content)

        if new_content == content:
            raise ValueError("Version pattern not found in pyproject.toml")

        if 'target-version = "' + new_version + '"' in new_content:
            raise ValueError(
                f"Version update would corrupt tool configuration. Ruff target-version should not be changed to package version {new_version}"
            )

        with open(self.pyproject_path, "w") as f:
            f.write(new_content)

    def update_uv_lock(self) -> None:
        self.run_command(["uv", "lock"])

    def run_command(self, cmd: list, cwd: Path | None = None) -> subprocess.CompletedProcess:
        try:
            result = subprocess.run(
                cmd, cwd=cwd or self.project_root, capture_output=True, text=True, check=True
            )
            return result
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {' '.join(cmd)}")
            print(f"Error: {e.stderr}")
            raise

    def clean_build(self) -> None:
        build_dirs = [self.project_root / "build", self.project_root / "dist"]
        for build_dir in build_dirs:
            if build_dir.exists():
                self.run_command(["rm", "-rf", str(build_dir)])

    def build_package(self) -> None:
        self.run_command([sys.executable, "-m", "build"])

    def validate_package(self) -> None:
        self.run_command(["twine", "check", "dist/*"])

    def run_tests(self) -> None:
        self.run_command([sys.executable, "-m", "unittest", "discover", "-s", "tests"])

    def publish_to_pypi(self, repository: str = "pypi") -> None:
        cmd = ["twine", "upload"]
        if repository != "pypi":
            cmd.extend(["--repository", repository])
        cmd.append("dist/*")

        self.run_command(cmd)

    def git_commit_and_tag(self, version: str, message: str | None = None) -> None:
        if not message:
            message = f"Release v{version}"

        self.run_command(["git", "add", "pyproject.toml", "uv.lock"])
        self.run_command(["git", "commit", "-m", message])
        self.run_command(["git", "tag", f"v{version}"])

    def check_git_status(self) -> bool:
        try:
            result = self.run_command(["git", "status", "--porcelain"])
            return len(result.stdout.strip()) == 0
        except subprocess.CalledProcessError:
            return False

    def publish(
        self,
        bump_type: str,
        dry_run: bool = False,
        skip_tests: bool = False,
        repository: str = "pypi",
        commit_message: str | None = None,
    ) -> str:

        print("🚀 Starting semver-based package publishing...")

        if not self.check_git_status() and not dry_run:
            print("⚠️  Warning: Git working directory is not clean")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != "y":
                print("Aborted.")
                return ""

        current_version = self.get_current_version()
        new_version = self.increment_version(current_version, bump_type)

        print(f"📦 Current version: {current_version}")
        print(f"📦 New version: {new_version}")

        if dry_run:
            print("🔍 DRY RUN - No changes will be made")
            return new_version

        try:
            if not skip_tests:
                print("🧪 Running tests...")
                self.run_tests()
                print("✅ Tests passed")

            print(f"📝 Updating version to {new_version}...")
            self.update_pyproject_version(new_version)

            print("🔒 Updating uv.lock file...")
            self.update_uv_lock()

            print("🧹 Cleaning build directories...")
            self.clean_build()

            print("🔨 Building package...")
            self.build_package()

            print("🔍 Validating package...")
            self.validate_package()

            print(f"📤 Publishing to {repository}...")
            self.publish_to_pypi(repository)

            print("📝 Committing and tagging...")
            self.git_commit_and_tag(new_version, commit_message)

            print(f"🎉 Successfully published {new_version}!")
            print(f"🏷️  Git tag: v{new_version}")

            if repository == "pypi":
                print(f"🌐 PyPI: https://pypi.org/project/mcp-mathematics/{new_version}/")

            return new_version

        except Exception as e:
            print(f"❌ Publishing failed: {e}")
            print("💡 You may need to manually revert version changes")
            raise


def main():
    parser = argparse.ArgumentParser(description="Semver-based package publishing")
    parser.add_argument("bump_type", choices=["major", "minor", "patch"], help="Version bump type")
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be done without making changes"
    )
    parser.add_argument("--skip-tests", action="store_true", help="Skip running tests")
    parser.add_argument("--repository", default="pypi", help="PyPI repository (default: pypi)")
    parser.add_argument("--message", help="Custom commit message")
    parser.add_argument("--project-root", default=".", help="Project root directory")

    args = parser.parse_args()

    try:
        publisher = SemverPublisher(args.project_root)
        new_version = publisher.publish(
            bump_type=args.bump_type,
            dry_run=args.dry_run,
            skip_tests=args.skip_tests,
            repository=args.repository,
            commit_message=args.message,
        )

        if not args.dry_run:
            print("\n✨ Next steps:")
            print("   git push origin main")
            print(f"   git push origin v{new_version}")

    except KeyboardInterrupt:
        print("\n❌ Aborted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
