class Cat:

    species = 'feline'

    def __init__(self, name, age=3, color='white'):
        self.name = name
        self.age = age
        self.color = color


    def meow(self):
        print("Hello!")

my_cat = Cat('Fluffy',10)
second_cat = Cat('Kitty', 15)


# print(my_cat.species)
# print(second_cat.species)

# print(my_cat.color)
# print(second_cat.color)
# my_cat.meow()


class Account:
    def __init__(self, balance):
        # Conventionally "private" attribute
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")

    # Method to safely retrieve the balance
    def get_balance(self):
        return self._balance


# Accessing the data through controlled methods is preferred
# my_account = Account(100)
# my_account.deposit(50)
# my_account._balance += 50
# print(my_account._balance)
# Output: Deposited 50. New balance: 150




class CoffeeMachine:
    # Private method (convention: only for internal use)
    def _grind_beans(self):
        print("1. Grinding beans (complex internal process...)")

    # Private method
    def _heat_water(self):
        print("2. Heating water to 92°C (complex internal process...)")

    # Public, Abstracted Method
    def make_drink(self, drink_type):
        """A simple interface for the user."""
        print(f"\n--- Starting to make {drink_type} ---")

        # Internal complexity is handled here
        self._grind_beans()
        self._heat_water()

        if drink_type == "espresso":
            print("3. Pushing high-pressure water through grounds.")
        elif drink_type == "latte":
            print("3. Pushing water. 4. Steaming milk.")
        else:
            print("3. Making Coffee")

        print("--- Your drink is ready! ---")


# Usage
# machine = CoffeeMachine()
# The user only needs to know the simple 'make_drink' interface
# machine.make_drink("espresso")


class Animal:
    def __init__(self, name, food="meat"):
        self.name = name
        self.food = food

    def eat(self):
        print(f"{self.name} is eating {self.food}")


unknown_animal = Animal("Unknown Animal")
# unknown_animal.eat()

class Mammal(Animal):
    def __init__(self, name, food="meat", num_legs=4):
        super().__init__(name, food)
        self.num_legs = num_legs

    def breathe(self):
        print(f"{self.name} is breathing air")


lion = Mammal("Lion", "Pizza", num_legs=4)
# lion.eat()
# lion.breathe()


class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


shapes = [Circle(3), Square(4)]
for shape in shapes:
    print(f"Area of {shape.__class__.__name__} is {shape.calculate_area():.2f}")
