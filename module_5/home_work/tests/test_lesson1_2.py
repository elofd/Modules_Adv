from unittest import TestCase

from Modules_Adv.module_5.home_work.lesson1_2 import app, RemoteUploadForm, remote_upload


class TestLesson1(TestCase):

    def setUp(self) -> None:
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def test_invalid_input(self):
        command = '"print(\'Hello, world!\')"'
        timeout = -1

        response = self.app.post('/remote_upload', data={'command': command, 'timeout': timeout})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input', response.text)

    def test_unsafe_input(self):
        command = '"from subprocess import run; run([\'./kill_the_system.sh\'])"'
        timeout = 5

        response = self.app.post('/remote_upload', data={'command': command, 'timeout': timeout})
        self.assertEqual(response.status_code, 400)
        self.assertIn('BlockingIOError', response.text)

    def test_timeout(self):
        command = '"import time; print(); time.sleep(10); print();"'
        timeout = 5

        response = self.app.post('/remote_upload', data={'command': command, 'timeout': timeout})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, 'Execution timed out')
