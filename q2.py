class Profile(object):
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    def update_profile(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location