from unittest import TestCase

from Modules_Adv.module_5.home_work.lesson1_3 import BlockErrors


class TestLesson3(TestCase):

    def test_ignore_error(self):
        errors = {ZeroDivisionError}
        result = None
        with BlockErrors(errors):
            result = 1 / 0
        self.assertIsNone(result)

    def test_raise_error(self):
        errors = {TypeError}
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors(errors):
                result = 1 / 0

    def test_ignore_inner_error(self):
        errors_inner = {TypeError}
        errors_outer = {ZeroDivisionError}
        result = None
        with BlockErrors(errors_outer):
            with BlockErrors(errors_inner):
                result = 1 / 'a'
        self.assertIsNone(result)

    def test_ignore_child_errors(self):
        errors = {Exception}
        result = None
        with BlockErrors(errors):
            try:
                result = 1 / 'a'
            except TypeError:
                self.fail("TypeError should have been ignored")
        self.assertIsNone(result)
