# Ex1
# Класс NamesIterable принимает коллекцию Фамилия Имя Отчество.
# Реализовать итератор, который будет возвращать элементы, ориентируясь на Имя
# Разделители могут быть ' ', '_', '-'


import pytest
from typing import List


names: List[str] = ['Ivanov Ivan Ivanovich', 'Petrova Olga Sergeevna', 'Petrichenko_Olga_Vladimirovna']


class NamesIterable:

    def __init__(self, collection, name: str = '', cursor=-1):
        self._collection = collection
        self._cursor = cursor
        self.name = name

    def __next__(self):
        if (self._cursor + 1) >= len(self._collection):
            raise StopIteration
        elif not isinstance(self.name, str):
            raise ValueError
        self._cursor += 1
        if self.name not in self._collection[self._cursor]:
            self._cursor += 1
        return self._collection[self._cursor]

    def __iter__(self):
        return self


def test_correct_data_output():
    iterator = NamesIterable(names, 'Olga')
    assert list(iterator) == ['Petrova Olga Sergeevna', 'Petrichenko_Olga_Vladimirovna']


def test_negative_stop_iter():
    iterator = NamesIterable(names)
    with pytest.raises(StopIteration):
        counter = len(names) + 1
        while counter:
            next(iterator)
            counter -= 1


def test_negative_invalid_value():
    iterator = NamesIterable(names, 10)
    with pytest.raises(ValueError):
        next(iterator)
