import math

class BiquadraticSolver:
    """
    Класс для решения биквадратного уравнения Ax^4 + Bx^2 + C = 0
    """

    @staticmethod
    def solve(a, b, c):
        """
        Решение биквадратного уравнения

        Args:
            a (float): коэффициент A
            b (float): коэффициент B
            c (float): коэффициент C

        Returns:
            list: список действительных корней (может быть пустым)

        Raises:
            ValueError: если коэффициент A равен 0
        """
        # Валидируем коэффициенты перед решением
        BiquadraticSolver.validate_coefficients(a, b, c)

        # Решаем как квадратное относительно t = x^2
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []

        roots = []

        # Первый корень квадратного уравнения
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        if t1 >= 0:
            x1 = math.sqrt(t1)
            x2 = -math.sqrt(t1)
            roots.extend([x1, x2])

        # Второй корень квадратного уравнения
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        if t2 >= 0 and abs(t2 - t1) > 1e-10:
            x3 = math.sqrt(t2)
            x4 = -math.sqrt(t2)
            roots.extend([x3, x4])

        # Убираем дубликаты и сортируем
        unique_roots = []
        for root in sorted(roots):
            if not unique_roots or abs(root - unique_roots[-1]) > 1e-10:
                unique_roots.append(root)

        return unique_roots

    @staticmethod
    def validate_coefficients(a, b, c):
        """
        Валидация коэффициентов уравнения

        Args:
            a, b, c: коэффициенты

        Returns:
            bool: True если коэффициенты валидны

        Raises:
            ValueError: если коэффициенты невалидны
        """
        if not isinstance(a, (int, float)):
            raise ValueError("Коэффициент A должен быть числом")
        if not isinstance(b, (int, float)):
            raise ValueError("Коэффициент B должен быть числом")
        if not isinstance(c, (int, float)):
            raise ValueError("Коэффициент C должен быть числом")
        if abs(a) < 1e-10:
            raise ValueError("Коэффициент A не может быть равен 0")
        return True
