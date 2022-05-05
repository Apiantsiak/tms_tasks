
import numpy as np
from numpy.typing import NDArray


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
