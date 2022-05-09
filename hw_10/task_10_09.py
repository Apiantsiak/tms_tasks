# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.


class Parrot:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} Run!")

    def jump(self):
        print(f"{self.name} Jump!")

    def birthday(self):
        self.age += 1
        print(f"Today is my birthday and I am {self.age} years old")

    def sleep(self):
        print(f"{self.name} is sleeping now")

    def fly(self):
        print(f"{self.name} Fly!")


class Cat:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} Run!")

    def jump(self):
        print(f"{self.name} Jump!")

    def birthday(self):
        self.age += 1
        print(f"Today is my birthday and I am {self.age} years old")

    def sleep(self):
        print(f"{self.name} is sleeping now")

    def meow(self):
        print(f"{self.name} Meow!")


class Dog:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} Run!")

    def jump(self):
        print(f"{self.name} Jump!")

    def birthday(self):
        self.age += 1
        print(f"Today is my birthday and I am {self.age} years old")

    def sleep(self):
        print(f"{self.name} is sleeping now")

    def bark(self):
        print(f"{self.name} Woof!")
