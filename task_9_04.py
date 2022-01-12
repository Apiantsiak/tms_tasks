# Имеется текстовый файл. Переписать в другой файл все
# его строки с заменой в них символа 0 на символ 1 и
# наоборот.


from typing import List


# Create file with "0" symbol

try:
    with open("test.txt") as original_file:
        org_file_data: List[str] = original_file.readlines()

    mod_file_data: List[List[str]] = [list(i) for i in org_file_data]

    # data_with_zero = [i.insert(2, "0") for i in mod_file_data]

    for i in mod_file_data:
        i.insert(2, "0")

    data_with_zero: List[str] = ["".join(i) for i in mod_file_data]

    with open("test_9_04.txt", "w") as file_with_zero:
        file_with_zero.writelines(data_with_zero)

except FileNotFoundError as error:
    with open("test.txt", "w") as test_file:
        text_for_wr: List[str] = [f"{i}. Text line\n" for i in range(1, 7)]
        test_file.writelines(text_for_wr)

# Rewrite all file's lines in another file with the replacement
# of the symbol 0 in them with the symbol 1

with open("test_9_04.txt") as org_file:
    text_from_file: List[str] = org_file.readlines()

modify_text: List[List[str]] = [list(char) for char in text_from_file]

for ls in modify_text:
    for pos, val in enumerate(ls):
        if val == "0":
            ls.insert(pos, "1")
            del ls[pos + 1]

text_for_wr: List[str] = ["".join(i) for i in modify_text]

with open("test_9_04(1).txt", "w") as file_for_wr:
    file_for_wr.writelines(text_for_wr)
