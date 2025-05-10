class parent:
    def __init__(self, name=None):
        print("parent class constructor")
        if name:
            print(f"Name: {name}")

    def parent_method(self):
        print("This is a method in the parent class.")

    def __init__(self, name=None):
        super().__init__(name)
        print("child class constructor")

    def childMethod(self):
        print("This is a method in the child class.")

class child(parent):
    def __init__(self, name=None):
        super().__init__(name)
        print("child class constructor")

    def childMethod(self):
        print("child class method")
    def parentMethod(self):
        print("parent class method")
    def parentMethod(self):
        print("parent class method")
    def childMethod(self):


        child_obj = child("Child")
        print("child class method")
        child_obj.childMethod()
        child_obj.parentMethod()

    #creating object of class parent