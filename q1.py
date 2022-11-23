class Profile:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def print_profile(self):
        print("Name: {} \nEmail: {} \nAge: {}".format(self.name, self.email, self.age))


profile1 = Profile("John Doe", "john@doe.com", "30")
profile1.print_profile()