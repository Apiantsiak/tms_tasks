# Получить сумму кубов натуральных чисел от n до m используя цикл for

cube_sum: int = 0

for var in range(1, 11):
    cube_sum += var ** 3

print(cube_sum)
