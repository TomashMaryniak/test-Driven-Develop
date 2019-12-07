import unittest
import kalkulator_klasa

class TestTDD1(unittest.TestCase):
    def kalkulator_klasa_dodawanie(self):
        wynik = kalkulator_klasa.dodawanie(2,2)
        self.assertEqual(wynik, 4)

    def kalkulator_klasa_odejmowanie(self):
        wynik = kalkulator_klasa.odejmowanie(5,2)
        self.assertEqual(wynik,3)

if __name__ == '__main__':
    unittest.main()
