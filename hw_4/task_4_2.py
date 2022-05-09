# Дан список целых чисел. Подсчитать сколько четных чисел в списке

# Using a for loop

numbs: list = list(range(16))
even_numbs_counter: int = 0

for numb in numbs:
    if numb % 2 == 0 and 0 < numb:
        even_numbs_counter += 1

print("Result using a for loop:", even_numbs_counter)

# Using a while loop

even_numbs_counter: int = 0
counter: int = 0

while counter < len(numbs):
    if numbs[counter] % 2 == 0 and numbs[counter] != 0:
        even_numbs_counter += 1
    counter += 1

print("Result using a while loop:", even_numbs_counter)
