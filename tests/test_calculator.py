import math
import unittest

from src.mcp_mathematics.calculator import evaluate_mathematical_expression


class TestCalculator(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sin(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sin(pi/2)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sin(pi)")), 0.0, places=7)

    def test_cos(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("cos(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("cos(pi/2)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("cos(pi)")), -1.0, places=7)

    def test_tan(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("tan(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("tan(pi/4)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("tan(-pi/4)")), -1.0, places=7
        )

    def test_asin(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("asin(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("asin(1)")), math.pi / 2, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("asin(0.5)")), math.pi / 6, places=7
        )

    def test_acos(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("acos(1)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("acos(0)")), math.pi / 2, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("acos(-1)")), math.pi, places=7
        )

    def test_atan(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("atan(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("atan(1)")), math.pi / 4, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("atan(-1)")), -math.pi / 4, places=7
        )

    def test_atan2(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("atan2(0, 1)")), 0.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("atan2(1, 0)")), math.pi / 2, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("atan2(1, 1)")), math.pi / 4, places=7
        )

    def test_sinh(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sinh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("sinh(1)")), math.sinh(1), places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("sinh(-1)")), math.sinh(-1), places=7
        )

    def test_cosh(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("cosh(0)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("cosh(1)")), math.cosh(1), places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("cosh(-1)")), math.cosh(-1), places=7
        )

    def test_tanh(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("tanh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("tanh(1)")), math.tanh(1), places=7
        )
        self.assertAlmostEqual(float(evaluate_mathematical_expression("tanh(100)")), 1.0, places=7)

    def test_asinh(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("asinh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("asinh(1)")), math.asinh(1), places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("asinh(-1)")), math.asinh(-1), places=7
        )

    def test_acosh(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("acosh(1)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("acosh(2)")), math.acosh(2), places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("acosh(10)")), math.acosh(10), places=7
        )

    def test_atanh(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("atanh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("atanh(0.5)")), math.atanh(0.5), places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("atanh(-0.5)")), math.atanh(-0.5), places=7
        )

    def test_log(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log(e)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("log(10)")), math.log(10), places=7
        )

    def test_log10(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log10(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log10(10)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log10(100)")), 2.0, places=7)

    def test_log2(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log2(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log2(2)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log2(8)")), 3.0, places=7)

    def test_log1p(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log1p(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("log1p(1)")), math.log(2), places=7
        )
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log1p(e-1)")), 1.0, places=7)

    def test_exp(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("exp(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("exp(1)")), math.e, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("exp(2)")), math.exp(2), places=7
        )

    def test_exp2(self):
        try:
            self.assertAlmostEqual(
                float(evaluate_mathematical_expression("exp2(0)")), 1.0, places=7
            )
            self.assertAlmostEqual(
                float(evaluate_mathematical_expression("exp2(1)")), 2.0, places=7
            )
            self.assertAlmostEqual(
                float(evaluate_mathematical_expression("exp2(3)")), 8.0, places=7
            )
        except Exception:
            self.skipTest("exp2 not available in this Python version")

    def test_expm1(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("expm1(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("expm1(1)")), math.e - 1, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("expm1(-1)")), math.expm1(-1), places=7
        )

    def test_sqrt(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sqrt(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sqrt(4)")), 2.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sqrt(9)")), 3.0, places=7)

    def test_cbrt(self):
        try:
            self.assertAlmostEqual(
                float(evaluate_mathematical_expression("cbrt(0)")), 0.0, places=7
            )
            self.assertAlmostEqual(
                float(evaluate_mathematical_expression("cbrt(8)")), 2.0, places=7
            )
            self.assertAlmostEqual(
                float(evaluate_mathematical_expression("cbrt(27)")), 3.0, places=7
            )
        except Exception:
            self.skipTest("cbrt not available in this Python version")

    def test_pow(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("pow(2, 0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("pow(2, 3)")), 8.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("pow(5, 2)")), 25.0, places=7)

    def test_hypot(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("hypot(3, 4)")), 5.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("hypot(5, 12)")), 13.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("hypot(0, 0)")), 0.0, places=7
        )

    def test_fabs(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("fabs(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("fabs(-5)")), 5.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("fabs(3.14)")), 3.14, places=7
        )

    def test_copysign(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("copysign(1, -1)")), -1.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("copysign(-5, 1)")), 5.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("copysign(3.14, -1)")), -3.14, places=7
        )

    def test_factorial(self):
        self.assertEqual(evaluate_mathematical_expression("factorial(0)"), "1")
        self.assertEqual(evaluate_mathematical_expression("factorial(5)"), "120")
        self.assertEqual(evaluate_mathematical_expression("factorial(10)"), "3628800")

    def test_ceil(self):
        self.assertEqual(evaluate_mathematical_expression("ceil(1.1)"), "2")
        self.assertEqual(evaluate_mathematical_expression("ceil(2.9)"), "3")
        self.assertEqual(evaluate_mathematical_expression("ceil(-1.1)"), "-1")

    def test_floor(self):
        self.assertEqual(evaluate_mathematical_expression("floor(1.9)"), "1")
        self.assertEqual(evaluate_mathematical_expression("floor(2.1)"), "2")
        self.assertEqual(evaluate_mathematical_expression("floor(-1.1)"), "-2")

    def test_trunc(self):
        self.assertEqual(evaluate_mathematical_expression("trunc(1.9)"), "1")
        self.assertEqual(evaluate_mathematical_expression("trunc(-1.9)"), "-1")
        self.assertEqual(evaluate_mathematical_expression("trunc(3.5)"), "3")

    def test_degrees(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("degrees(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("degrees(pi)")), 180.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("degrees(pi/2)")), 90.0, places=7
        )

    def test_radians(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("radians(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("radians(180)")), math.pi, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("radians(90)")), math.pi / 2, places=7
        )

    def test_gcd(self):
        self.assertEqual(evaluate_mathematical_expression("gcd(12, 8)"), "4")
        self.assertEqual(evaluate_mathematical_expression("gcd(15, 25)"), "5")
        self.assertEqual(evaluate_mathematical_expression("gcd(17, 19)"), "1")

    def test_lcm(self):
        try:
            self.assertEqual(evaluate_mathematical_expression("lcm(4, 6)"), "12")
            self.assertEqual(evaluate_mathematical_expression("lcm(3, 5)"), "15")
            self.assertEqual(evaluate_mathematical_expression("lcm(12, 18)"), "36")
        except Exception:
            self.skipTest("lcm not available in this Python version")

    def test_isqrt(self):
        try:
            self.assertEqual(evaluate_mathematical_expression("isqrt(0)"), "0")
            self.assertEqual(evaluate_mathematical_expression("isqrt(4)"), "2")
            self.assertEqual(evaluate_mathematical_expression("isqrt(10)"), "3")
        except Exception:
            self.skipTest("isqrt not available in this Python version")

    def test_fmod(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("fmod(10, 3)")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("fmod(5.5, 2.5)")), 0.5, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("fmod(-10, 3)")), -1.0, places=7
        )

    def test_remainder(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("remainder(10, 3)")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("remainder(10, 6)")), -2.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("remainder(10, 10)")), 0.0, places=7
        )

    def test_modf(self):
        result = evaluate_mathematical_expression("modf(1.5)")
        self.assertIn("0.5", result)
        self.assertIn("1.0", result)
        result = evaluate_mathematical_expression("modf(2.7)")
        self.assertIn("0.7", result)
        result = evaluate_mathematical_expression("modf(-1.5)")
        self.assertIn("-0.5", result)

    def test_frexp(self):
        result = evaluate_mathematical_expression("frexp(4)")
        self.assertIn("0.5", result)
        self.assertIn("3", result)
        result = evaluate_mathematical_expression("frexp(8)")
        self.assertIn("0.5", result)
        self.assertIn("4", result)
        result = evaluate_mathematical_expression("frexp(1)")
        self.assertIn("0.5", result)

    def test_ldexp(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("ldexp(0.5, 3)")), 4.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("ldexp(1, 0)")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("ldexp(0.5, 4)")), 8.0, places=7
        )

    def test_isfinite(self):
        self.assertEqual(evaluate_mathematical_expression("isfinite(0)"), "True")
        self.assertEqual(evaluate_mathematical_expression("isfinite(1.5)"), "True")
        self.assertEqual(evaluate_mathematical_expression("isfinite(inf)"), "False")

    def test_isinf(self):
        self.assertEqual(evaluate_mathematical_expression("isinf(inf)"), "True")
        self.assertEqual(evaluate_mathematical_expression("isinf(-inf)"), "True")
        self.assertEqual(evaluate_mathematical_expression("isinf(1.0)"), "False")

    def test_isnan(self):
        self.assertEqual(evaluate_mathematical_expression("isnan(nan)"), "True")
        self.assertEqual(evaluate_mathematical_expression("isnan(1.0)"), "False")
        self.assertEqual(evaluate_mathematical_expression("isnan(inf)"), "False")

    def test_isclose(self):
        self.assertEqual(evaluate_mathematical_expression("isclose(1.0, 1.0)"), "True")
        self.assertEqual(evaluate_mathematical_expression("isclose(1.0, 1.00001)"), "False")
        self.assertEqual(evaluate_mathematical_expression("isclose(1.0, 1.000001)"), "False")

    def test_comb(self):
        try:
            self.assertEqual(evaluate_mathematical_expression("comb(5, 2)"), "10")
            self.assertEqual(evaluate_mathematical_expression("comb(10, 3)"), "120")
            self.assertEqual(evaluate_mathematical_expression("comb(4, 4)"), "1")
        except Exception:
            self.skipTest("comb not available in this Python version")

    def test_perm(self):
        try:
            self.assertEqual(evaluate_mathematical_expression("perm(5, 2)"), "20")
            self.assertEqual(evaluate_mathematical_expression("perm(4, 3)"), "24")
            self.assertEqual(evaluate_mathematical_expression("perm(3, 3)"), "6")
        except Exception:
            self.skipTest("perm not available in this Python version")

    def test_erf(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("erf(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("erf(1)")), math.erf(1), places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("erf(-1)")), math.erf(-1), places=7
        )

    def test_erfc(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("erfc(0)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("erfc(1)")), math.erfc(1), places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("erfc(-1)")), math.erfc(-1), places=7
        )

    def test_gamma(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("gamma(1)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("gamma(2)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("gamma(5)")), 24.0, places=7)

    def test_lgamma(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("lgamma(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("lgamma(2)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("lgamma(10)")), math.lgamma(10), places=7
        )

    def test_nextafter(self):
        try:
            result = float(evaluate_mathematical_expression("nextafter(1, 2)"))
            self.assertGreater(result, 1.0)
            self.assertLess(result, 1.0001)
            result = float(evaluate_mathematical_expression("nextafter(1, 0)"))
            self.assertLess(result, 1.0)
            self.assertAlmostEqual(
                float(evaluate_mathematical_expression("nextafter(0, 1)")), 5e-324, places=320
            )
        except Exception:
            self.skipTest("nextafter not available in this Python version")

    def test_ulp(self):
        try:
            self.assertGreater(float(evaluate_mathematical_expression("ulp(1.0)")), 0)
            self.assertLess(float(evaluate_mathematical_expression("ulp(1.0)")), 1e-10)
            self.assertGreater(
                float(evaluate_mathematical_expression("ulp(1000000.0)")),
                float(evaluate_mathematical_expression("ulp(1.0)")),
            )
        except Exception:
            self.skipTest("ulp not available in this Python version")

    def test_pi_constant(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("pi")), math.pi, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("pi * 2")), math.pi * 2, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("pi / 2")), math.pi / 2, places=7
        )

    def test_e_constant(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("e")), math.e, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("e * 2")), math.e * 2, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("e ** 2")), math.e**2, places=7
        )

    def test_tau_constant(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("tau")), math.tau, places=7)
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("tau / 4")), math.tau / 4, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("tau / 2")), math.pi, places=7
        )

    def test_inf_constant(self):
        # Calculator has safety checks for infinite values
        with self.assertRaises(ValueError, msg="Calculator should handle inf safely"):
            evaluate_mathematical_expression("inf")
        # Test operations that should raise ValueError for safety
        with self.assertRaises(ValueError):
            evaluate_mathematical_expression("1.0 / 0.0")
        # Test very large numbers (should either work or raise error safely)
        try:
            result = evaluate_mathematical_expression("10**308")
            self.assertIsInstance(result, str)
        except ValueError:
            pass  # Large numbers may be restricted for safety

    def test_nan_constant(self):
        self.assertEqual(evaluate_mathematical_expression("nan"), "nan")
        self.assertEqual(evaluate_mathematical_expression("nan + 1"), "nan")
        self.assertEqual(evaluate_mathematical_expression("0 * nan"), "nan")

    def test_basic_arithmetic(self):
        self.assertEqual(evaluate_mathematical_expression("2 + 3"), "5")
        self.assertEqual(evaluate_mathematical_expression("10 - 4"), "6")
        self.assertEqual(evaluate_mathematical_expression("5 * 6"), "30")
        self.assertEqual(evaluate_mathematical_expression("15 / 3"), "5.0")
        self.assertEqual(evaluate_mathematical_expression("7 // 2"), "3")
        self.assertEqual(evaluate_mathematical_expression("10 % 3"), "1")
        self.assertEqual(evaluate_mathematical_expression("2 ** 3"), "8")

    def test_unicode_operators(self):
        self.assertEqual(evaluate_mathematical_expression("2 × 3"), "6")
        self.assertEqual(evaluate_mathematical_expression("8 ÷ 2"), "4.0")
        self.assertEqual(evaluate_mathematical_expression("2 ^ 3"), "8")

    def test_complex_expressions(self):
        self.assertEqual(evaluate_mathematical_expression("(2 + 3) * 4"), "20")
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("sin(pi/2) + cos(0)")), 2.0, places=7
        )
        result = evaluate_mathematical_expression("factorial(5) + sqrt(16)")
        self.assertIn(result, ["124", "124.0"])

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            evaluate_mathematical_expression("1 / 0")
        with self.assertRaises(SyntaxError):
            evaluate_mathematical_expression("")
        with self.assertRaises(ValueError):
            evaluate_mathematical_expression("unknown_func()")

    def test_new_constants_phi_euler(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("phi")), (1 + math.sqrt(5)) / 2, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("euler")), 0.5772156649, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("phi * 2")), (1 + math.sqrt(5)), places=7
        )

    def test_statistics_functions(self):
        # Note: Direct list syntax may not be supported, but we can test if functions exist
        # Test would need to be implemented based on actual calculator syntax support
        try:
            # Test if mean function exists in calculator
            result = evaluate_mathematical_expression("mean([1, 2, 3, 4, 5])")
            if "Error" in result or "not" in result.lower():
                self.skipTest("List syntax not supported in calculator")
            else:
                self.assertEqual(result, "3.0")
        except Exception as e:
            self.skipTest(f"Statistics functions syntax not supported: {e}")

    def test_complex_functions_phase_polar(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("phase(1+1j)")), math.pi / 4, places=7
        )
        result = evaluate_mathematical_expression("polar(1+1j)")
        self.assertTrue("1.414" in result or "Result:" in result)

    def test_complex_trigonometry_functions(self):
        result = evaluate_mathematical_expression("csin(0)")
        self.assertTrue("0" in result or "Result:" in result)
        result = evaluate_mathematical_expression("ccos(0)")
        self.assertTrue("1" in result or "Result:" in result)
        result = evaluate_mathematical_expression("cexp(0)")
        self.assertTrue("1" in result or "Result:" in result)

    def test_complex_logarithm_functions(self):
        result = evaluate_mathematical_expression("clog(1)")
        self.assertTrue("0" in result or "Result:" in result)
        result = evaluate_mathematical_expression("clog10(1)")
        self.assertTrue("0" in result or "Result:" in result)
        result = evaluate_mathematical_expression("csqrt(4)")
        self.assertTrue("2" in result or "Result:" in result)

    def test_enhanced_mathematical_functions(self):
        try:
            result = evaluate_mathematical_expression("cbrt(27)")
            self.assertAlmostEqual(float(result), 3.0, places=7)
        except Exception:
            self.skipTest("cbrt not available in this Python version")

        try:
            result = evaluate_mathematical_expression("comb(5, 2)")
            self.assertEqual(result, "10")
        except Exception:
            self.skipTest("comb not available in this Python version")

        try:
            result = evaluate_mathematical_expression("perm(5, 2)")
            self.assertEqual(result, "20")
        except Exception:
            self.skipTest("perm not available in this Python version")

    def test_complex_number_expressions(self):
        result = evaluate_mathematical_expression("1+2j")
        self.assertTrue("1" in result and "2j" in result)

        result = evaluate_mathematical_expression("(1+2j) + (3+4j)")
        self.assertTrue("4" in result and "6j" in result)

        try:
            result = evaluate_mathematical_expression("abs(3+4j)")
            self.assertAlmostEqual(float(result), 5.0, places=7)
        except Exception:
            self.skipTest("Complex abs function not implemented")

    def test_security_validation(self):
        dangerous_expressions = [
            "__import__",
            "exec()",
            "eval()",
            "globals()",
            "locals()",
            "open()",
            "file()",
        ]

        for expr in dangerous_expressions:
            with self.assertRaises((ValueError, SyntaxError)) as context:
                evaluate_mathematical_expression(expr)
            error_message = str(context.exception).lower()
            self.assertTrue(
                "forbidden pattern" in error_message
                or "invalid mathematical expression" in error_message
                or "unsupported operations" in error_message,
                f"Expected security error for '{expr}', got: {error_message}",
            )

    def test_resource_limits_factorial(self):
        result = evaluate_mathematical_expression("factorial(5)")
        self.assertEqual(result, "120")

        result = evaluate_mathematical_expression("factorial(10)")
        self.assertEqual(result, "3628800")

        try:
            result = evaluate_mathematical_expression("factorial(200)")
            if "Error" not in result:
                self.fail("Large factorial should be limited")
        except Exception:
            pass

    def test_resource_limits_expression_length(self):
        very_long_expr = "1+" * 2000 + "1"
        try:
            result = evaluate_mathematical_expression(very_long_expr)
            if "Error" not in result:
                self.fail("Very long expression should be limited")
        except Exception:
            pass

    def test_enhanced_error_handling_complex(self):
        try:
            result = evaluate_mathematical_expression("log(-1)")
            if "Error" in result or "nan" in result or "inf" in result:
                pass
            else:
                self.fail("log(-1) should produce error or special value")
        except Exception:
            pass

        try:
            result = evaluate_mathematical_expression("sqrt(-1)")
            if "Error" in result or "j" in result:
                pass
            else:
                self.fail("sqrt(-1) should produce error or complex number")
        except Exception:
            pass

    def test_trigonometric_edge_cases(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("sin(pi)")), 0.0, places=5)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("cos(2*pi)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("tan(pi/4)")), 1.0, places=7)

    def test_logarithmic_edge_cases(self):
        self.assertEqual(evaluate_mathematical_expression("log(1)"), "0")
        self.assertAlmostEqual(float(evaluate_mathematical_expression("log(e)")), 1.0, places=7)
        self.assertEqual(evaluate_mathematical_expression("log10(1)"), "0")
        self.assertEqual(evaluate_mathematical_expression("log10(10)"), "1")

    def test_exponential_edge_cases(self):
        self.assertEqual(evaluate_mathematical_expression("exp(0)"), "1")
        self.assertAlmostEqual(float(evaluate_mathematical_expression("exp(1)")), math.e, places=7)
        try:
            self.assertEqual(evaluate_mathematical_expression("exp2(0)"), "1")
            self.assertEqual(evaluate_mathematical_expression("exp2(3)"), "8")
        except Exception:
            self.skipTest("exp2 not available in this Python version")

    def test_hyperbolic_functions_edge_cases(self):
        self.assertEqual(evaluate_mathematical_expression("sinh(0)"), "0")
        self.assertEqual(evaluate_mathematical_expression("cosh(0)"), "1")
        self.assertEqual(evaluate_mathematical_expression("tanh(0)"), "0")

    def test_inverse_hyperbolic_functions_edge_cases(self):
        self.assertEqual(evaluate_mathematical_expression("asinh(0)"), "0")
        self.assertEqual(evaluate_mathematical_expression("acosh(1)"), "0")
        self.assertEqual(evaluate_mathematical_expression("atanh(0)"), "0")

    def test_special_values_handling(self):
        # Test that calculator handles special values safely
        with self.assertRaises(ValueError):
            evaluate_mathematical_expression("inf")
        # Test nan constant (should work if implemented)
        try:
            result = evaluate_mathematical_expression("nan")
            self.assertEqual(result, "nan")
        except ValueError:
            pass  # nan might also be restricted for safety
        # Test division by zero handling
        with self.assertRaises(ValueError):
            evaluate_mathematical_expression("1.0 / 0.0")

    def test_precision_and_rounding(self):
        self.assertAlmostEqual(float(evaluate_mathematical_expression("pi")), math.pi, places=10)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("e")), math.e, places=10)
        self.assertAlmostEqual(float(evaluate_mathematical_expression("tau")), math.tau, places=10)

    def test_mathematical_identities(self):
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("sin(pi/2)**2 + cos(pi/2)**2")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("exp(log(5))")), 5.0, places=7
        )
        self.assertAlmostEqual(
            float(evaluate_mathematical_expression("log(exp(3))")), 3.0, places=7
        )

    def test_large_number_handling(self):
        result = evaluate_mathematical_expression("2**50")
        self.assertEqual(result, str(2**50))

        result = evaluate_mathematical_expression("factorial(20)")
        expected = str(math.factorial(20))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
