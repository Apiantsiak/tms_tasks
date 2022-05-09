# Сделать все атрибуты класса Dog приватными.
# Сделать для каждого атрибута getter и setter используя декораторы.
# Все change методы удалить


class Dog:

    def __init__(self, height, weight, name, age, master, address="Minsk"):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__address = address

    @property
    def height(self):
        return self.__height

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight

    @property
    def master(self):
        return self.__master

    @property
    def address(self):
        return self.__address

    @height.setter
    def height(self, height):
        self.__height = height

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @master.setter
    def master(self, master):
        self.__master = master

    @address.setter
    def address(self, address):
        self.__address = address


dog = Dog(1, 2, "dog", "2 year", "Free_Dog", "Streets")

print(dog.height, dog.weight, dog.name, dog.age, dog.master, dog.address, sep="\n")
