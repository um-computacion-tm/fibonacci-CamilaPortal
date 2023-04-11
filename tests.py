import unittest
from fibonacci import fibonacci
from fibonacci import fibonacci_1

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        result= fibonacci(1)
        self.assertEqual(result, 1)

    def test_2(self):
        result= fibonacci(2)
        self.assertEqual(result, 1)

    def test_3(self):
        result= fibonacci(3)
        self.assertEqual(result, 2)

    def test_4(self):
        result= fibonacci(4)
        self.assertEqual(result, 3)

    def test_5(self):
        result= fibonacci(5)
        self.assertEqual(result, 5)

    def test_6(self):
        result= fibonacci(6)
        self.assertEqual(result, 8)

    
class TestFibonacciRecursive(unittest.TestCase):
    def test_1(self):
        result= fibonacci_1(1)
        self.assertEqual(result, 1)

    def test_2(self):
        result= fibonacci_1(2)
        self.assertEqual(result, 1)

    def test_3(self):
        result= fibonacci_1(3)
        self.assertEqual(result, 2)

    def test_4(self):
        result= fibonacci_1(4)
        self.assertEqual(result, 3)

    def test_5(self):
        result= fibonacci_1(5)
        self.assertEqual(result, 5)

    def test_6(self):
        result= fibonacci_1(6)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()