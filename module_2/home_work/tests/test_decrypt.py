from unittest import TestCase

from decrypt import decrypt


class TestDecrypt(TestCase):

    def test_decrypt(self):
        self.assertEqual('абра-кадабра', decrypt('абра-кадабра.'))
        self.assertEqual('абра-кадабра', decrypt('абраа..-кадабра'))
        self.assertEqual('абра-кадабра', decrypt('абраа..-.кадабра'))
        self.assertEqual('абра-кадабра', decrypt('абра--..кадабра'))
        self.assertEqual('абра-кадабра', decrypt('абрау...-кадабра'))
        self.assertEqual('', decrypt('абра........'))
        self.assertEqual('a', decrypt('абр......a.'))
        self.assertEqual('23', decrypt('1..2.3'))
        self.assertEqual('', decrypt('.'))
        self.assertEqual('', decrypt('1.......................'))
