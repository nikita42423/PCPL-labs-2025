def field(items, *args):
    assert len(args) > 0

    # Если передан только один аргумент (поле)
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]

    # Если передано несколько аргументов (полей)
    else:
        for item in items:
            # Создаем временный словарь для результата
            result_dict = {}

            # Добавляем только те поля, которые есть в словаре и не равны None
            for key in args:
                if key in item and item[key] is not None:
                    result_dict[key] = item[key]

            # Если в результате есть хотя бы одно поле (не пустой словарь)
            if result_dict:
                yield result_dict


# Тестовые данные
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': None, 'price': 1500},
    {'color': 'blue'},
    {'title': 'Стул', 'price': None, 'color': 'red'},
    {'description': 'test'}
]

print("Тест 1 - одно поле 'title':")
for value in field(goods, 'title'):
    print(value)

print("\nТест 2 - два поля 'title', 'price':")
for value in field(goods, 'title', 'price'):
    print(value)

print("\nТест 3 - поле, которого нет в некоторых словарях:")
for value in field(goods, 'color'):
    print(value)

print("\nТест 4 - несколько полей с None значениями:")
for value in field(goods, 'title', 'price', 'color'):
    print(value)
