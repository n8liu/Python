import unittest
import src.recursive as recursive

class TestRecursion(unittest.TestCase):
    def test_print(self):
        self.assertEqual(recursive.print_until_0(5), 0)

    def test_add(self):
        self.assertEqual(recursive.add_all(5), 15)

    def test_fibonacci(self):
        self.assertEqual(recursive.fibonacci(1), 0)
        self.assertEqual(recursive.fibonacci(2), 1)
        self.assertEqual(recursive.fibonacci(3), 1)
        self.assertEqual(recursive.fibonacci(9), 21)

unittest.main()