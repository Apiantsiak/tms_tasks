# Ex.6
# Реализовать класс-миксин, добавляющий классу Car атрибут
# spoiler.
# Spoiler должен влиять на Car.speed , увеличивая ее на значение N.


class SpoilerMixin:

    def __init__(self):
        self.spoiler = False

    def install_spoiler(self):
        self.spoiler = True
