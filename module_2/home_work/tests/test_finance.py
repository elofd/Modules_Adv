from unittest import TestCase

from Modules_Adv.module_2.home_work.app_2 import app, storage


class TestFinance(TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        storage[2023] = {1: 50, 4: 150, 3: 250}

    def test_add_work_date(self):
        url = '/add/20230202/500'
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue('500' in response_text)
        self.assertTrue('2023' in response_text)
        self.assertTrue('02' in response_text)
        self.assertTrue(response.status_code, 200)

    def test_add_wrong_date(self):
        url = '/add/afaf/400'
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue('Дата введена некорректно' in response_text)
        self.assertTrue(response.status_code, 404)

    def test_add_wrong_expence(self):
        url = '/add/20230420/afaf'
        response = self.app.get(url)
        self.assertTrue(response.status_code, 404)

    def test_calculate_year_work_year(self):
        url = 'calculate/2023'
        response = self.app.get(url)
        response_text = response.data.decode()
        self.assertTrue(response.status_code, 200)
        self.assertTrue('450' in response_text)

    def test_calculate_year_wrong_type_of_year(self):
        response = self.app.get('calculate/afa')
        self.assertTrue(response.status_code, 404)

    def test_calculate_year_wrong_year(self):
        response = self.app.get('calculate/2019')
        self.assertTrue(response.status_code, 404)
        self.assertTrue('Суммарные траты' in response.data.decode())

    def test_calculate_month_work_month(self):
        response = self.app.get('calculate/2023/4')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('150' in response.data.decode())

    def test_calculate_month_wrong_type_of_month_or_year(self):
        response = self.app.get('calculate/2023/af')
        self.assertTrue(response.status_code, 404)

    def test_calculate_month_wrong_month(self):
        response = self.app.get('calculate/2023/7')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('Суммарные траты' in response.data.decode())
