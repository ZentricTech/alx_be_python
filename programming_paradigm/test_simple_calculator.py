# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test the addition method
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)        # Normal addition
        self.assertEqual(self.calc.add(-1, 1), 0)       # Adding negative numbers
        self.assertEqual(self.calc.add(-2, -3), -5)     # Adding two negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)        # Adding zero

    # Test the subtraction method
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)   # Normal subtraction
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Subtracting a larger number
        self.assertEqual(self.calc.subtract(-3, 5), -8) # Subtracting positive from negative
        self.assertEqual(self.calc.subtract(0, 0), 0)   # Subtracting zero from zero

    # Test the multiplication method
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)     # Normal multiplication
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Multiplying negative number
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Multiplying by zero
        self.assertEqual(self.calc.multiply(0, 0), 0)      # Multiplying two zeros
        self.assertEqual(self.calc.multiply(-2, -3), 6)    # Multiplying two negative numbers

    # Test the division method
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)        # Normal division
        self.assertEqual(self.calc.divide(-6, 3), -2)       # Division with negative numerator
        self.assertEqual(self.calc.divide(6, -3), -2)       # Division with negative denominator
        self.assertEqual(self.calc.divide(0, 5), 0)         # Zero divided by a number
        self.assertEqual(self.calc.divide(5, 0), None)      # Division by zero
        self.assertEqual(self.calc.divide(0, 0), None)      # Edge case: 0 divided by 0 (undefined)

if __name__ == "__main__":
    unittest.main()
