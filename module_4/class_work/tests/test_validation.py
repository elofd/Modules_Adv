from unittest import TestCase

from Modules_Adv.module_4.class_work.lesson4_1 import app, RegistrationForm, number_length, ValidationError


class FormValidationTest(TestCase):

    def setUp(self) -> None:
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.data = {
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'John Doe',
            'address': '123 Main St',
            'index': 12345
        }

    def test_email_valid(self):
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_email_invalid(self):
        self.data['email'] = 'afafaf'
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_phone_valid(self):
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_phone_invalid(self):
        self.data['phone'] = 12345678901222
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_name_valid(self):
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_address_valid(self):
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_index_valid(self):
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 200)

