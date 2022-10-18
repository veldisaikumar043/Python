import unittest
from creditCardValidation import*
class creditCardvalidatonTest(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def test_validateCard_valid(self):
        result = validateCard(date(2022, 12, 12))
        self.assertEqual('valid', result)

    def test_validateCard_expired(self):
        result=validateCard(date(2021,12,12))
        self.assertEqual('expired',result)

    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()
