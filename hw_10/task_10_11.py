# Добавить два новых атрибута в родительский класс: weight и height.
# Добавить методы change_weight, change_height принимающий один
# параметр и прибавляющий его к соответствующему аргументу.
# В случае если параметр не был передан, увеличивать на 0.2.
# Изменить метод fly класса Parrot.
# Если вес больше 0.1 выводить сообщение 'This parrot cannot fly'.


class Pet:

    def __init__(self, name, age, master, weight=1, height=1):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print(f"{self.name} Run!")

    def jump(self):
        print(f"{self.name} Jump!")

    def birthday(self):
        self.age += 1
        print(f"Today is my birthday and I am {self.age} years old")

    def sleep(self):
        print(f"{self.name} is sleeping now")

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 0.2
            print(f"{self.name} weight {self.height}")

    def change_height(self, height=None):
        if height:
            self.height += height
        else:
            self.height += 0.2
            print(f"{self.name} height {self.height}")

    def action(self):
        self.run()
        self.jump()
        self.birthday()
        self.sleep()
        self.change_weight()
        self.change_height()


class Parrot(Pet):

    def fly(self):
        if self.weight > 0.1:
            print("This parrot cannot fly!")
        else:
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
