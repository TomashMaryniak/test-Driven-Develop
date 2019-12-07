# import unittest
#import mojprogram_String

#class Test(unitest.TestCase):
#    def test_upper(self):
#        self.assertEqual(mojprogram_String.doUpper('sdajh'))
#        pass

#    def test_replace(self):
#        str = mojprogram.do_replace('co','na co')
#        self.assertTrue(str.index('na co') > 0)

# if __name__ == '__main__':
#    unittest.main()
import unittest
import mojprogram_String

class TestTDD2(unittest.TestCase):
    def mojprogram_String(self):
        wynik = mojprogram_String.capitalize()
        self.assertEqual(wynik, 4)

    def kalkulator_klasa_odejmowanie(self):
        wynik = kalkulator_klasa.odejmowanie(5,2)
        self.assertEqual(wynik,3)

if __name__ == '__main__':
    unittest.main()
