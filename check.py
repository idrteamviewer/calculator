import unittest

from calculator import Calculator


class CalculatorTests(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(Calculator.calculate(2, "+", 3), 5)

	def test_subtraction(self):
		self.assertEqual(Calculator.calculate(7, "-", 4), 3)

	def test_multiplication(self):
		self.assertEqual(Calculator.calculate(6, "*", 5), 30)

	def test_division(self):
		self.assertEqual(Calculator.calculate(8, "/", 2), 4)

	def test_division_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			Calculator.calculate(8, "/", 0)


if __name__ == "__main__":
	unittest.main()
