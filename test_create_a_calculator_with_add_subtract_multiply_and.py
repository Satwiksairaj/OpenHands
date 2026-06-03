import pytest
from create_a_calculator_with_add_subtract_multiply_and import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
    def test_subtract(self):
        assert self.calc.subtract(5, 2) == 3
        assert self.calc.subtract(2, 5) == -3
    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-1, 5) == -5
    def test_divide(self):
        assert self.calc.divide(10, 2) == 5
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
