import mojprogram
import unittest

class Test(unitest.TestCase):

    def test_upper(self):
        self.assertEqual(mojprogram.doUpper('sdajh'))

    def test_upper(self):
        pass

    def test_replace(self):
        str = mojprogram.do_replace('co','na co')
        self.assertTrue(str.index('na co') > 0)
if __name__ == '__main__':
    unittest.main()
