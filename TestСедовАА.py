import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
       self.calc = Calculator

    def test_division(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_multiply(self):
        assert self.calc.multiply(self, 7, 2) == 14

    def test_adding(self):
        assert self.calc.adding(self, 4, 5) == 9

    def teardown(self):
        print("Выполнение метода Taerdown")








