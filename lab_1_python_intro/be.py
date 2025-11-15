import sys
import math

def get_input_value(prompt):
    """Получение корректного числового значения от пользователя"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")

def solve_biquadratic():
    """Решение биквадратного уравнения"""
    print("Решение биквадратного уравнения Ax^4 + Bx^2 + C = 0")

    # Обработка аргументов командной строки
    coefficients = [None, None, None]  # Инициализируем список из 3 элементов

    for i, arg in enumerate(sys.argv[1:4]):  # Берем только первые 3 аргумента
        try:
            coefficients[i] = float(arg)
        except (ValueError, IndexError):
            coefficients[i] = None
            print(f"Некорректный коэффициент в командной строке: {arg}")

    # Заполнение недостающих коэффициентов
    coefficient_names = ['A', 'B', 'C']
    for i in range(3):
        if coefficients[i] is None:
            coefficients[i] = get_input_value(f"Введите коэффициент {coefficient_names[i]}: ")

    a, b, c = coefficients

    # Проверка, что уравнение биквадратное
    if a == 0:
        print("Ошибка: коэффициент A не может быть равен 0")
        return

    print(f"\nУравнение: {a}x^4 + {b}x^2 + {c} = 0")

    # Решение через замену t = x^2
    D = b * b - 4 * a * c
    print(f"Дискриминант: {D}")

    if D < 0:
        print("Действительных корней нет")
        return

    roots = []

    # Первая пара корней
    t1 = (-b + math.sqrt(D)) / (2 * a)
    if t1 >= 0:
        x1 = math.sqrt(t1)
        x2 = -math.sqrt(t1)
        roots.extend([x1, x2])
        if abs(x1) < 1e-10:  # Проверка на ноль
            print("x1 = 0")
        else:
            print(f"x1 = {x1:.6f}, x2 = {x2:.6f}")

    # Вторая пара корней (если корни разные)
    t2 = (-b - math.sqrt(D)) / (2 * a)
    if t2 >= 0 and abs(t2 - t1) > 1e-10:
        x3 = math.sqrt(t2)
        x4 = -math.sqrt(t2)
        roots.extend([x3, x4])
        if abs(x3) < 1e-10:  # Проверка на ноль
            print("x3 = 0")
        else:
            print(f"x3 = {x3:.6f}, x4 = {x4:.6f}")

    # Вывод всех корней
    if roots:
        # Убираем дубликаты и сортируем
        unique_roots = []
        for root in sorted(roots):
            if not unique_roots or abs(root - unique_roots[-1]) > 1e-10:
                unique_roots.append(root)

        roots_str = ", ".join(f"{x:.6f}" for x in unique_roots)
        print(f"\nВсе действительные корни: {roots_str}")
    else:
        print("\nДействительных корней нет")

def main():
    """Главная функция"""
    solve_biquadratic()

if __name__ == "__main__":
    main()
