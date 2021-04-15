# learn python: https://www.learnpython.org/en/Classes_and_Objects
# learn python https://www.programiz.com/python-programming/class

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60.000

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10.000

# test code
print(car1.description())
print(car2.description())


    fer is a red convertible worth $60.00.
    Jump is a blue van worth $10.00.
