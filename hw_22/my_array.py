
import pytest
import numpy as np
from numpy.typing import NDArray

from hw_16.task_3 import Circle


class MyArray(np.ndarray):

    def __add__(self, other) -> NDArray:
        if len(self.shape) > 1:
            result = []
            for i in range(len(self)):
                result.append([])
                for j in range(len(self[i])):
                    result[i].append(self[i][j].square() + other[i][j].square())
            return np.array(result)
        else:
            return np.array([self[index].square() + other[index].square() for index in range(len(self))])

    def __mul__(self, other) -> NDArray:
        if len(self.shape) > 1:
            result = []
            for i in range(len(self)):
                result.append([])
                for j in range(len(self[i])):
                    result[i].append(self[i][j].square() * other[i][j].square())
            return np.array(result)
        else:
            return np.array([self[index].square() * other[index].square() for index in range(len(self))])


def test_add_arrays_negative():
    circle = Circle()
    circle.radius = 1
    circle_array = np.array([[circle for _ in range(3)] for _ in range(3)])
    circle_square_array = np.array([[circle.square() for _ in range(3)] for _ in range(3)])
    assert isinstance(circle_array[0][0], Circle)
    assert isinstance(circle_square_array[0][0], float)
    with pytest.raises(TypeError):
        circle_array + circle_array


def test_add_arrays():
    circle = Circle()
    circle.radius = 1
    circle_array = np.array([[circle for _ in range(3)] for _ in range(3)])
    my_circle_array = MyArray((3, 3), dtype=object, buffer=circle_array)
    assert isinstance(my_circle_array[0][0], Circle)
    my_circle_array + my_circle_array
