import unittest
import kalkulator_klasa

class TestTDD1(unittest.TestCase):
    def test_calculator_dodawanie(self):
        wynik = kalkulator_klasa.dodawanie(2, 2)
        self.assertEqual(wynik, 4)

    def test_calculator_odejmowanie(self):
        wynik = kalkulator_klasa.odejmowanie(5, 2)
        self.assertEqual(wynik, 3)

    def test_calculator_mnozenie(self):
        wynik = kalkulator_klasa.mnozenie(5, 5)
        self.assertEqual(wynik, 25)

    def test_calculator_dzielenie(self):
        wynik = kalkulator_klasa.dzielenie(8, 2)
        self.assertEqual(wynik, 4)

if __name__ == '__main__':
    unittest.main()
