# Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet.
# Удалить в дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.


class Pet:
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

    def action(self):
        self.run()
        self.jump()
        self.birthday()
        self.sleep()


class Parrot(Pet):

    def fly(self):
        print(f"{self.name} Fly!")


class Cat(Pet):

    def meow(self):
        print(f"{self.name} Meow!")


class Dog(Pet):

    def bark(self):
        print(f"{self.name} Woof!")


parrot = Parrot("parrot", 1, "ted")
cat = Cat("cat", 2, "bob")
dog = Dog("dog", 3, "tom")

print("Parrot methods:")
parrot.action()
parrot.fly()
print("\nCat methods:")
cat.action()
cat.meow()
print("\nDog methods:")
dog.action()
dog.bark()
