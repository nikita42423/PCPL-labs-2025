class Unique(object):
    def __init__(self, items, **kwargs):
        # Получаем значение ignore_case из kwargs, по умолчанию False
        self.ignore_case = kwargs.get('ignore_case', False)

        # Сохраняем итератор исходных данных
        self.iterator = iter(items)

        # Множество для отслеживания уже встреченных элементов
        self.seen = set()

        # Указатель на следующий элемент
        self.next_item = None

        # Загружаем первый элемент
        self._get_next()

    def _normalize_item(self, item):
        """Нормализует элемент для сравнения с учетом ignore_case"""
        if self.ignore_case and isinstance(item, str):
            return item.lower()
        return item

    def _get_next(self):
        """Находит следующий уникальный элемент"""
        while True:
            try:
                item = next(self.iterator)
                normalized = self._normalize_item(item)

                if normalized not in self.seen:
                    self.seen.add(normalized)
                    self.next_item = item
                    return
            except StopIteration:
                self.next_item = None
                return

    def __next__(self):
        if self.next_item is None:
            raise StopIteration

        result = self.next_item
        self._get_next()
        return result

    def __iter__(self):
        return self


# Тестовые примеры
print("Тест 1 - числа с дубликатами:")
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
for item in Unique(data1):
    print(item, end=" ")
print()

print("\nТест 2 - с генератором gen_random:")
def simple_gen():
    for i in [1, 2, 2, 3, 3, 3, 1, 4, 4]:
        yield i

for item in Unique(simple_gen()):
    print(item, end=" ")
print()

print("\nТест 3 - строки без ignore_case (по умолчанию):")
data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for item in Unique(data3):
    print(item, end=" ")
print()

print("\nТест 4 - строки с ignore_case=True:")
for item in Unique(data3, ignore_case=True):
    print(item, end=" ")
print()

print("\nТест 5 - смешанные данные:")
data5 = [1, '1', 1, '1', 'a', 'A', 2.5, 2.5]
for item in Unique(data5):
    print(item, end=" ")
print()
