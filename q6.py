class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

class Calculator2_0(Calculator):
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2

calc = Calculator2_0(10, 5)
print(calc.multiply())
print(calc.divide())