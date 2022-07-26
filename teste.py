import unittest
from urllib import response
from controller.app import product

class TestProduct(unittest.TestCase):
    def testResponse(self):
        #se o response == 200 pass
        if self.assertEqual(product.response.status_code, 200):
            print("pass")
        else:
            print("fail")


if __name__ == '__main__':
    unittest.main()