# Object Oriented Programming in Python - Examples

# define class
class Dog:
    # whenever we create a new Dog instance, we would pass a reference to which object 
    # it was called on so we can reference things specifically
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    # we can create method that modifies this attributes
    def set_age(self, age):
        self.age = age
    
    # create method() - this is a function that goes in a class
    # starts with a parameter `self`    
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")
        
        
# we instantiate the class dog using `Dog()`
d = Dog("Tim", 34) # d assigned to an instance of the class Dog. 
d2 = Dog("Bill", 37)
print(d.name)
print(d2.name)

# modifies Bill's age to 23 from 37
d2.set_age(23)
print(d2.get_age())

