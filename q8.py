class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

class Calculator2_0(Calculator):
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2

class Phone:
 def __init__(self):
  self.features = ["calling", "sms"]
 
 def print_features(self):
  print(self.features)

class SmartPhone(Calculator2_0, Phone):
    def __init__(self, make, model, price, color, qty):
        super().__init__(price, qty)
        self.make = make
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.make} {self.model} Smartphone: quantity- {self.qty} price- {self.price}"

    def __repr__(self):
        return f"{self.make} {self.model} Smartphone: quantity- {self.qty} price- {self.price}"