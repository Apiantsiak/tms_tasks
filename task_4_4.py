# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1

numbs: list = list(range(1, 6))

# Using a for loop

for _ in range(len(numbs) - 1):
    numbs.insert(0, numbs.pop())

print("Result using a for loop:", numbs)

# Using a while loop

numbs: list = list(range(1, 6))
counter: int = len(numbs) - 1

while counter:
    numbs.insert(0, numbs.pop())
    counter -= 1

print("Result using a while loop:", numbs)
