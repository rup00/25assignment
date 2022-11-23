

class Profile(object):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def update_profile(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def get_profile(self):
        return self.name, self.age, self.email
        
        
profile = Profile('John Doe', 30, 'john.doe@example.com')
print(profile.get_profile())

profile.update_profile('Jane Doe', 32, 'jane.doe@example.com')
print(profile.get_profile())