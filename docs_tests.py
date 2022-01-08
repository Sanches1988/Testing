from documents import get_name_people, get_shelf_number
import unittest

class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        print(f'Начало проверки функции')

    def test_get_name_people(self):
        self.assertEqual(get_name_people('Геннадий Покемонов'), True)
        print('Проверка функции get_name_people')

    def test_get_shelf_number(self):
        self.assertEqual(get_shelf_number('10006'), '2')
        print('Проверка функции get_shelf_number')

    def tearDown(self):
        print(f'Конец проверки функции', end="\n\n")


if __name__ == '__main__':
    unittest.main()