from YAapi import YandexDiskAPI
import unittest

class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        print('Начало проверки функции')

    def test_create_folder_pytest(self):
        yandex = YandexDiskAPI('')
        self.assertEqual(yandex.create_folder('pytest'), 201)

    def tearDown(self):
        print('Конец проверки функции', end="\n\n")


if __name__ == '__main__':
    unittest.main()