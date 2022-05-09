# Составить список чисел Фибоначчи содержащий 15 элементов.

# Using a for loop

fibonachi_numbs: list = []
a, b = 0, 1

for _ in range(15):
    a, b = b, a + b
    fibonachi_numbs.append(a)

print("Result using a for loop:", fibonachi_numbs)

# Using a while loop

fibonachi_numbs: list = []
counter: int = 15
a, b = 0, 1

while counter:
    a, b = b, a + b
    fibonachi_numbs.append(a)
    counter -= 1

print("Result using a while loop:", fibonachi_numbs)
