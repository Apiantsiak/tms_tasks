# 10.01
# Создать пустой класс Dog

# 10.02
# Создать два объекта класса Dog. Вывести их на экран

# 10.03
# Добавить два метода в класс Dog: jump и run. Методы
# выводят на экран Jump! и Run! соответственно.

# 10.04
# Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark.
# Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

# 10.05
# Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет атрибут имени у объекта.
# Создать один объект класса. Вывести имя.
# Вызвать метод change_name. Вывести имя.

# 10.06
# Добавить в метод инициализации новый приватный атрибут - master.
# Создать метод get_master() который возвращает значение атрибута master.

# 10.07
# Добавить новый приватный атрибут адрес (по-умолчанию равен ‘Minsk’).
# Добавить getter и setter для адреса.


class Dog:

    def __init__(self, height, weight, name, age, master, address="Minsk"):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__address = address

    def get_master(self):
        return self.__master

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def change_name(self, name):
        self.name = name

    @staticmethod
    def jump():
        print("Jump!")

    @staticmethod
    def run():
        print("Run!")

    @staticmethod
    def bark():
        print("Woof!")


first_dog = Dog("1 meter", "8 kilos", "dog's name is first_dog", "age 2", "first_master")
second_dog = Dog("1.2 meter", "7 kilos", "dog's name is second_dog", "age 2", "second_master")

print("First dog methods:")
first_dog.jump()
first_dog.run()
first_dog.bark()

print("\nFirst dog attributes:",
      first_dog.height,
      first_dog.weight,
      first_dog.name,
      first_dog.age, sep="\n")

print("\nSecond dog attributes:",
      second_dog.height,
      second_dog.weight,
      second_dog.name,
      second_dog.age, sep="\n")

first_dog.change_name("new_name_for_first_dog")

print(f"\nFirst dog new name: {first_dog.name}",
      f"First dog privet attributes: {first_dog.get_master()}, {first_dog.get_address()}", sep="\n")
