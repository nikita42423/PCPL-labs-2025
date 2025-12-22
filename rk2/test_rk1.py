# test_rk1.py
import unittest
from rk1_refactored import *

class TestRK1(unittest.TestCase):
    def setUp(self):
        self.dbs = [
            Database(1, 'Активная база'),
            Database(2, 'Архивная база данных'),
            Database(3, 'Тестовая'),
        ]

        self.tables = [
            Table(1, 'Пользователей', 1000, 1),
            Table(2, 'Заказов', 5000, 2),
            Table(3, 'Товары', 800, 2),
        ]

        self.tables_dbs = [
            TableDatabase(1, 1),
            TableDatabase(2, 2),
            TableDatabase(2, 3),
        ]

        self.one_to_many = get_one_to_many(self.dbs, self.tables)
        self.many_to_many = get_many_to_many(self.dbs, self.tables, self.tables_dbs)

    def test_task1(self):
        result = task1(self.one_to_many)
        self.assertEqual(len(result), 1)
        self.assertTrue(all(i[0].endswith('ов') for i in result))

    def test_task2(self):
        result = task2(self.dbs, self.one_to_many)
        self.assertEqual(len(result), 2)  # 2 БД имеют таблицы
        self.assertLessEqual(result[0][1], result[1][1])  # отсортированы

    def test_task3(self):
        result = task3(self.dbs, self.many_to_many)
        self.assertEqual(len(result), 2)  # 2 БД начинаются на 'А'
        self.assertIn('Активная база', result)
        self.assertIn('Архивная база данных', result)

if __name__ == '__main__':
    unittest.main()
