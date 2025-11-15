import unittest
from unittest.mock import patch, MagicMock
import math
from equation_solver.biquadratic import BiquadraticSolver

class TestBiquadraticSolverMocksSimple(unittest.TestCase):
    """
    Тесты с Mock-объектами
    """

    @patch('equation_solver.biquadratic.math.sqrt')
    def test_mock_prevents_actual_sqrt_calculation(self, mock_sqrt):
        """Mock: Проверяем что mock предотвращает реальные вычисления sqrt"""
        # Настраиваем mock чтобы он всегда возвращал 1
        mock_sqrt.return_value = 1.0

        # При таких настройках уравнение будет иметь предсказуемые корни
        roots = BiquadraticSolver.solve(1, 0, 0)

        # Проверяем что mock был вызван
        self.assertTrue(mock_sqrt.called)

        # При sqrt=1 корни будут ±1
        expected_roots = [-1, 1]
        self.assertEqual(len(roots), 2)
        for i, root in enumerate(roots):
            self.assertAlmostEqual(root, expected_roots[i], places=6)

    @patch('equation_solver.biquadratic.BiquadraticSolver.validate_coefficients')
    def test_validate_called_in_solve(self, mock_validate):
        """Mock: Проверяем что solve вызывает validate_coefficients"""
        mock_validate.return_value = True

        roots = BiquadraticSolver.solve(2, 0, -8)  # 2x^4 - 8 = 0

        mock_validate.assert_called_once_with(2, 0, -8)
        # Корни: x^4 = 4 → x = ±√2
        expected_roots = [-math.sqrt(2), math.sqrt(2)]
        self.assertEqual(len(roots), 2)

    def test_mock_validation_failure(self):
        """Mock: Тест провала валидации с mock-объектом"""
        # Создаем mock который не проходит проверку isinstance
        mock_invalid = MagicMock()

        with self.assertRaises(ValueError):
            BiquadraticSolver.validate_coefficients(mock_invalid, 1, 1)

    @patch('equation_solver.biquadratic.BiquadraticSolver.validate_coefficients')
    @patch('equation_solver.biquadratic.math.sqrt')
    def test_multiple_mocks_together(self, mock_sqrt, mock_validate):
        """Mock: Тест с несколькими mock-объектами одновременно"""
        # Настраиваем оба mock-объекта
        mock_validate.return_value = True
        mock_sqrt.return_value = 2.0  # Все sqrt возвращают 2

        roots = BiquadraticSolver.solve(1, 0, 0)

        # Проверяем оба mock-объекта
        mock_validate.assert_called_once_with(1, 0, 0)
        self.assertTrue(mock_sqrt.called)

        # При sqrt=2 корни будут ±2
        self.assertEqual(roots, [-2, 2])

if __name__ == '__main__':
    unittest.main()
