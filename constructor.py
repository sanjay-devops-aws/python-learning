# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors
# The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None. 
# Parameterized Constructor
# Default Constructor

class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
