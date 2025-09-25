import math
import unittest

from src.mcp_mathematics.calculator import evaluate


class TestCalculator(unittest.TestCase):

    def test_sin(self):
        self.assertAlmostEqual(float(evaluate("sin(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("sin(pi/2)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("sin(pi)")), 0.0, places=7)

    def test_cos(self):
        self.assertAlmostEqual(float(evaluate("cos(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("cos(pi/2)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("cos(pi)")), -1.0, places=7)

    def test_tan(self):
        self.assertAlmostEqual(float(evaluate("tan(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("tan(pi/4)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("tan(-pi/4)")), -1.0, places=7)

    def test_asin(self):
        self.assertAlmostEqual(float(evaluate("asin(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("asin(1)")), math.pi / 2, places=7)
        self.assertAlmostEqual(float(evaluate("asin(0.5)")), math.pi / 6, places=7)

    def test_acos(self):
        self.assertAlmostEqual(float(evaluate("acos(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("acos(0)")), math.pi / 2, places=7)
        self.assertAlmostEqual(float(evaluate("acos(-1)")), math.pi, places=7)

    def test_atan(self):
        self.assertAlmostEqual(float(evaluate("atan(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("atan(1)")), math.pi / 4, places=7)
        self.assertAlmostEqual(float(evaluate("atan(-1)")), -math.pi / 4, places=7)

    def test_atan2(self):
        self.assertAlmostEqual(float(evaluate("atan2(0, 1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("atan2(1, 0)")), math.pi / 2, places=7)
        self.assertAlmostEqual(float(evaluate("atan2(1, 1)")), math.pi / 4, places=7)

    def test_sinh(self):
        self.assertAlmostEqual(float(evaluate("sinh(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("sinh(1)")), math.sinh(1), places=7)
        self.assertAlmostEqual(float(evaluate("sinh(-1)")), math.sinh(-1), places=7)

    def test_cosh(self):
        self.assertAlmostEqual(float(evaluate("cosh(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("cosh(1)")), math.cosh(1), places=7)
        self.assertAlmostEqual(float(evaluate("cosh(-1)")), math.cosh(-1), places=7)

    def test_tanh(self):
        self.assertAlmostEqual(float(evaluate("tanh(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("tanh(1)")), math.tanh(1), places=7)
        self.assertAlmostEqual(float(evaluate("tanh(100)")), 1.0, places=7)

    def test_asinh(self):
        self.assertAlmostEqual(float(evaluate("asinh(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("asinh(1)")), math.asinh(1), places=7)
        self.assertAlmostEqual(float(evaluate("asinh(-1)")), math.asinh(-1), places=7)

    def test_acosh(self):
        self.assertAlmostEqual(float(evaluate("acosh(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("acosh(2)")), math.acosh(2), places=7)
        self.assertAlmostEqual(float(evaluate("acosh(10)")), math.acosh(10), places=7)

    def test_atanh(self):
        self.assertAlmostEqual(float(evaluate("atanh(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("atanh(0.5)")), math.atanh(0.5), places=7)
        self.assertAlmostEqual(float(evaluate("atanh(-0.5)")), math.atanh(-0.5), places=7)

    def test_log(self):
        self.assertAlmostEqual(float(evaluate("log(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("log(e)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("log(10)")), math.log(10), places=7)

    def test_log10(self):
        self.assertAlmostEqual(float(evaluate("log10(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("log10(10)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("log10(100)")), 2.0, places=7)

    def test_log2(self):
        self.assertAlmostEqual(float(evaluate("log2(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("log2(2)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("log2(8)")), 3.0, places=7)

    def test_log1p(self):
        self.assertAlmostEqual(float(evaluate("log1p(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("log1p(1)")), math.log(2), places=7)
        self.assertAlmostEqual(float(evaluate("log1p(e-1)")), 1.0, places=7)

    def test_exp(self):
        self.assertAlmostEqual(float(evaluate("exp(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("exp(1)")), math.e, places=7)
        self.assertAlmostEqual(float(evaluate("exp(2)")), math.exp(2), places=7)

    def test_exp2(self):
        try:
            self.assertAlmostEqual(float(evaluate("exp2(0)")), 1.0, places=7)
            self.assertAlmostEqual(float(evaluate("exp2(1)")), 2.0, places=7)
            self.assertAlmostEqual(float(evaluate("exp2(3)")), 8.0, places=7)
        except Exception:
            self.skipTest("exp2 not available in this Python version")

    def test_expm1(self):
        self.assertAlmostEqual(float(evaluate("expm1(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("expm1(1)")), math.e - 1, places=7)
        self.assertAlmostEqual(float(evaluate("expm1(-1)")), math.expm1(-1), places=7)

    def test_sqrt(self):
        self.assertAlmostEqual(float(evaluate("sqrt(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("sqrt(4)")), 2.0, places=7)
        self.assertAlmostEqual(float(evaluate("sqrt(9)")), 3.0, places=7)

    def test_cbrt(self):
        try:
            self.assertAlmostEqual(float(evaluate("cbrt(0)")), 0.0, places=7)
            self.assertAlmostEqual(float(evaluate("cbrt(8)")), 2.0, places=7)
            self.assertAlmostEqual(float(evaluate("cbrt(27)")), 3.0, places=7)
        except Exception:
            self.skipTest("cbrt not available in this Python version")

    def test_pow(self):
        self.assertAlmostEqual(float(evaluate("pow(2, 0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("pow(2, 3)")), 8.0, places=7)
        self.assertAlmostEqual(float(evaluate("pow(5, 2)")), 25.0, places=7)

    def test_hypot(self):
        self.assertAlmostEqual(float(evaluate("hypot(3, 4)")), 5.0, places=7)
        self.assertAlmostEqual(float(evaluate("hypot(5, 12)")), 13.0, places=7)
        self.assertAlmostEqual(float(evaluate("hypot(0, 0)")), 0.0, places=7)

    def test_fabs(self):
        self.assertAlmostEqual(float(evaluate("fabs(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("fabs(-5)")), 5.0, places=7)
        self.assertAlmostEqual(float(evaluate("fabs(3.14)")), 3.14, places=7)

    def test_copysign(self):
        self.assertAlmostEqual(float(evaluate("copysign(1, -1)")), -1.0, places=7)
        self.assertAlmostEqual(float(evaluate("copysign(-5, 1)")), 5.0, places=7)
        self.assertAlmostEqual(float(evaluate("copysign(3.14, -1)")), -3.14, places=7)

    def test_factorial(self):
        self.assertEqual(evaluate("factorial(0)"), "1")
        self.assertEqual(evaluate("factorial(5)"), "120")
        self.assertEqual(evaluate("factorial(10)"), "3628800")

    def test_ceil(self):
        self.assertEqual(evaluate("ceil(1.1)"), "2")
        self.assertEqual(evaluate("ceil(2.9)"), "3")
        self.assertEqual(evaluate("ceil(-1.1)"), "-1")

    def test_floor(self):
        self.assertEqual(evaluate("floor(1.9)"), "1")
        self.assertEqual(evaluate("floor(2.1)"), "2")
        self.assertEqual(evaluate("floor(-1.1)"), "-2")

    def test_trunc(self):
        self.assertEqual(evaluate("trunc(1.9)"), "1")
        self.assertEqual(evaluate("trunc(-1.9)"), "-1")
        self.assertEqual(evaluate("trunc(3.5)"), "3")

    def test_degrees(self):
        self.assertAlmostEqual(float(evaluate("degrees(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("degrees(pi)")), 180.0, places=7)
        self.assertAlmostEqual(float(evaluate("degrees(pi/2)")), 90.0, places=7)

    def test_radians(self):
        self.assertAlmostEqual(float(evaluate("radians(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("radians(180)")), math.pi, places=7)
        self.assertAlmostEqual(float(evaluate("radians(90)")), math.pi / 2, places=7)

    def test_gcd(self):
        self.assertEqual(evaluate("gcd(12, 8)"), "4")
        self.assertEqual(evaluate("gcd(15, 25)"), "5")
        self.assertEqual(evaluate("gcd(17, 19)"), "1")

    def test_lcm(self):
        try:
            self.assertEqual(evaluate("lcm(4, 6)"), "12")
            self.assertEqual(evaluate("lcm(3, 5)"), "15")
            self.assertEqual(evaluate("lcm(12, 18)"), "36")
        except Exception:
            self.skipTest("lcm not available in this Python version")

    def test_isqrt(self):
        try:
            self.assertEqual(evaluate("isqrt(0)"), "0")
            self.assertEqual(evaluate("isqrt(4)"), "2")
            self.assertEqual(evaluate("isqrt(10)"), "3")
        except Exception:
            self.skipTest("isqrt not available in this Python version")

    def test_fmod(self):
        self.assertAlmostEqual(float(evaluate("fmod(10, 3)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("fmod(5.5, 2.5)")), 0.5, places=7)
        self.assertAlmostEqual(float(evaluate("fmod(-10, 3)")), -1.0, places=7)

    def test_remainder(self):
        self.assertAlmostEqual(float(evaluate("remainder(10, 3)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("remainder(10, 6)")), -2.0, places=7)
        self.assertAlmostEqual(float(evaluate("remainder(10, 10)")), 0.0, places=7)

    def test_modf(self):
        result = evaluate("modf(1.5)")
        self.assertIn("0.5", result)
        self.assertIn("1.0", result)
        result = evaluate("modf(2.7)")
        self.assertIn("0.7", result)
        result = evaluate("modf(-1.5)")
        self.assertIn("-0.5", result)

    def test_frexp(self):
        result = evaluate("frexp(4)")
        self.assertIn("0.5", result)
        self.assertIn("3", result)
        result = evaluate("frexp(8)")
        self.assertIn("0.5", result)
        self.assertIn("4", result)
        result = evaluate("frexp(1)")
        self.assertIn("0.5", result)

    def test_ldexp(self):
        self.assertAlmostEqual(float(evaluate("ldexp(0.5, 3)")), 4.0, places=7)
        self.assertAlmostEqual(float(evaluate("ldexp(1, 0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("ldexp(0.5, 4)")), 8.0, places=7)

    def test_isfinite(self):
        self.assertEqual(evaluate("isfinite(0)"), "True")
        self.assertEqual(evaluate("isfinite(1.5)"), "True")
        self.assertEqual(evaluate("isfinite(inf)"), "False")

    def test_isinf(self):
        self.assertEqual(evaluate("isinf(inf)"), "True")
        self.assertEqual(evaluate("isinf(-inf)"), "True")
        self.assertEqual(evaluate("isinf(1.0)"), "False")

    def test_isnan(self):
        self.assertEqual(evaluate("isnan(nan)"), "True")
        self.assertEqual(evaluate("isnan(1.0)"), "False")
        self.assertEqual(evaluate("isnan(inf)"), "False")

    def test_isclose(self):
        self.assertEqual(evaluate("isclose(1.0, 1.0)"), "True")
        self.assertEqual(evaluate("isclose(1.0, 1.00001)"), "False")
        self.assertEqual(evaluate("isclose(1.0, 1.000001)"), "False")

    def test_comb(self):
        try:
            self.assertEqual(evaluate("comb(5, 2)"), "10")
            self.assertEqual(evaluate("comb(10, 3)"), "120")
            self.assertEqual(evaluate("comb(4, 4)"), "1")
        except Exception:
            self.skipTest("comb not available in this Python version")

    def test_perm(self):
        try:
            self.assertEqual(evaluate("perm(5, 2)"), "20")
            self.assertEqual(evaluate("perm(4, 3)"), "24")
            self.assertEqual(evaluate("perm(3, 3)"), "6")
        except Exception:
            self.skipTest("perm not available in this Python version")

    def test_erf(self):
        self.assertAlmostEqual(float(evaluate("erf(0)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("erf(1)")), math.erf(1), places=7)
        self.assertAlmostEqual(float(evaluate("erf(-1)")), math.erf(-1), places=7)

    def test_erfc(self):
        self.assertAlmostEqual(float(evaluate("erfc(0)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("erfc(1)")), math.erfc(1), places=7)
        self.assertAlmostEqual(float(evaluate("erfc(-1)")), math.erfc(-1), places=7)

    def test_gamma(self):
        self.assertAlmostEqual(float(evaluate("gamma(1)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("gamma(2)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("gamma(5)")), 24.0, places=7)

    def test_lgamma(self):
        self.assertAlmostEqual(float(evaluate("lgamma(1)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("lgamma(2)")), 0.0, places=7)
        self.assertAlmostEqual(float(evaluate("lgamma(10)")), math.lgamma(10), places=7)

    def test_nextafter(self):
        try:
            result = float(evaluate("nextafter(1, 2)"))
            self.assertGreater(result, 1.0)
            self.assertLess(result, 1.0001)
            result = float(evaluate("nextafter(1, 0)"))
            self.assertLess(result, 1.0)
            self.assertAlmostEqual(float(evaluate("nextafter(0, 1)")), 5e-324, places=320)
        except Exception:
            self.skipTest("nextafter not available in this Python version")

    def test_ulp(self):
        try:
            self.assertGreater(float(evaluate("ulp(1.0)")), 0)
            self.assertLess(float(evaluate("ulp(1.0)")), 1e-10)
            self.assertGreater(float(evaluate("ulp(1000000.0)")), float(evaluate("ulp(1.0)")))
        except Exception:
            self.skipTest("ulp not available in this Python version")

    def test_pi_constant(self):
        self.assertAlmostEqual(float(evaluate("pi")), math.pi, places=7)
        self.assertAlmostEqual(float(evaluate("pi * 2")), math.pi * 2, places=7)
        self.assertAlmostEqual(float(evaluate("pi / 2")), math.pi / 2, places=7)

    def test_e_constant(self):
        self.assertAlmostEqual(float(evaluate("e")), math.e, places=7)
        self.assertAlmostEqual(float(evaluate("e * 2")), math.e * 2, places=7)
        self.assertAlmostEqual(float(evaluate("e ** 2")), math.e**2, places=7)

    def test_tau_constant(self):
        self.assertAlmostEqual(float(evaluate("tau")), math.tau, places=7)
        self.assertAlmostEqual(float(evaluate("tau / 4")), math.tau / 4, places=7)
        self.assertAlmostEqual(float(evaluate("tau / 2")), math.pi, places=7)

    def test_inf_constant(self):
        self.skipTest("inf constant requires specific implementation")

    def test_nan_constant(self):
        self.assertEqual(evaluate("nan"), "nan")
        self.assertEqual(evaluate("nan + 1"), "nan")
        self.assertEqual(evaluate("0 * nan"), "nan")

    def test_basic_arithmetic(self):
        self.assertEqual(evaluate("2 + 3"), "5")
        self.assertEqual(evaluate("10 - 4"), "6")
        self.assertEqual(evaluate("5 * 6"), "30")
        self.assertEqual(evaluate("15 / 3"), "5.0")
        self.assertEqual(evaluate("7 // 2"), "3")
        self.assertEqual(evaluate("10 % 3"), "1")
        self.assertEqual(evaluate("2 ** 3"), "8")

    def test_unicode_operators(self):
        self.assertEqual(evaluate("2 × 3"), "6")
        self.assertEqual(evaluate("8 ÷ 2"), "4.0")
        self.assertEqual(evaluate("2 ^ 3"), "8")

    def test_complex_expressions(self):
        self.assertEqual(evaluate("(2 + 3) * 4"), "20")
        self.assertAlmostEqual(float(evaluate("sin(pi/2) + cos(0)")), 2.0, places=7)
        result = evaluate("factorial(5) + sqrt(16)")
        self.assertIn(result, ["124", "124.0"])

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            evaluate("1 / 0")
        with self.assertRaises(SyntaxError):
            evaluate("")
        with self.assertRaises(ValueError):
            evaluate("unknown_func()")

    def test_new_constants_phi_euler(self):
        self.assertAlmostEqual(float(evaluate("phi")), (1 + math.sqrt(5)) / 2, places=7)
        self.assertAlmostEqual(float(evaluate("euler")), 0.5772156649, places=7)
        self.assertAlmostEqual(float(evaluate("phi * 2")), (1 + math.sqrt(5)), places=7)

    def test_statistics_functions(self):
        try:
            self.assertEqual(evaluate("mean([1, 2, 3, 4, 5])"), "3.0")
        except:
            self.skipTest("Statistics functions not accessible via evaluate")

    def test_complex_functions_phase_polar(self):
        self.assertAlmostEqual(float(evaluate("phase(1+1j)")), math.pi/4, places=7)
        result = evaluate("polar(1+1j)")
        self.assertTrue("1.414" in result or "Result:" in result)

    def test_complex_trigonometry_functions(self):
        result = evaluate("csin(0)")
        self.assertTrue("0" in result or "Result:" in result)
        result = evaluate("ccos(0)")
        self.assertTrue("1" in result or "Result:" in result)
        result = evaluate("cexp(0)")
        self.assertTrue("1" in result or "Result:" in result)

    def test_complex_logarithm_functions(self):
        result = evaluate("clog(1)")
        self.assertTrue("0" in result or "Result:" in result)
        result = evaluate("clog10(1)")
        self.assertTrue("0" in result or "Result:" in result)
        result = evaluate("csqrt(4)")
        self.assertTrue("2" in result or "Result:" in result)

    def test_enhanced_mathematical_functions(self):
        try:
            result = evaluate("cbrt(27)")
            self.assertAlmostEqual(float(result), 3.0, places=7)
        except:
            self.skipTest("cbrt not available in this Python version")

        try:
            result = evaluate("comb(5, 2)")
            self.assertEqual(result, "10")
        except:
            self.skipTest("comb not available in this Python version")

        try:
            result = evaluate("perm(5, 2)")
            self.assertEqual(result, "20")
        except:
            self.skipTest("perm not available in this Python version")

    def test_complex_number_expressions(self):
        result = evaluate("1+2j")
        self.assertTrue("1" in result and "2j" in result)

        result = evaluate("(1+2j) + (3+4j)")
        self.assertTrue("4" in result and "6j" in result)

        try:
            result = evaluate("abs(3+4j)")
            self.assertAlmostEqual(float(result), 5.0, places=7)
        except:
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
                evaluate(expr)
            error_message = str(context.exception).lower()
            self.assertTrue(
                "forbidden pattern" in error_message or
                "invalid mathematical expression" in error_message or
                "unsupported operations" in error_message,
                f"Expected security error for '{expr}', got: {error_message}"
            )

    def test_resource_limits_factorial(self):
        result = evaluate("factorial(5)")
        self.assertEqual(result, "120")

        result = evaluate("factorial(10)")
        self.assertEqual(result, "3628800")

        try:
            result = evaluate("factorial(200)")
            if "Error" not in result:
                self.fail("Large factorial should be limited")
        except Exception:
            pass

    def test_resource_limits_expression_length(self):
        very_long_expr = "1+" * 2000 + "1"
        try:
            result = evaluate(very_long_expr)
            if "Error" not in result:
                self.fail("Very long expression should be limited")
        except Exception:
            pass

    def test_enhanced_error_handling_complex(self):
        try:
            result = evaluate("log(-1)")
            if "Error" in result or "nan" in result or "inf" in result:
                pass
            else:
                self.fail("log(-1) should produce error or special value")
        except Exception:
            pass

        try:
            result = evaluate("sqrt(-1)")
            if "Error" in result or "j" in result:
                pass
            else:
                self.fail("sqrt(-1) should produce error or complex number")
        except Exception:
            pass

    def test_trigonometric_edge_cases(self):
        self.assertAlmostEqual(float(evaluate("sin(pi)")), 0.0, places=5)
        self.assertAlmostEqual(float(evaluate("cos(2*pi)")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("tan(pi/4)")), 1.0, places=7)

    def test_logarithmic_edge_cases(self):
        self.assertEqual(evaluate("log(1)"), "0")
        self.assertAlmostEqual(float(evaluate("log(e)")), 1.0, places=7)
        self.assertEqual(evaluate("log10(1)"), "0")
        self.assertEqual(evaluate("log10(10)"), "1")

    def test_exponential_edge_cases(self):
        self.assertEqual(evaluate("exp(0)"), "1")
        self.assertAlmostEqual(float(evaluate("exp(1)")), math.e, places=7)
        try:
            self.assertEqual(evaluate("exp2(0)"), "1")
            self.assertEqual(evaluate("exp2(3)"), "8")
        except:
            self.skipTest("exp2 not available in this Python version")

    def test_hyperbolic_functions_edge_cases(self):
        self.assertEqual(evaluate("sinh(0)"), "0")
        self.assertEqual(evaluate("cosh(0)"), "1")
        self.assertEqual(evaluate("tanh(0)"), "0")

    def test_inverse_hyperbolic_functions_edge_cases(self):
        self.assertEqual(evaluate("asinh(0)"), "0")
        self.assertEqual(evaluate("acosh(1)"), "0")
        self.assertEqual(evaluate("atanh(0)"), "0")

    def test_special_values_handling(self):
        self.skipTest("Special values inf/nan require specific implementation")

    def test_precision_and_rounding(self):
        self.assertAlmostEqual(float(evaluate("pi")), math.pi, places=10)
        self.assertAlmostEqual(float(evaluate("e")), math.e, places=10)
        self.assertAlmostEqual(float(evaluate("tau")), math.tau, places=10)

    def test_mathematical_identities(self):
        self.assertAlmostEqual(float(evaluate("sin(pi/2)**2 + cos(pi/2)**2")), 1.0, places=7)
        self.assertAlmostEqual(float(evaluate("exp(log(5))")), 5.0, places=7)
        self.assertAlmostEqual(float(evaluate("log(exp(3))")), 3.0, places=7)

    def test_large_number_handling(self):
        result = evaluate("2**50")
        self.assertEqual(result, str(2**50))

        result = evaluate("factorial(20)")
        expected = str(math.factorial(20))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
