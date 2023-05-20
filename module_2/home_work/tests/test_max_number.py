import unittest
import os
from datetime import datetime

from freezegun import freeze_time

from Modules_Adv.module_2.home_work.app import app


class TestMaxNumberApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.url = '/max_number/'

        self.filename = 'test.txt'
        with open(self.filename, 'w') as f:
            f.write('test file\nline 2\nline 3\nline 4\nline 5\n')

    def tearDown(self):
        os.remove(self.filename)

    def test_can_get_correct_max_number(self):
        numbers = 1, 2
        url = self.url + '/'.join(map(str, numbers))
        response = self.app.get(url)
        response_text = response.data.decode()
        correct_answer_str = f'<i>{max(numbers)}</i>'
        self.assertTrue(correct_answer_str in response_text)

    def test_cannot_get_str_in_numbers(self):
        numbers = 1, 'qwe', 3
        url = self.url + '/'.join(map(str, numbers))
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue(response_text in 'Ошибка, можно передавать только числа')


class TestHelloWorldApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.url = '/hello_world/'

    def test_can_get_correct_username(self):
        username = 'username'
        response = self.app.get(self.url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_cannot_get_path_as_username(self):
        username = 'qwe/asd/zxc'
        response = self.app.get(self.url + username)
        status = response.status_code
        self.assertTrue(status == 404)

    @freeze_time('2023-01-14')
    def test_can_get_correct_username_with_weekdate(self):
        username = 'username'
        weekdays_tuple = ('Понедельника', 'Вторника', 'Среды',
                          'Четверга', 'Пятницы', 'Субботы', 'Воскресенья')
        today = datetime.today().weekday()
        response = self.app.get(self.url + username)
        response_text = response.data.decode()
        self.assertTrue(weekdays_tuple[today] in response_text)

