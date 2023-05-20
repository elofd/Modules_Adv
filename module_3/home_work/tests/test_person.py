from unittest import TestCase

from Modules_Adv.module_3.home_work.person import Person


class TestPerson(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Person('name', 2020)

    def test_get_age(self):
        self.assertEqual(3, self.obj.get_age())

    def test_set_name(self):
        self.assertEqual(None, self.obj.set_name('Vasua'))
        self.assertEqual('Vasua', self.obj.get_name())

    def test_get_name(self):
        self.assertEqual('name', self.obj.get_name())

    def test_set_address(self):
        self.assertEqual(None, self.obj.set_address('Lenina 8'))
        self.assertEqual('Lenina 8', self.obj.get_address())

    def test_get_address(self):
        self.assertEqual('', self.obj.get_address())

    def test_is_homeless(self):
        self.assertEqual(False, self.obj.is_homeless())
