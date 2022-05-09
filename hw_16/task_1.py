# Ex.1
# реализовать общий для всех классов
# counter и метод, который его изменяет на 1
# изменения должны быть видны всем дочерним классам


class Parent:

    counter: int = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1


class ChildOne(Parent):
    pass


class ChildTwo(Parent):
    pass


def test_visible_changes():
    for _ in range(5):
        Parent.increment_counter()
        Parent().increment_counter()
        assert ChildOne.counter == ChildTwo.counter == Parent.counter
