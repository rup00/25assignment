class Truecaller:

    def get_name(self, number):
        return self.data.get(number)

    def add_entry(self, number, name):
        self.data[number] = name