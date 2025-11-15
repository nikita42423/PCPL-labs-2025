import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


# Тестовые примеры
print("Тест 1 - 5 чисел от 1 до 3:")
for num in gen_random(5, 1, 3):
    print(num, end=" ")
print()

print("\nТест 2 - 10 чисел от 0 до 10:")
for num in gen_random(10, 0, 10):
    print(num, end=" ")
print()

print("\nТест 3 - 3 числа от -5 до 5:")
for num in gen_random(3, -5, 5):
    print(num, end=" ")
print()

print("\nТест 4 - в виде списка (8 чисел от 1 до 100):")
result = list(gen_random(8, 1, 100))
print(result)
