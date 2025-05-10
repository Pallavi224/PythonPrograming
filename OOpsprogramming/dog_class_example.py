#define class called dog
class Dog:
    #class variable
    species = "Canis familiaris"

    #initializing the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    #instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."
    #class method
    @classmethod
    def get_species(cls):
        return cls.species
    #static method
    @staticmethod
    def bark():
        return "Woof! Woof!"
    #static method
    @staticmethod
    def bark():
        return "Woof! Woof!"
    #static method
    @staticmethod
    def get_dog_info(name, age):
        return f"Dog Name: {name}, Age: {age}"
    #static method
    @staticmethod
    def get_dog_info(name, age):
        return f"Dog Name: {name}, Age: {age}"
    #static method
    print("Dog class created")
    #static method
    @staticmethod
    def get_dog_info(name, age):
        return f"Dog Name: {name}, Age: {age}"
    #static method
    @staticmethod
    def get_dog_info(name, age):
        return f"Dog Name: {name}, Age: {age}"
    #static method
    print("Dog class created")

    #print result
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(dog1.description())
print(dog2.description())
print(dog1.speak("Woof!"))
print(dog2.speak("Bark!"))
print(Dog.get_species())



#creating object of class Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

#calling instance method
print(dog1.description())
print(dog2.description())
#calling instance method
print(dog1.speak("Woof!"))
print(dog2.speak("Bark!"))
#calling class method
print(Dog.get_species())

#calling static method
print(Dog.bark())
#calling static method
print(Dog.get_dog_info("Buddy", 3))
#calling static method

print(Dog.get_dog_info("Max", 5))
#calling static method
print(Dog.get_dog_info("Buddy", 3))
