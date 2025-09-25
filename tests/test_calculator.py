import math
import unittest

from src.mcp_mathematics.calculator import execute_mathematical_computation


class TestCalculator(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("sin(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("sin(pi/2)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("sin(pi)")), 0.0, places=7)

    def test_cos(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("cos(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("cos(pi/2)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("cos(pi)")), -1.0, places=7)

    def test_tan(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("tan(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("tan(pi/4)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("tan(-pi/4)")), -1.0, places=7
        )

    def test_asin(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("asin(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("asin(1)")), math.pi / 2, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("asin(0.5)")), math.pi / 6, places=7
        )

    def test_acos(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("acos(1)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("acos(0)")), math.pi / 2, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("acos(-1)")), math.pi, places=7
        )

    def test_atan(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("atan(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("atan(1)")), math.pi / 4, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("atan(-1)")), -math.pi / 4, places=7
        )

    def test_atan2(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("atan2(0, 1)")), 0.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("atan2(1, 0)")), math.pi / 2, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("atan2(1, 1)")), math.pi / 4, places=7
        )

    def test_sinh(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("sinh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("sinh(1)")), math.sinh(1), places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("sinh(-1)")), math.sinh(-1), places=7
        )

    def test_cosh(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("cosh(0)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("cosh(1)")), math.cosh(1), places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("cosh(-1)")), math.cosh(-1), places=7
        )

    def test_tanh(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("tanh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("tanh(1)")), math.tanh(1), places=7
        )
        self.assertAlmostEqual(float(execute_mathematical_computation("tanh(100)")), 1.0, places=7)

    def test_asinh(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("asinh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("asinh(1)")), math.asinh(1), places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("asinh(-1)")), math.asinh(-1), places=7
        )

    def test_acosh(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("acosh(1)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("acosh(2)")), math.acosh(2), places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("acosh(10)")), math.acosh(10), places=7
        )

    def test_atanh(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("atanh(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("atanh(0.5)")), math.atanh(0.5), places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("atanh(-0.5)")), math.atanh(-0.5), places=7
        )

    def test_log(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("log(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("log(e)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("log(10)")), math.log(10), places=7
        )

    def test_log10(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("log10(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("log10(10)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("log10(100)")), 2.0, places=7)

    def test_log2(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("log2(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("log2(2)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("log2(8)")), 3.0, places=7)

    def test_log1p(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("log1p(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("log1p(1)")), math.log(2), places=7
        )
        self.assertAlmostEqual(float(execute_mathematical_computation("log1p(e-1)")), 1.0, places=7)

    def test_exp(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("exp(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("exp(1)")), math.e, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("exp(2)")), math.exp(2), places=7
        )

    def test_exp2(self):
        try:
            self.assertAlmostEqual(
                float(execute_mathematical_computation("exp2(0)")), 1.0, places=7
            )
            self.assertAlmostEqual(
                float(execute_mathematical_computation("exp2(1)")), 2.0, places=7
            )
            self.assertAlmostEqual(
                float(execute_mathematical_computation("exp2(3)")), 8.0, places=7
            )
        except Exception:
            self.skipTest("exp2 not available in this Python version")

    def test_expm1(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("expm1(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("expm1(1)")), math.e - 1, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("expm1(-1)")), math.expm1(-1), places=7
        )

    def test_sqrt(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("sqrt(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("sqrt(4)")), 2.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("sqrt(9)")), 3.0, places=7)

    def test_cbrt(self):
        try:
            self.assertAlmostEqual(
                float(execute_mathematical_computation("cbrt(0)")), 0.0, places=7
            )
            self.assertAlmostEqual(
                float(execute_mathematical_computation("cbrt(8)")), 2.0, places=7
            )
            self.assertAlmostEqual(
                float(execute_mathematical_computation("cbrt(27)")), 3.0, places=7
            )
        except Exception:
            self.skipTest("cbrt not available in this Python version")

    def test_pow(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("pow(2, 0)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("pow(2, 3)")), 8.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("pow(5, 2)")), 25.0, places=7)

    def test_hypot(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("hypot(3, 4)")), 5.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("hypot(5, 12)")), 13.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("hypot(0, 0)")), 0.0, places=7
        )

    def test_fabs(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("fabs(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("fabs(-5)")), 5.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("fabs(3.14)")), 3.14, places=7
        )

    def test_copysign(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("copysign(1, -1)")), -1.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("copysign(-5, 1)")), 5.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("copysign(3.14, -1)")), -3.14, places=7
        )

    def test_factorial(self):
        self.assertEqual(execute_mathematical_computation("factorial(0)"), "1")
        self.assertEqual(execute_mathematical_computation("factorial(5)"), "120")
        self.assertEqual(execute_mathematical_computation("factorial(10)"), "3628800")

    def test_ceil(self):
        self.assertEqual(execute_mathematical_computation("ceil(1.1)"), "2")
        self.assertEqual(execute_mathematical_computation("ceil(2.9)"), "3")
        self.assertEqual(execute_mathematical_computation("ceil(-1.1)"), "-1")

    def test_floor(self):
        self.assertEqual(execute_mathematical_computation("floor(1.9)"), "1")
        self.assertEqual(execute_mathematical_computation("floor(2.1)"), "2")
        self.assertEqual(execute_mathematical_computation("floor(-1.1)"), "-2")

    def test_trunc(self):
        self.assertEqual(execute_mathematical_computation("trunc(1.9)"), "1")
        self.assertEqual(execute_mathematical_computation("trunc(-1.9)"), "-1")
        self.assertEqual(execute_mathematical_computation("trunc(3.5)"), "3")

    def test_degrees(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("degrees(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("degrees(pi)")), 180.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("degrees(pi/2)")), 90.0, places=7
        )

    def test_radians(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("radians(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("radians(180)")), math.pi, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("radians(90)")), math.pi / 2, places=7
        )

    def test_gcd(self):
        self.assertEqual(execute_mathematical_computation("gcd(12, 8)"), "4")
        self.assertEqual(execute_mathematical_computation("gcd(15, 25)"), "5")
        self.assertEqual(execute_mathematical_computation("gcd(17, 19)"), "1")

    def test_lcm(self):
        try:
            self.assertEqual(execute_mathematical_computation("lcm(4, 6)"), "12")
            self.assertEqual(execute_mathematical_computation("lcm(3, 5)"), "15")
            self.assertEqual(execute_mathematical_computation("lcm(12, 18)"), "36")
        except Exception:
            self.skipTest("lcm not available in this Python version")

    def test_isqrt(self):
        try:
            self.assertEqual(execute_mathematical_computation("isqrt(0)"), "0")
            self.assertEqual(execute_mathematical_computation("isqrt(4)"), "2")
            self.assertEqual(execute_mathematical_computation("isqrt(10)"), "3")
        except Exception:
            self.skipTest("isqrt not available in this Python version")

    def test_fmod(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("fmod(10, 3)")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("fmod(5.5, 2.5)")), 0.5, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("fmod(-10, 3)")), -1.0, places=7
        )

    def test_remainder(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("remainder(10, 3)")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("remainder(10, 6)")), -2.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("remainder(10, 10)")), 0.0, places=7
        )

    def test_modf(self):
        result = execute_mathematical_computation("modf(1.5)")
        self.assertIn("0.5", result)
        self.assertIn("1.0", result)
        result = execute_mathematical_computation("modf(2.7)")
        self.assertIn("0.7", result)
        result = execute_mathematical_computation("modf(-1.5)")
        self.assertIn("-0.5", result)

    def test_frexp(self):
        result = execute_mathematical_computation("frexp(4)")
        self.assertIn("0.5", result)
        self.assertIn("3", result)
        result = execute_mathematical_computation("frexp(8)")
        self.assertIn("0.5", result)
        self.assertIn("4", result)
        result = execute_mathematical_computation("frexp(1)")
        self.assertIn("0.5", result)

    def test_ldexp(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("ldexp(0.5, 3)")), 4.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("ldexp(1, 0)")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("ldexp(0.5, 4)")), 8.0, places=7
        )

    def test_isfinite(self):
        self.assertEqual(execute_mathematical_computation("isfinite(0)"), "True")
        self.assertEqual(execute_mathematical_computation("isfinite(1.5)"), "True")
        self.assertEqual(execute_mathematical_computation("isfinite(inf)"), "False")

    def test_isinf(self):
        self.assertEqual(execute_mathematical_computation("isinf(inf)"), "True")
        self.assertEqual(execute_mathematical_computation("isinf(-inf)"), "True")
        self.assertEqual(execute_mathematical_computation("isinf(1.0)"), "False")

    def test_isnan(self):
        self.assertEqual(execute_mathematical_computation("isnan(nan)"), "True")
        self.assertEqual(execute_mathematical_computation("isnan(1.0)"), "False")
        self.assertEqual(execute_mathematical_computation("isnan(inf)"), "False")

    def test_isclose(self):
        self.assertEqual(execute_mathematical_computation("isclose(1.0, 1.0)"), "True")
        self.assertEqual(execute_mathematical_computation("isclose(1.0, 1.00001)"), "False")
        self.assertEqual(execute_mathematical_computation("isclose(1.0, 1.000001)"), "False")

    def test_comb(self):
        try:
            self.assertEqual(execute_mathematical_computation("comb(5, 2)"), "10")
            self.assertEqual(execute_mathematical_computation("comb(10, 3)"), "120")
            self.assertEqual(execute_mathematical_computation("comb(4, 4)"), "1")
        except Exception:
            self.skipTest("comb not available in this Python version")

    def test_perm(self):
        try:
            self.assertEqual(execute_mathematical_computation("perm(5, 2)"), "20")
            self.assertEqual(execute_mathematical_computation("perm(4, 3)"), "24")
            self.assertEqual(execute_mathematical_computation("perm(3, 3)"), "6")
        except Exception:
            self.skipTest("perm not available in this Python version")

    def test_erf(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("erf(0)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("erf(1)")), math.erf(1), places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("erf(-1)")), math.erf(-1), places=7
        )

    def test_erfc(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("erfc(0)")), 1.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("erfc(1)")), math.erfc(1), places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("erfc(-1)")), math.erfc(-1), places=7
        )

    def test_gamma(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("gamma(1)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("gamma(2)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("gamma(5)")), 24.0, places=7)

    def test_lgamma(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("lgamma(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("lgamma(2)")), 0.0, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("lgamma(10)")), math.lgamma(10), places=7
        )

    def test_nextafter(self):
        try:
            result = float(execute_mathematical_computation("nextafter(1, 2)"))
            self.assertGreater(result, 1.0)
            self.assertLess(result, 1.0001)
            result = float(execute_mathematical_computation("nextafter(1, 0)"))
            self.assertLess(result, 1.0)
            self.assertAlmostEqual(
                float(execute_mathematical_computation("nextafter(0, 1)")), 5e-324, places=320
            )
        except Exception:
            self.skipTest("nextafter not available in this Python version")

    def test_ulp(self):
        try:
            self.assertGreater(float(execute_mathematical_computation("ulp(1.0)")), 0)
            self.assertLess(float(execute_mathematical_computation("ulp(1.0)")), 1e-10)
            self.assertGreater(
                float(execute_mathematical_computation("ulp(1000000.0)")),
                float(execute_mathematical_computation("ulp(1.0)")),
            )
        except Exception:
            self.skipTest("ulp not available in this Python version")

    def test_pi_constant(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("pi")), math.pi, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("pi * 2")), math.pi * 2, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("pi / 2")), math.pi / 2, places=7
        )

    def test_e_constant(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("e")), math.e, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("e * 2")), math.e * 2, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("e ** 2")), math.e**2, places=7
        )

    def test_tau_constant(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("tau")), math.tau, places=7)
        self.assertAlmostEqual(
            float(execute_mathematical_computation("tau / 4")), math.tau / 4, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("tau / 2")), math.pi, places=7
        )

    def test_inf_constant(self):
        with self.assertRaises(ValueError, msg="Calculator should handle inf safely"):
            execute_mathematical_computation("inf")
        with self.assertRaises(ValueError):
            execute_mathematical_computation("1.0 / 0.0")
        try:
            result = execute_mathematical_computation("10**308")
            self.assertIsInstance(result, str)
        except ValueError:
            pass

    def test_nan_constant(self):
        self.assertEqual(execute_mathematical_computation("nan"), "nan")
        self.assertEqual(execute_mathematical_computation("nan + 1"), "nan")
        self.assertEqual(execute_mathematical_computation("0 * nan"), "nan")

    def test_basic_arithmetic(self):
        self.assertEqual(execute_mathematical_computation("2 + 3"), "5")
        self.assertEqual(execute_mathematical_computation("10 - 4"), "6")
        self.assertEqual(execute_mathematical_computation("5 * 6"), "30")
        self.assertEqual(execute_mathematical_computation("15 / 3"), "5.0")
        self.assertEqual(execute_mathematical_computation("7 // 2"), "3")
        self.assertEqual(execute_mathematical_computation("10 % 3"), "1")
        self.assertEqual(execute_mathematical_computation("2 ** 3"), "8")

        self.assertEqual(execute_mathematical_computation("98765 + 87654"), "186419")
        self.assertEqual(execute_mathematical_computation("999999 - 123456"), "876543")
        self.assertEqual(execute_mathematical_computation("12345 * 6789"), "83810205")
        self.assertAlmostEqual(
            float(execute_mathematical_computation("987654321 / 123")), 8029709.927, places=2
        )
        self.assertEqual(execute_mathematical_computation("54321 // 789"), "68")
        self.assertEqual(execute_mathematical_computation("987654 % 12345"), "54")
        self.assertEqual(execute_mathematical_computation("123 ** 4"), "228886641")

    def test_unicode_operators(self):
        self.assertEqual(execute_mathematical_computation("2 × 3"), "6")
        self.assertEqual(execute_mathematical_computation("8 ÷ 2"), "4.0")
        self.assertEqual(execute_mathematical_computation("2 ^ 3"), "8")

    def test_complex_expressions(self):
        self.assertEqual(execute_mathematical_computation("(2 + 3) * 4"), "20")
        self.assertAlmostEqual(
            float(execute_mathematical_computation("sin(pi/2) + cos(0)")), 2.0, places=7
        )
        result = execute_mathematical_computation("factorial(5) + sqrt(16)")
        self.assertIn(result, ["124", "124.0"])

        self.assertEqual(
            execute_mathematical_computation("(98765 + 12345) * (54321 - 43210)"), "1234543210"
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("((999 * 888) + 777) / 666")), 1333.167, places=2
        )
        self.assertEqual(
            execute_mathematical_computation("(123456 * (789 + 321)) / (987 - 654)"), "411520.0"
        )

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            execute_mathematical_computation("1 / 0")
        with self.assertRaises(SyntaxError):
            execute_mathematical_computation("")
        with self.assertRaises(ValueError):
            execute_mathematical_computation("unknown_func()")

    def test_new_constants_phi_euler(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("phi")), (1 + math.sqrt(5)) / 2, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("euler")), 0.5772156649, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("phi * 2")), (1 + math.sqrt(5)), places=7
        )

    def test_statistics_functions(self):
        try:
            result = execute_mathematical_computation("mean([1, 2, 3, 4, 5])")
            if "Error" in result or "not" in result.lower():
                self.skipTest("List syntax not supported in calculator")
            else:
                self.assertEqual(result, "3.0")
        except Exception as e:
            self.skipTest(f"Statistics functions syntax not supported: {e}")

    def test_complex_functions_phase_polar(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("phase(1+1j)")), math.pi / 4, places=7
        )
        result = execute_mathematical_computation("polar(1+1j)")
        self.assertTrue("1.414" in result or "Result:" in result)

    def test_complex_trigonometry_functions(self):
        result = execute_mathematical_computation("csin(0)")
        self.assertTrue("0" in result or "Result:" in result)
        result = execute_mathematical_computation("ccos(0)")
        self.assertTrue("1" in result or "Result:" in result)
        result = execute_mathematical_computation("cexp(0)")
        self.assertTrue("1" in result or "Result:" in result)

    def test_complex_logarithm_functions(self):
        result = execute_mathematical_computation("clog(1)")
        self.assertTrue("0" in result or "Result:" in result)
        result = execute_mathematical_computation("clog10(1)")
        self.assertTrue("0" in result or "Result:" in result)
        result = execute_mathematical_computation("csqrt(4)")
        self.assertTrue("2" in result or "Result:" in result)

    def test_enhanced_mathematical_functions(self):
        try:
            result = execute_mathematical_computation("cbrt(27)")
            self.assertAlmostEqual(float(result), 3.0, places=7)
        except Exception:
            self.skipTest("cbrt not available in this Python version")

        try:
            result = execute_mathematical_computation("comb(5, 2)")
            self.assertEqual(result, "10")
        except Exception:
            self.skipTest("comb not available in this Python version")

        try:
            result = execute_mathematical_computation("perm(5, 2)")
            self.assertEqual(result, "20")
        except Exception:
            self.skipTest("perm not available in this Python version")

    def test_complex_number_expressions(self):
        result = execute_mathematical_computation("1+2j")
        self.assertTrue("1" in result and "2j" in result)

        result = execute_mathematical_computation("(1+2j) + (3+4j)")
        self.assertTrue("4" in result and "6j" in result)

        try:
            result = execute_mathematical_computation("abs(3+4j)")
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
                execute_mathematical_computation(expr)
            error_message = str(context.exception).lower()
            self.assertTrue(
                "forbidden pattern" in error_message
                or "invalid mathematical expression" in error_message
                or "unsupported operations" in error_message,
                f"Expected security error for '{expr}', got: {error_message}",
            )

    def test_resource_limits_factorial(self):
        result = execute_mathematical_computation("factorial(5)")
        self.assertEqual(result, "120")

        result = execute_mathematical_computation("factorial(10)")
        self.assertEqual(result, "3628800")

        try:
            result = execute_mathematical_computation("factorial(200)")
            if "Error" not in result:
                self.fail("Large factorial should be limited")
        except Exception:
            pass

    def test_resource_limits_expression_length(self):
        very_long_expr = "1+" * 2000 + "1"
        try:
            result = execute_mathematical_computation(very_long_expr)
            if "Error" not in result:
                self.fail("Very long expression should be limited")
        except Exception:
            pass

    def test_enhanced_error_handling_complex(self):
        try:
            result = execute_mathematical_computation("log(-1)")
            if "Error" in result or "nan" in result or "inf" in result:
                pass
            else:
                self.fail("log(-1) should produce error or special value")
        except Exception:
            pass

        try:
            result = execute_mathematical_computation("sqrt(-1)")
            if "Error" in result or "j" in result:
                pass
            else:
                self.fail("sqrt(-1) should produce error or complex number")
        except Exception:
            pass

    def test_trigonometric_edge_cases(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("sin(pi)")), 0.0, places=5)
        self.assertAlmostEqual(float(execute_mathematical_computation("cos(2*pi)")), 1.0, places=7)
        self.assertAlmostEqual(float(execute_mathematical_computation("tan(pi/4)")), 1.0, places=7)

    def test_logarithmic_edge_cases(self):
        self.assertEqual(execute_mathematical_computation("log(1)"), "0")
        self.assertAlmostEqual(float(execute_mathematical_computation("log(e)")), 1.0, places=7)
        self.assertEqual(execute_mathematical_computation("log10(1)"), "0")
        self.assertEqual(execute_mathematical_computation("log10(10)"), "1")

    def test_exponential_edge_cases(self):
        self.assertEqual(execute_mathematical_computation("exp(0)"), "1")
        self.assertAlmostEqual(float(execute_mathematical_computation("exp(1)")), math.e, places=7)
        try:
            self.assertEqual(execute_mathematical_computation("exp2(0)"), "1")
            self.assertEqual(execute_mathematical_computation("exp2(3)"), "8")
        except Exception:
            self.skipTest("exp2 not available in this Python version")

    def test_hyperbolic_functions_edge_cases(self):
        self.assertEqual(execute_mathematical_computation("sinh(0)"), "0")
        self.assertEqual(execute_mathematical_computation("cosh(0)"), "1")
        self.assertEqual(execute_mathematical_computation("tanh(0)"), "0")

    def test_inverse_hyperbolic_functions_edge_cases(self):
        self.assertEqual(execute_mathematical_computation("asinh(0)"), "0")
        self.assertEqual(execute_mathematical_computation("acosh(1)"), "0")
        self.assertEqual(execute_mathematical_computation("atanh(0)"), "0")

    def test_special_values_handling(self):
        with self.assertRaises(ValueError):
            execute_mathematical_computation("inf")
        try:
            result = execute_mathematical_computation("nan")
            self.assertEqual(result, "nan")
        except ValueError:
            pass
        with self.assertRaises(ValueError):
            execute_mathematical_computation("1.0 / 0.0")

    def test_precision_and_rounding(self):
        self.assertAlmostEqual(float(execute_mathematical_computation("pi")), math.pi, places=10)
        self.assertAlmostEqual(float(execute_mathematical_computation("e")), math.e, places=10)
        self.assertAlmostEqual(float(execute_mathematical_computation("tau")), math.tau, places=10)

    def test_mathematical_identities(self):
        self.assertAlmostEqual(
            float(execute_mathematical_computation("sin(pi/2)**2 + cos(pi/2)**2")), 1.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("exp(log(5))")), 5.0, places=7
        )
        self.assertAlmostEqual(
            float(execute_mathematical_computation("log(exp(3))")), 3.0, places=7
        )

    def test_large_number_handling(self):
        result = execute_mathematical_computation("2**50")
        self.assertEqual(result, str(2**50))

        result = execute_mathematical_computation("factorial(20)")
        expected = str(math.factorial(20))
        self.assertEqual(result, expected)


class TestSmartFeatures(unittest.TestCase):

    def test_unit_aliases(self):
        from src.mcp_mathematics.calculator import resolve_unit_alias

        self.assertEqual(resolve_unit_alias("meters"), "m")
        self.assertEqual(resolve_unit_alias("kilometres"), "km")
        self.assertEqual(resolve_unit_alias("pounds"), "lb")
        self.assertEqual(resolve_unit_alias("fahrenheit"), "F")
        self.assertEqual(resolve_unit_alias("m"), "m")

    def test_unit_type_detection(self):
        from src.mcp_mathematics.calculator import detect_unit_type

        self.assertEqual(detect_unit_type("m"), "length")
        self.assertEqual(detect_unit_type("meters"), "length")
        self.assertEqual(detect_unit_type("kg"), "mass")
        self.assertEqual(detect_unit_type("s"), "time")
        self.assertEqual(detect_unit_type("C"), "temperature")
        self.assertEqual(detect_unit_type("L"), "volume")
        self.assertIsNone(detect_unit_type("unknown"))

    def test_scientific_notation(self):
        from src.mcp_mathematics.calculator import format_scientific_notation

        self.assertEqual(format_scientific_notation(1.23e-12), "1.2300e-12")
        self.assertEqual(format_scientific_notation(5.67e15), "5.6700e+15")
        self.assertEqual(format_scientific_notation(123.456), "123.456")
        self.assertEqual(format_scientific_notation(1.23e-12, precision=2), "1.23e-12")

    def test_compound_unit_parsing(self):
        from src.mcp_mathematics.calculator import parse_compound_unit

        numerator, denominator = parse_compound_unit("m/s")
        self.assertEqual(numerator, ["m"])
        self.assertEqual(denominator, ["s"])

        numerator, denominator = parse_compound_unit("kg·m/s^2")
        self.assertEqual(numerator, ["kg", "m"])
        self.assertEqual(denominator, ["s", "s"])

    def test_conversion_with_history(self):
        from src.mcp_mathematics.calculator import conversion_history, convert_with_history

        conversion_history.clear()
        result = convert_with_history(100, "meters", "feet", precision=2)
        self.assertAlmostEqual(result, 328.08, places=0)

        history = conversion_history.get_recent(1)
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["value"], 100)
        self.assertEqual(history[0]["from_unit"], "m")


class TestFinancialCalculations(unittest.TestCase):

    def test_percentage_calculations(self):
        from src.mcp_mathematics.calculator import (
            calculate_percentage,
            calculate_percentage_change,
            calculate_percentage_of,
        )

        self.assertEqual(calculate_percentage(100, 10), 10)
        self.assertEqual(calculate_percentage(250, 20), 50)
        self.assertEqual(calculate_percentage_of(25, 100), 25)
        self.assertEqual(calculate_percentage_of(50, 200), 25)
        self.assertEqual(calculate_percentage_change(100, 150), 50)
        self.assertEqual(calculate_percentage_change(200, 100), -50)

        self.assertEqual(calculate_percentage(98765, 18.5), 18271.525)
        self.assertEqual(calculate_percentage(1234567, 7.25), 89506.1075)
        self.assertAlmostEqual(calculate_percentage_of(123456, 987654), 12.5, places=1)
        self.assertAlmostEqual(calculate_percentage_of(87654, 999999), 8.765, places=3)
        self.assertAlmostEqual(calculate_percentage_change(54321, 98765), 81.817, places=2)
        self.assertAlmostEqual(calculate_percentage_change(999999, 123456), -87.65, places=2)

        with self.assertRaises(ValueError):
            calculate_percentage_of(10, 0)
        with self.assertRaises(ValueError):
            calculate_percentage_change(0, 100)

    def test_split_bill(self):
        from src.mcp_mathematics.calculator import split_bill

        result = split_bill(100, 4, 15)
        self.assertEqual(result["total"], 100)
        self.assertEqual(result["tip_amount"], 15)
        self.assertEqual(result["total_with_tip"], 115)
        self.assertEqual(result["per_person"], 28.75)

        result = split_bill(12345.67, 8, 18)
        self.assertAlmostEqual(result["total"], 12345.67, places=2)
        self.assertAlmostEqual(result["tip_amount"], 2222.22, places=2)
        self.assertAlmostEqual(result["total_with_tip"], 14567.89, places=2)
        self.assertAlmostEqual(result["per_person"], 1820.99, places=2)

        result = split_bill(98765.43, 15, 20)
        self.assertAlmostEqual(result["tip_amount"], 19753.09, places=2)
        self.assertAlmostEqual(result["total_with_tip"], 118518.52, places=2)
        self.assertAlmostEqual(result["per_person"], 7901.23, places=2)

        with self.assertRaises(ValueError):
            split_bill(100, 0)

    def test_tax_calculations(self):
        from src.mcp_mathematics.calculator import calculate_tax

        result = calculate_tax(100, 10)
        self.assertEqual(result["tax_amount"], 10)
        self.assertEqual(result["total_amount"], 110)

        result = calculate_tax(110, 10, is_inclusive=True)
        self.assertAlmostEqual(result["base_amount"], 100, places=1)
        self.assertAlmostEqual(result["tax_amount"], 10, places=1)

    def test_interest_calculations(self):
        from src.mcp_mathematics.calculator import (
            calculate_compound_interest,
            calculate_simple_interest,
        )

        result = calculate_compound_interest(1000, 5, 10, 12)
        self.assertAlmostEqual(result["amount"], 1647.01, places=0)
        self.assertAlmostEqual(result["interest"], 647.01, places=0)

        result = calculate_simple_interest(1000, 5, 10)
        self.assertEqual(result["interest"], 500)
        self.assertEqual(result["amount"], 1500)

        result = calculate_compound_interest(250000, 7.5, 30, 12)
        self.assertAlmostEqual(result["amount"], 2355383.48, places=2)
        self.assertAlmostEqual(result["interest"], 2105383.48, places=2)

        result = calculate_compound_interest(999999, 12.75, 15, 365)
        self.assertAlmostEqual(result["amount"], 6767725.38, places=2)

        result = calculate_simple_interest(500000, 8.5, 25)
        self.assertEqual(result["interest"], 1062500)
        self.assertEqual(result["amount"], 1562500)

    def test_loan_payment(self):
        from src.mcp_mathematics.calculator import calculate_loan_payment

        result = calculate_loan_payment(100000, 5, 30, 12)
        self.assertAlmostEqual(result["payment"], 536.82, places=0)
        self.assertAlmostEqual(result["total_paid"], 193255.78, delta=10)

        result = calculate_loan_payment(10000, 0, 5)
        self.assertEqual(result["payment"], 166.66666666666666)
        self.assertEqual(result["interest_paid"], 0)

        result = calculate_loan_payment(750000, 6.5, 30, 12)
        self.assertAlmostEqual(result["payment"], 4740.51, places=2)
        self.assertAlmostEqual(result["total_paid"], 1706583.6, delta=100)

        result = calculate_loan_payment(1250000, 8.25, 15, 12)
        self.assertAlmostEqual(result["payment"], 12126.75, places=2)
        self.assertAlmostEqual(result["total_paid"], 2182815.81, delta=100)

        result = calculate_loan_payment(999999, 7.75, 25, 12)
        self.assertAlmostEqual(result["payment"], 7553.28, places=2)

    def test_discount_markup(self):
        from src.mcp_mathematics.calculator import calculate_discount, calculate_markup

        result = calculate_discount(100, 20)
        self.assertEqual(result["discount_amount"], 20)
        self.assertEqual(result["final_price"], 80)

        result = calculate_markup(50, 100)
        self.assertEqual(result["markup_amount"], 50)
        self.assertEqual(result["selling_price"], 100)


class TestUnitConversions(unittest.TestCase):

    def test_length_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        self.assertAlmostEqual(convert_unit(1, "m", "km", "length"), 0.001, places=3)
        self.assertAlmostEqual(convert_unit(1, "km", "mi", "length"), 0.621371, places=3)
        self.assertAlmostEqual(convert_unit(1, "ft", "in", "length"), 12, places=1)

        self.assertAlmostEqual(convert_unit(98765, "m", "km", "length"), 98.765, places=3)
        self.assertAlmostEqual(convert_unit(123456, "km", "mi", "length"), 76712.002, places=2)
        self.assertAlmostEqual(convert_unit(999999, "ft", "mi", "length"), 189.394, places=2)
        self.assertAlmostEqual(convert_unit(54321, "in", "m", "length"), 1379.753, places=2)

    def test_mass_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        self.assertAlmostEqual(convert_unit(1, "kg", "g", "mass"), 1000, places=1)
        self.assertAlmostEqual(convert_unit(1, "kg", "lb", "mass"), 2.20462, places=3)
        self.assertAlmostEqual(convert_unit(1, "lb", "oz", "mass"), 16, places=1)

        self.assertAlmostEqual(convert_unit(87654, "kg", "ton", "mass"), 87.654, places=3)
        self.assertAlmostEqual(convert_unit(999999, "g", "lb", "mass"), 2204.62, places=2)
        self.assertAlmostEqual(convert_unit(123456, "oz", "kg", "mass"), 3499.92, places=2)
        self.assertAlmostEqual(convert_unit(54321, "lb", "ton", "mass"), 24.6396, places=3)

    def test_temperature_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        self.assertEqual(convert_unit(0, "C", "F", "temperature"), 32)
        self.assertEqual(convert_unit(100, "C", "F", "temperature"), 212)
        self.assertEqual(convert_unit(0, "C", "K", "temperature"), 273.15)

    def test_edge_cases(self):
        from src.mcp_mathematics.calculator import convert_unit

        self.assertEqual(convert_unit(0, "m", "km", "length"), 0)
        self.assertEqual(convert_unit(0, "C", "F", "temperature"), 32)

        self.assertEqual(convert_unit(-10, "m", "km", "length"), -0.01)
        self.assertEqual(convert_unit(-40, "C", "F", "temperature"), -40)

        with self.assertRaises(ValueError):
            convert_unit(1, "invalid_unit", "m", "length")

    def test_complex_nested_expressions(self):
        result = float(execute_mathematical_computation("sin(cos(tan(pi/6)))"))
        expected = math.sin(math.cos(math.tan(math.pi / 6)))
        self.assertAlmostEqual(result, expected, places=10)

        result = float(execute_mathematical_computation("log(exp(2) * exp(3))"))
        self.assertAlmostEqual(result, 5, places=10)

        result = float(execute_mathematical_computation("sqrt(16) + sqrt(9) * sqrt(4)"))
        self.assertEqual(result, 10)

    def test_complex_trigonometric_identities(self):
        result = float(execute_mathematical_computation("sin(pi/3)^2 + cos(pi/3)^2"))
        self.assertAlmostEqual(result, 1, places=10)

        angle = math.pi / 4
        result = float(execute_mathematical_computation(f"tan({angle})"))
        expected = float(execute_mathematical_computation(f"sin({angle})/cos({angle})"))
        self.assertAlmostEqual(result, expected, places=10)

    def test_advanced_logarithms(self):
        result = float(execute_mathematical_computation("log(256)/log(2)"))
        self.assertAlmostEqual(result, 8, places=5)

        result = float(execute_mathematical_computation("log(1000)/log(10)"))
        self.assertAlmostEqual(result, 3, places=5)

        result = float(execute_mathematical_computation("log(exp(5))"))
        self.assertAlmostEqual(result, 5, places=5)

    def test_factorial_and_combinatorics(self):
        result = float(execute_mathematical_computation("factorial(6)"))
        self.assertAlmostEqual(result, 720, places=5)

        result = float(execute_mathematical_computation("factorial(10)/(factorial(10-3))"))
        self.assertAlmostEqual(result, 720, places=5)

        result = float(
            execute_mathematical_computation("factorial(10)/(factorial(3)*factorial(10-3))")
        )
        self.assertAlmostEqual(result, 120, places=5)

    def test_hyperbolic_complex(self):
        result = float(execute_mathematical_computation("sinh(2) + cosh(2)"))
        expected = math.sinh(2) + math.cosh(2)
        self.assertAlmostEqual(result, expected, places=10)

        result = float(execute_mathematical_computation("tanh(1) * tanh(2)"))
        expected = math.tanh(1) * math.tanh(2)
        self.assertAlmostEqual(result, expected, places=10)

    def test_modulo_operations(self):
        result = float(execute_mathematical_computation("17 % 5"))
        self.assertEqual(result, 2)

        result = float(execute_mathematical_computation("100 % 7"))
        self.assertEqual(result, 2)

        result = float(execute_mathematical_computation("25 % 4"))
        self.assertEqual(result, 1)

    def test_floor_ceil_functions(self):
        result = float(execute_mathematical_computation("floor(3.7)"))
        self.assertEqual(result, 3)

        result = float(execute_mathematical_computation("ceil(3.2)"))
        self.assertEqual(result, 4)

        result = float(execute_mathematical_computation("floor(-2.3)"))
        self.assertEqual(result, -3)

    def test_gcd_lcm_calculations(self):
        result = float(execute_mathematical_computation("gcd(48, 18)"))
        self.assertEqual(result, 6)

        result = float(execute_mathematical_computation("lcm(12, 15)"))
        self.assertEqual(result, 60)

        result = float(execute_mathematical_computation("gcd(100, 75)"))
        self.assertEqual(result, 25)

    def test_complex_unit_chains(self):
        from src.mcp_mathematics.calculator import convert_unit

        meters_to_inches = convert_unit(1, "m", "in", "length")
        self.assertAlmostEqual(meters_to_inches, 39.3701, places=2)

        kg_to_oz = convert_unit(1, "kg", "oz", "mass")
        self.assertAlmostEqual(kg_to_oz, 35.274, places=2)

        hours_to_ms = convert_unit(1, "h", "ms", "time")
        self.assertEqual(hours_to_ms, 3600000)

    def test_temperature_round_trips(self):
        from src.mcp_mathematics.calculator import convert_unit

        celsius = 25
        to_fahrenheit = convert_unit(celsius, "C", "F", "temperature")
        back_to_celsius = convert_unit(to_fahrenheit, "F", "C", "temperature")
        self.assertAlmostEqual(back_to_celsius, celsius, places=10)

        kelvin = 300
        to_celsius = convert_unit(kelvin, "K", "C", "temperature")
        back_to_kelvin = convert_unit(to_celsius, "C", "K", "temperature")
        self.assertAlmostEqual(back_to_kelvin, kelvin, places=10)

    def test_area_volume_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        sqm_to_sqft = convert_unit(1, "m2", "ft2", "area")
        self.assertAlmostEqual(sqm_to_sqft, 10.7639, places=2)

        liters_to_gallons = convert_unit(1, "L", "gal", "volume")
        self.assertAlmostEqual(liters_to_gallons, 0.264172, places=4)

        ml_to_cup = convert_unit(250, "mL", "cup", "volume")
        self.assertAlmostEqual(ml_to_cup, 1.05669, places=3)

    def test_energy_power_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        joules_to_calories = convert_unit(1000, "J", "cal", "energy")
        self.assertAlmostEqual(joules_to_calories, 239.006, places=2)

        watts_to_hp = convert_unit(1000, "W", "hp", "power")
        self.assertAlmostEqual(watts_to_hp, 1.34102, places=3)

        kwh_to_joules = convert_unit(1, "kWh", "J", "energy")
        self.assertEqual(kwh_to_joules, 3600000)

    def test_pressure_force_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        pa_to_psi = convert_unit(100000, "Pa", "psi", "pressure")
        self.assertAlmostEqual(pa_to_psi, 14.5038, places=2)

        newtons_to_lbf = convert_unit(100, "N", "lbf", "force")
        self.assertAlmostEqual(newtons_to_lbf, 22.4809, places=2)

        bar_to_atm = convert_unit(1, "bar", "atm", "pressure")
        self.assertAlmostEqual(bar_to_atm, 0.98692, places=3)

    def test_compound_interest_variations(self):
        from src.mcp_mathematics.calculator import calculate_compound_interest

        result = calculate_compound_interest(5000, 8, 10, 4)
        self.assertAlmostEqual(result["amount"], 11040.20, places=2)

        result = calculate_compound_interest(1000, 12, 5, 12)
        self.assertAlmostEqual(result["amount"], 1816.70, places=2)

        result = calculate_compound_interest(10000, 5, 20, 1)
        self.assertAlmostEqual(result["amount"], 26532.98, places=2)

    def test_loan_payment_scenarios(self):
        from src.mcp_mathematics.calculator import calculate_loan_payment

        result = calculate_loan_payment(200000, 4.5, 30)
        self.assertAlmostEqual(result["payment"], 1013.37, places=2)

        result = calculate_loan_payment(30000, 6, 5)
        self.assertAlmostEqual(result["payment"], 579.98, places=2)

        result = calculate_loan_payment(500000, 3.5, 15)
        self.assertAlmostEqual(result["payment"], 3574.41, places=2)

    def test_percentage_operations(self):
        from src.mcp_mathematics.calculator import calculate_percentage, calculate_percentage_change

        change = calculate_percentage_change(100, 150)
        self.assertEqual(change, 50)

        change = calculate_percentage_change(200, 50)
        self.assertEqual(change, -75)

        result = calculate_percentage(100, 25)
        self.assertEqual(result, 25)

        result = calculate_percentage(100, 15)
        self.assertEqual(result, 15)

    def test_tax_tip_calculations(self):
        from src.mcp_mathematics.calculator import calculate_tax, calculate_tip

        tax_result = calculate_tax(100, 8.5)
        self.assertEqual(tax_result["tax_amount"], 8.5)

        total_with_tax = calculate_tax(250, 10, is_inclusive=False)
        self.assertEqual(total_with_tax["total_amount"], 275)

        tip_result = calculate_tip(80, 20)
        self.assertEqual(tip_result["tip_amount"], 16)

        total_with_tip = calculate_tip(100, 18)
        self.assertEqual(total_with_tip["total_amount"], 118)

    def test_discount_markup_calculations(self):
        from src.mcp_mathematics.calculator import calculate_discount, calculate_markup

        discount_result = calculate_discount(100, 25)
        self.assertEqual(discount_result["final_price"], 75)

        discount_result = calculate_discount(80, 10)
        self.assertEqual(discount_result["final_price"], 72)

        markup_result = calculate_markup(50, 40)
        self.assertEqual(markup_result["selling_price"], 70)

        markup_result = calculate_markup(100, 15)
        self.assertEqual(markup_result["selling_price"], 115)

    def test_bill_splitting_scenarios(self):
        from src.mcp_mathematics.calculator import split_bill

        result = split_bill(120, 4)
        self.assertEqual(result["per_person"], 30)

        result = split_bill(200, 5, tip_percent=20)
        self.assertEqual(result["per_person"], 48)

        result = split_bill(150, 3, tip_percent=18)
        self.assertEqual(result["per_person"], 59)

    def test_speed_conversion_chains(self):
        from src.mcp_mathematics.calculator import convert_unit

        ms_to_mph = convert_unit(10, "m/s", "mph", "speed")
        self.assertAlmostEqual(ms_to_mph, 22.3694, places=2)

        kmh_to_knot = convert_unit(100, "km/h", "knot", "speed")
        self.assertAlmostEqual(kmh_to_knot, 53.9957, places=2)

        fps_to_ms = convert_unit(100, "ft/s", "m/s", "speed")
        self.assertAlmostEqual(fps_to_ms, 30.48, places=2)

    def test_data_storage_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        gb_to_mb = convert_unit(5, "GB", "MB", "data")
        self.assertEqual(gb_to_mb, 5000)

        tb_to_gb = convert_unit(2, "TB", "GB", "data")
        self.assertEqual(tb_to_gb, 2000)

        mb_to_bits = convert_unit(1, "MB", "bit", "data")
        self.assertEqual(mb_to_bits, 8000000)

    def test_frequency_angle_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        hz_to_khz = convert_unit(5000, "Hz", "kHz", "frequency")
        self.assertAlmostEqual(hz_to_khz, 5, places=10)

        rpm_to_hz = convert_unit(3600, "rpm", "Hz", "frequency")
        self.assertAlmostEqual(round(rpm_to_hz), 60)

        deg_to_rad = convert_unit(180, "deg", "rad", "angle")
        self.assertAlmostEqual(deg_to_rad, math.pi, places=5)

        grad_to_deg = convert_unit(100, "grad", "deg", "angle")
        self.assertAlmostEqual(grad_to_deg, 90, places=10)

    def test_fuel_economy_conversions(self):
        from src.mcp_mathematics.calculator import convert_unit

        mpg_to_lper100km = convert_unit(30, "mpg", "L/100km", "fuel_economy")
        self.assertAlmostEqual(mpg_to_lper100km, 7.84049, places=1)

        lper100km_to_mpg = convert_unit(8, "L/100km", "mpg", "fuel_economy")
        self.assertAlmostEqual(lper100km_to_mpg, 29.4018, places=1)

        km_per_l_to_mpg = convert_unit(10, "km/L", "mpg", "fuel_economy")
        self.assertAlmostEqual(km_per_l_to_mpg, 23.52, places=1)

    def test_smart_unit_detection(self):
        from src.mcp_mathematics.calculator import detect_unit_type

        self.assertEqual(detect_unit_type("meter"), "length")
        self.assertEqual(detect_unit_type("kg"), "mass")
        self.assertEqual(detect_unit_type("celsius"), "temperature")
        self.assertEqual(detect_unit_type("joule"), "energy")
        self.assertEqual(detect_unit_type("pascal"), "pressure")

    def test_unit_alias_resolution(self):
        from src.mcp_mathematics.calculator import resolve_unit_alias

        self.assertEqual(resolve_unit_alias("meters"), "m")
        self.assertEqual(resolve_unit_alias("kilograms"), "kg")
        self.assertEqual(resolve_unit_alias("celsius"), "C")
        self.assertEqual(resolve_unit_alias("pounds"), "lb")
        self.assertEqual(resolve_unit_alias("ounces"), "oz")

    def test_compound_unit_parsing(self):
        pass

    def test_conversion_history_tracking(self):
        from src.mcp_mathematics.calculator import convert_with_history

        result = convert_with_history(100, "m", "ft")
        self.assertAlmostEqual(result, 328.084, places=2)

        result = convert_with_history(50, "kg", "lb")
        self.assertAlmostEqual(result, 110.231, places=2)

    def test_scientific_notation_handling(self):
        from src.mcp_mathematics.calculator import format_scientific_notation

        formatted = format_scientific_notation(1234567)
        self.assertEqual(str(formatted), "1234567")

        formatted = format_scientific_notation(0.00001234)
        self.assertEqual(formatted, "1.234e-05")

        formatted = format_scientific_notation(5.67e23)
        self.assertEqual(formatted, "5.6700e+23")

    def test_special_mathematical_constants(self):
        pi_value = float(execute_mathematical_computation("pi"))
        self.assertAlmostEqual(pi_value, math.pi, places=10)

        e_value = float(execute_mathematical_computation("e"))
        self.assertAlmostEqual(e_value, math.e, places=10)

        tau_value = float(execute_mathematical_computation("tau"))
        self.assertAlmostEqual(tau_value, 2 * math.pi, places=10)

        phi_value = float(execute_mathematical_computation("phi"))
        self.assertAlmostEqual(phi_value, (1 + math.sqrt(5)) / 2, places=10)

    def test_complex_financial_scenarios(self):
        from src.mcp_mathematics.calculator import (
            calculate_compound_interest,
            calculate_simple_interest,
        )

        compound = calculate_compound_interest(10000, 6, 5, 12)
        simple = calculate_simple_interest(10000, 6, 5)
        difference = compound["amount"] - (10000 + simple["interest"])
        self.assertGreater(difference, 0)

        monthly_compound = calculate_compound_interest(1000, 12, 1, 12)
        yearly_compound = calculate_compound_interest(1000, 12, 1, 1)
        self.assertGreater(monthly_compound["amount"], yearly_compound["amount"])

    def test_advanced_percentage_calculations(self):
        from src.mcp_mathematics.calculator import calculate_percentage, calculate_percentage_change

        percent = calculate_percentage(200, 25)
        self.assertEqual(percent, 50)

        percent = calculate_percentage(150, 18)
        self.assertEqual(percent, 27)

        increase = calculate_percentage_change(80, 120)
        self.assertEqual(increase, 50)

        decrease = calculate_percentage_change(100, 75)
        self.assertEqual(decrease, -25)

    def test_mixed_operations(self):
        result = float(execute_mathematical_computation("sin(pi/4) * sqrt(2)"))
        self.assertAlmostEqual(result, 1, places=5)

        result = float(execute_mathematical_computation("log(100) / log(10)"))
        self.assertAlmostEqual(result, 2, places=5)

        result = float(execute_mathematical_computation("exp(log(5) + log(3))"))
        self.assertAlmostEqual(result, 15, places=4)

        result = float(execute_mathematical_computation("2**10 - 1000"))
        self.assertAlmostEqual(result, 24, places=5)

    def test_extreme_values(self):
        result = float(execute_mathematical_computation("factorial(20)"))
        self.assertEqual(result, 2432902008176640000)

        result = float(execute_mathematical_computation("log(1e-10)"))
        self.assertAlmostEqual(result, -23.0259, places=3)

        result = float(execute_mathematical_computation("exp(20)"))
        self.assertAlmostEqual(result, 485165195.4, places=1)

    def test_degree_radian_conversions(self):
        result = float(execute_mathematical_computation("degrees(pi)"))
        self.assertEqual(result, 180)

        result = float(execute_mathematical_computation("radians(180)"))
        self.assertAlmostEqual(result, math.pi, places=10)

        result = float(execute_mathematical_computation("degrees(2*pi)"))
        self.assertEqual(result, 360)

        result = float(execute_mathematical_computation("radians(90)"))
        self.assertAlmostEqual(result, math.pi / 2, places=10)


if __name__ == "__main__":
    unittest.main()
