# Дан двумерный массив n × m элементов.
# Определить, сколько раз встречается число 7 среди элементов массива.

from random import randint
from typing import List

n, m = randint(1, 9), randint(1, 9)
square_matrix: List[List[int]] = [[randint(1, 9) for i in range(n)] for j in range(m)]
counter: int = 0

for i in square_matrix:
    print(i, end="\n")
    for j in i:
        if j == 7:
            counter += 1

print("Values 7 appears {} times".format(counter))
