import unittest

from social_age import get_social_status


class TestSocialAge(unittest.TestCase):

    def test_can_get_child_age(self):
        self.assertEqual('Ребёнок', get_social_status(8))

    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_cannot_pass_negative_age(self):
        with self.assertRaises(ValueError):
            get_social_status(-1)

    def test_can_get_others_ages(self):
        self.assertEqual('Подросток', get_social_status(15))
        self.assertEqual('Взрослый', get_social_status(25))
        self.assertEqual('Пожилой', get_social_status(55))
        self.assertEqual('Пенсионер', get_social_status(65))
