# используется для сортировки
from operator import itemgetter

class Table:
    """Таблица данных"""
    def __init__(self, id, name, row_count, db_id):
        self.id = id
        self.name = name
        self.row_count = row_count  # количественный признак
        self.db_id = db_id

class Database:
    """База данных"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TableDatabase:
    """Связь многие-ко-многим между таблицами и базами данных"""
    def __init__(self, db_id, table_id):
        self.db_id = db_id
        self.table_id = table_id

# Базы данных
dbs = [
    Database(1, 'Активная база'),
    Database(2, 'Архивная база данных'),
    Database(3, 'Тестовая'),
    Database(4, 'Аналитическая база данных'),
    Database(5, 'Основная база'),
]

# Таблицы
tables = [
    Table(1, 'Пользователей', 1000, 1),
    Table(2, 'Заказов', 5000, 2),
    Table(3, 'Товаров', 800, 2),
    Table(4, 'Аналитика продаж', 300, 4),
    Table(5, 'Логов', 1200, 5),
]

# Связи многие-ко-многим
tables_dbs = [
    TableDatabase(1, 1),
    TableDatabase(2, 2),
    TableDatabase(2, 3),
    TableDatabase(4, 4),
    TableDatabase(5, 5),
    TableDatabase(1, 2),
    TableDatabase(2, 1),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(t.name, t.row_count, d.name)
                   for d in dbs
                   for t in tables
                   if t.db_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, td.db_id, td.table_id)
                         for d in dbs
                         for td in tables_dbs
                         if d.id == td.db_id]

    many_to_many = [(t.name, t.row_count, db_name)
                    for db_name, db_id, table_id in many_to_many_temp
                    for t in tables if t.id == table_id]

    print('Задание Д1')
    # Список всех таблиц, у которых название заканчивается на "ов", и названия их БД
    res_1 = list(filter(lambda i: i[0].endswith('ов'), one_to_many))
    print(res_1)

    print('\nЗадание Д2')
    # Список БД со средней числом строк в таблицах в каждой БД, отсортированный по средней
    res_2_unsorted = []
    for d in dbs:
        # Список таблиц БД
        d_tables = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_tables) > 0:
            # Количество строк таблиц БД
            d_rows = [row_count for _, row_count, _ in d_tables]
            # Среднее число строк (с округлением до 2 знаков)
            d_rows_avg = round(sum(d_rows) / len(d_rows), 2)
            res_2_unsorted.append((d.name, d_rows_avg))
    # Сортировка по средней числу строк
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(res_2)

    print('\nЗадание Д3')
    # Список всех БД, у которых название начинается с буквы "А", и список их таблиц
    res_3 = {}
    for d in dbs:
        if d.name.startswith('А'):
            # Список таблиц БД
            d_tables = list(filter(lambda i: i[2] == d.name, many_to_many))
            # Только названия таблиц
            d_tables_names = [name for name, _, _ in d_tables]
            res_3[d.name] = d_tables_names
    print(res_3)

if __name__ == '__main__':
    main()
