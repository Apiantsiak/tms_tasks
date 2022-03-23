# Ex.6
# Реализовать класс-миксин, добавляющий классу Car атрибут
# spoiler.
# Spoiler должен влиять на Car.speed , увеличивая ее на значение N.


class Spoiler:

    def __init__(self):
        self.status = None


class SpoilerMixin:

    def __init__(self):
        self.spoiler = Spoiler()

    def activate_spoiler(self):
        self.spoiler.status = True

    def deactivate_spoiler(self):
        self.spoiler.status = False
