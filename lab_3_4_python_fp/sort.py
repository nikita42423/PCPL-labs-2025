data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # Способ 1: Без lambda-функции (используя key и reverse)
    result = sorted(data, key=abs, reverse=True)
    print("Без lambda:", result)

    # Способ 2: С использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("С lambda:  ", result_with_lambda)
