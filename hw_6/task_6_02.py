# Написать программу для работы с матрицами:
# 1. Создание +
# 2. Вывод +
# 3. Сумма всех элементов +
# 4. Нахождение максимального элемента +
# 5. Нахождение минимального элемента +


from random import randint
from typing import List


def matrix_func(rand_from=1, rand_to=9) -> List[List[int]]:
    """Create a matrix"""
    matrix: List[List[int]] = [[randint(1, 100) for _ in range(rand_from)]
                               for _ in range(rand_to)
                               ]
    return matrix


def matrix_pprint_func(rand_ls: List[List[int]]) -> None:
    """Output a matrix in a convenient format"""
    for i in rand_ls:
        print(i)


def matrix_args_sum_func(rand_ls: List[List[int]]) -> int:
    """Find the SUM of matrix value"""
    sum_args = sum(j for i in rand_ls for j in i)
    return sum_args


def matrix_max_func(rand_ls: List[List[int]]) -> int:
    """Find MAX value in matrix"""
    max_values = []
    for i in rand_ls:
        max_values.append(max(i))
    return max(max_values)


def matrix_min_func(rand_ls: List[List[int]]) -> int:
    """Find MIN value in matrix"""
    min_values = []
    for i in rand_ls:
        min_values.append(min(i))
    return min(min_values)


user_ls = matrix_func(randint(1, 10), randint(1, 10))
matrix_pprint_func(user_ls)

print(f"\nThe SUM of matrix values is - {matrix_args_sum_func(user_ls)}",
      f"The MAX value in matrix is - {matrix_max_func(user_ls)}",
      f"The MIN value in matrix is - {matrix_min_func(user_ls)}",
      sep="\n")
