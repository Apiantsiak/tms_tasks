# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2

# Using a for loop

first_list: list = list(range(16))
second_list: list = []

for numb in first_list:
    second_list.append(numb * (-2))

print(second_list)

# Using a for while

second_list: list = []
count = 0

while count != len(first_list):
    second_list.append(first_list[count] * (-2))
    count += 1

print(second_list)
