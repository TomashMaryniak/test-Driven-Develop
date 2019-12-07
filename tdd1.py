import unittest
import mojpragram

class TestTDD1(unittest.TestCase):
    def test_zwroc_100(self):
        wynik = mojpragram.zwroc_100()
        self.assertEqual(wynik, 100)

if __name__ == '__main__':
    unittest.main()
