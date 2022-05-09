# Дан произвольный список, содержащий только числа.
# Выведите результат сложения всех чисел больше 10.

numbs: list = list(range(66))
sum_numbs: int = 0

for val in numbs:
    if val > 10:
        sum_numbs += val

print(sum_numbs)
