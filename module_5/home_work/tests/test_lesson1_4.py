import sys
from io import StringIO
import unittest
from traceback import format_exc
from Modules_Adv.module_5.home_work.lesson1_4 import Redirect


class TestRedirect(unittest.TestCase):
    def setUp(self):
        self.stdout = StringIO()
        self.stderr = StringIO()
        self.redirect = Redirect(stdout=self.stdout, stderr=self.stderr)
        self.redirect.__enter__()

    def tearDown(self):
        self.redirect.__exit__(None, None, None)

    def test_stdout_redirect(self):
        print('Test stdout')
        self.assertEqual(self.stdout.getvalue().strip(), 'Test stdout')

    def test_stderr_redirect(self):
        sys.stderr.write('Test stderr')
        self.assertEqual(self.stderr.getvalue().strip(), 'Test stderr')

    def test_exception_redirect(self):
        try:
            1 / 0
        except ZeroDivisionError:
            pass
        self.assertTrue('ZeroDivisionError' in self.stderr.getvalue())


# if __name__ == '__main__':
#     with open('test_results.txt', 'a') as test_file_stream:
#         runner = unittest.TextTestRunner(stream=test_file_stream)
#         unittest.main(testRunner=runner)
