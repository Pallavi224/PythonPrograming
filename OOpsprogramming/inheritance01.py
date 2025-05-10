class parent:
    def __init__(self):
        print("This is parent class constructor")
        self.name = "Parent"
        self.age = 50

    def display(self):
        print("This is parent class method")
        print(f"Name: {self.name}, Age: {self.age}")

class child(parent):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        print("This is child class constructor")
        self.name = "Child"
        self.age = 10

    def display(self):
        print("This is child class method")
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the child class
child_obj = child()
child_obj.display()  # Call the display method of the child class   
parent_obj = parent()
parent_obj.display()  # Call the display method of the parent class
print("This code demonstrates the concept of inheritance in Python. The child class inherits properties and methods from the parent class.")
#print output
#initializing the class
#creating object of class Dog



# Output:
# This is parent class constructor
# This is child class constructor
# This is child class method
# Name: Child, Age: 10
# This is parent class method
# Name: Parent, Age: 50
# This code demonstrates the concept of inheritance in Python. The child class inherits properties and methods from the parent class.
# The child class can override methods from the parent class and also call the parent class constructor using super().
# The child class can also have its own properties and methods.






# Inheritance allows for code reusability and a hierarchical class structure.
# In this example, the child class inherits from the parent class, and both classes have their own constructors and display methods.
# The child class constructor calls the parent class constructor
# using super(), allowing it to initialize properties from the parent class.
# The display method in the child class overrides the display method in the parent class, demonstrating polymorphism.
