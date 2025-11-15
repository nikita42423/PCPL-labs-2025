"""
BDD-стиль тестов на чистом Python с использованием unittest
"""

import unittest
import math
from equation_solver.biquadratic import BiquadraticSolver

class TestBiquadraticSolverBDDStyle(unittest.TestCase):
    """
    BDD-стиль тестов: тесты сфокусированы на поведении системы
    """

    def test_should_return_four_roots_when_equation_has_four_real_solutions(self):
        """BDD: Должен вернуть 4 корня когда уравнение имеет 4 действительных решения"""
        # Given (Дано) - биквадратное уравнение с 4 корнями
        a, b, c = 1, -5, 4  # x^4 - 5x^2 + 4 = 0

        # When (Когда) - решаем уравнение
        roots = BiquadraticSolver.solve(a, b, c)

        # Then (Тогда) - должны получить 4 корня: -2, -1, 1, 2
        self.assertEqual(len(roots), 4)
        self.assertEqual(roots, [-2, -1, 1, 2])

    def test_should_return_three_roots_when_equation_has_three_real_solutions(self):
        """BDD: Должен вернуть 3 корня когда уравнение имеет 3 действительных решения"""
        # Given - уравнение x^4 - 3x^2 = 0
        a, b, c = 1, -3, 0

        # When - решаем уравнение
        roots = BiquadraticSolver.solve(a, b, c)

        # Then - должны получить 3 корня: -√3, 0, √3
        expected_roots = [-math.sqrt(3), 0, math.sqrt(3)]
        self.assertEqual(len(roots), 3)
        for i, root in enumerate(roots):
            self.assertAlmostEqual(root, expected_roots[i], places=6)

    def test_should_return_no_roots_when_equation_has_no_real_solutions(self):
        """BDD: Должен вернуть пустой список когда нет действительных решений"""
        # Given - уравнение без действительных корней
        a, b, c = 1, 1, 1  # x^4 + x^2 + 1 = 0

        # When - решаем уравнение
        roots = BiquadraticSolver.solve(a, b, c)

        # Then - должны получить пустой список
        self.assertEqual(roots, [])
        self.assertEqual(len(roots), 0)

    def test_should_raise_error_when_coefficient_a_is_zero(self):
        """BDD: Должен вызвать ошибку когда коэффициент A равен нулю"""
        # Given - уравнение с A = 0
        a, b, c = 0, 1, 1

        # When/Then - при решении должна быть вызвана ошибка
        with self.assertRaises(ValueError) as context:
            BiquadraticSolver.solve(a, b, c)
        self.assertEqual(str(context.exception), "Коэффициент A не может быть равен 0")

    def test_should_validate_correct_coefficients_successfully(self):
        """BDD: Должен успешно валидировать корректные коэффициенты"""
        # Given - корректные коэффициенты
        a, b, c = 1, 2, 3

        # When - валидируем коэффициенты
        result = BiquadraticSolver.validate_coefficients(a, b, c)

        # Then - валидация успешна
        self.assertTrue(result)

    def test_should_reject_invalid_coefficient_a(self):
        """BDD: Должен отвергнуть невалидный коэффициент A"""
        # Given - невалидный коэффициент A
        a, b, c = 0, 2, 3

        # When/Then - при валидации должна быть ошибка
        with self.assertRaises(ValueError) as context:
            BiquadraticSolver.validate_coefficients(a, b, c)
        self.assertIn("Коэффициент A не может быть равен 0", str(context.exception))

class TestBiquadraticScenarios(unittest.TestCase):
    """
    Дополнительные BDD сценарии
    """

    def test_scenario_complex_equation(self):
        """BDD сценарий: Решение сложного биквадратного уравнения"""
        # Scenario: Решение уравнения с комплексными корнями

        # Given: Уравнение x^4 + 2x^2 + 1 = 0
        a, b, c = 1, 2, 1

        # When: Пользователь решает уравнение
        roots = BiquadraticSolver.solve(a, b, c)

        # Then: Получает один корень (x = 0 не является корнем!)
        # Уравнение: (x^2 + 1)^2 = 0 → x^2 = -1 → нет действительных корней
        self.assertEqual(len(roots), 0)

    def test_scenario_simple_square(self):
        """BDD сценарий: Решение простого уравнения вида x^4 = k"""
        # Scenario: Решение уравнения x^4 = 16

        # Given: Уравнение x^4 - 16 = 0
        a, b, c = 1, 0, -16

        # When: Пользователь решает уравнение
        roots = BiquadraticSolver.solve(a, b, c)

        # Then: Получает корни ±2
        self.assertEqual(len(roots), 2)
        self.assertEqual(roots, [-2, 2])

if __name__ == '__main__':
    unittest.main()
