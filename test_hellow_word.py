import unittest
import hellowword

class TestTDD1(unittest.TestCase):
    def hellowword(self):
        wynik = hellowword.hellow_word()
        self.assertEqual(wynik, 'hellow word')
if __name__ == '__main__':
    unittest.main()
