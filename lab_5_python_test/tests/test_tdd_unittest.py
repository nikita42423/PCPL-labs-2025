import unittest
import math
from equation_solver.biquadratic import BiquadraticSolver

class TestBiquadraticSolverTDD(unittest.TestCase):
    """
    TDD тесты для решения биквадратного уравнения с использованием unittest
    """

    def test_four_real_roots(self):
        """TDD: Уравнение с четырьмя действительными корнями"""
        # Уравнение: x^4 - 5x^2 + 4 = 0
        # Корни: x = ±1, x = ±2
        roots = BiquadraticSolver.solve(1, -5, 4)
        expected_roots = [-2, -1, 1, 2]

        self.assertEqual(len(roots), 4)
        for i, root in enumerate(roots):
            self.assertAlmostEqual(root, expected_roots[i], places=6)

    def test_two_real_roots(self):
        """TDD: Уравнение с двумя действительными корнями"""
        # Уравнение: x^4 - 3x^2 = 0 -> x^2(x^2 - 3) = 0
        roots = BiquadraticSolver.solve(1, -3, 0)
        expected_roots = [-math.sqrt(3), 0, math.sqrt(3)]

        self.assertEqual(len(roots), 3)
        for i, root in enumerate(roots):
            self.assertAlmostEqual(root, expected_roots[i], places=6)

    def test_no_real_roots(self):
        """TDD: Уравнение без действительных корней"""
        # Уравнение: x^4 + x^2 + 1 = 0
        roots = BiquadraticSolver.solve(1, 1, 1)
        self.assertEqual(len(roots), 0)

    def test_zero_coefficient_a(self):
        """TDD: Исключение при нулевом коэффициенте A"""
        with self.assertRaises(ValueError) as context:
            BiquadraticSolver.solve(0, 1, 1)
        self.assertEqual(str(context.exception), "Коэффициент A не может быть равен 0")

    def test_validate_coefficients(self):
        """TDD: Валидация коэффициентов"""
        self.assertTrue(BiquadraticSolver.validate_coefficients(1, 2, 3))

        with self.assertRaises(ValueError):
            BiquadraticSolver.validate_coefficients(0, 2, 3)

    def test_single_real_root(self):
        """TDD: Уравнение с одним действительным корнем"""
        # Уравнение: x^4 = 0
        roots = BiquadraticSolver.solve(1, 0, 0)
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 0, places=6)

if __name__ == '__main__':
    unittest.main()
