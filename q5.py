class Calculator:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def add(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1 + self.value2

    def subtract(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1 - self.value2

value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))

calc = Calculator()

print("Addition: ", calc.add(value1, value2))
print("Subtraction: ", calc.subtract(value1, value2))