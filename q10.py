
class SmartPhone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def make_a_call(self, phone_no):
        print(f"Calling {phone_no}...")

    def __str__(self):
        return f'{self.full_name()} with price {self._price}'

class Truecaller:
    def __init__(self, phone_no):
        self.phone_no = phone_no
    def fetch(self):
        print(f"Fetching details of {self.phone_no}...")

class Myphone(SmartPhone):
    def __init__(self, brand, model_name, price, truecaller):
        super().__init__(brand, model_name, price)
        self.truecaller = truecaller

   