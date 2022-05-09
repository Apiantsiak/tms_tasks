# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.


from typing import List


with open("test.txt", "w") as test_file:
    text_for_wr: List[str] = [f"{i}. Text line\n" for i in range(1, 7)]
    test_file.writelines(text_for_wr)

with open("test.txt") as test_file:
    file_text: List[str] = test_file.readlines()

counter: int = 0

while True:

    if not counter:
        print(f"a)\t{file_text[counter].strip()}")
        counter += 1
    elif counter == 1:
        print(f"b)\t{file_text[4].strip()}")
        counter += 1
    elif counter == 2:
        print("c)", end=" ")
        for i in file_text[:5]:
            print(f"\t{i.strip()}")
        counter += 1
    elif counter == 3:
        print("d)", end=" ")
        for i in file_text[:counter]:
            print(f"\t{i.strip()}")
        counter += 1
    else:
        print("e)", end=" ")
        for i in file_text:
            print(f"\t{i.strip()}")
        counter = 0
        break
