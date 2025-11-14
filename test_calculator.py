import unittest
from calculator import *
#https://github.com/nicaniemi/lab11-NN.git
class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(3,3), 6)
        self.assertEqual(add(5, 5), 10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,3), 2)
        self.assertEqual(sub(10,4), 6)
        self.assertEqual(sub(100,1), 99)
    ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,4), 2)
        self.assertEqual(div(1, 5), 5)
        self.assertEqual(div(1, 10), 10)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 3), 8)
        self.assertEqual(log(3, 4), 81)
        self.assertEqual(log(2,2), 4)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(5,0)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(1, 1), 1)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(square_root(ValueError)):
            square_root(-1)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(100), 10)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()