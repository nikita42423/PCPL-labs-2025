# rk1_refactored.py
from operator import itemgetter

class Table:
    def __init__(self, id, name, row_count, db_id):
        self.id = id
        self.name = name
        self.row_count = row_count
        self.db_id = db_id

class Database:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TableDatabase:
    def __init__(self, db_id, table_id):
        self.db_id = db_id
        self.table_id = table_id

def get_one_to_many(dbs, tables):
    return [(t.name, t.row_count, d.name)
            for d in dbs for t in tables if t.db_id == d.id]

def get_many_to_many(dbs, tables, tables_dbs):
    temp = [(d.name, td.db_id, td.table_id)
            for d in dbs for td in tables_dbs if d.id == td.db_id]
    return [(t.name, t.row_count, db_name)
            for db_name, db_id, table_id in temp
            for t in tables if t.id == table_id]

def task1(one_to_many):
    return list(filter(lambda i: i[0].endswith('ов'), one_to_many))

def task2(dbs, one_to_many):
    res = []
    for d in dbs:
        d_tables = list(filter(lambda i: i[2] == d.name, one_to_many))
        if d_tables:
            avg = round(sum(r for _, r, _ in d_tables) / len(d_tables), 2)
            res.append((d.name, avg))
    return sorted(res, key=itemgetter(1))

def task3(dbs, many_to_many):
    res = {}
    for d in dbs:
        if d.name.startswith('А'):
            tables = [name for name, _, db in many_to_many if db == d.name]
            res[d.name] = tables
    return res

def main():
    dbs = [
        Database(1, 'Активная база'),
        Database(2, 'Архивная база данных'),
        Database(3, 'Тестовая'),
        Database(4, 'Аналитическая база данных'),
        Database(5, 'Основная база'),
    ]

    tables = [
        Table(1, 'Пользователей', 1000, 1),
        Table(2, 'Заказов', 5000, 2),
        Table(3, 'Товаров', 800, 2),
        Table(4, 'Аналитика продаж', 300, 4),
        Table(5, 'Логов', 1200, 5),
    ]

    tables_dbs = [
        TableDatabase(1, 1),
        TableDatabase(2, 2),
        TableDatabase(2, 3),
        TableDatabase(4, 4),
        TableDatabase(5, 5),
        TableDatabase(1, 2),
        TableDatabase(2, 1),
    ]

    one_to_many = get_one_to_many(dbs, tables)
    many_to_many = get_many_to_many(dbs, tables, tables_dbs)

    print('Задание Д1:', task1(one_to_many))
    print('Задание Д2:', task2(dbs, one_to_many))
    print('Задание Д3:', task3(dbs, many_to_many))

if __name__ == '__main__':
    main()
