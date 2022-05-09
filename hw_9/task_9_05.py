# Имеется текстовый файл. Все четные строки этого файла
# записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.


from typing import List
# from pathlib import Path

try:
    with open("test.txt") as text_file:
        data_file: List[str] = text_file.readlines()

except FileNotFoundError as error:
    with open("test.txt", "w") as text_file:
        text_file.writelines([f"{i}. Text line\n" for i in range(1, 11)])
    with open("test.txt") as text_file:
        data_file: List[str] = text_file.readlines()

even_data: List[str] = [line for pos, line in enumerate(data_file) if pos % 2]

with open("test_9_05(1).txt", "w") as even_line_file:
    even_line_file.writelines(even_data)

with open("test_9_05(2).txt", "w") as odd_line_file:
    odd_line_file.writelines(data_file[::2])

# Just to try deleting file with help of Python

# if Path.is_file(Path("test.txt")):
#     del_files = input("Do you want to delete created files? y/n: ")
#     if del_files == "y":
#         Path("test.txt").unlink()
#         Path("test_9_05(1).txt").unlink()
#         Path("test_9_05(2).txt").unlink()
#         Path("test_json.txt").unlink()
#         Path("test_9_06.txt").unlink()
#         Path("test_9_06(1).txt").unlink()
#         Path("test_json(1).txt").unlink()
#         Path("test_9_04.txt").unlink()
#         Path("test_9_04(1).txt").unlink()
