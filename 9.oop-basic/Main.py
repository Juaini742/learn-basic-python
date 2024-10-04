from abc import ABC, abstractclassmethod

"""
Represents a cat with a name and age.

The `Cat` class provides a simple interface for managing a cat's name and age.
It encapsulates the name and age as private attributes, and provides a method to
make the cat meow.
"""
class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def meow(self):
        return f"{self.name}, says meow!!!"

my_cat = Cat("Orange", 3)
print(my_cat.meow())

"""
Represents a car with a brand and model.

The `Car` class provides a simple interface for managing a car's brand and model.
It encapsulates the brand and model as private attributes, and provides a method to
start the car.
"""
class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is started!!"

my_car = Car("Toyota", "sport")
print(my_car.start())



"""
Represents a bank account with a balance that can be deposited to.

The `BankAccount` class provides a simple interface for managing a bank account balance.
It encapsulates the balance as a private attribute, and provides methods to deposit funds
and retrieve the current balance.
"""
class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount(100)
account.deposit(50)
print(account.get_balance())

"""
Represents an animal with a name that can make a sound.

The `Animal` class provides a simple interface for managing an animal's name and sound.
It encapsulates the name as a public attribute, and provides a method to make a sound.

The `Dog` class is a subclass of `Animal` that overrides the `speak` method to make a barking sound.
"""
class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    
    def speak(self):
        return super().speak()
        # return f"{self.name} barks"

my_dog = Dog("Bob")
print(my_dog.speak())

print("+++++++++++++++")

class Bird(Animal):

    def speak(self):
        # return super().speak()
        return f"{self.name} is chirping"
    
animals = [Dog("Boby"), Bird("Eagle")]

for animal in animals:
    print(animal.speak())


"""
Represents a geometric shape with an area calculation.

The `Shape` class is an abstract base class that defines a common interface for calculating the area of a shape. Concrete subclasses must implement the `area` method to provide the specific area calculation.

The `Circle` class is a concrete subclass of `Shape` that represents a circle. It takes a radius parameter in its constructor and implements the `area` method to calculate the area of the circle using the formula `pi * radius^2`.
"""
class Shape(ABC):
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        # super().__init__()
        self.radius = radius
    
    def area(self):
        # return super().area()
        return 3.14 * (self.radius ** 2)

my_circle = Circle(5)
print(my_circle.area())