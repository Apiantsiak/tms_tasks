# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки,
# в которой эти файлы отличаются друг от друга.


from typing import List


with open("test_9_06.txt", "w") as first_file:
    text_for_wr: List[str] = [f"{i}. Text line\n" for i in range(1, 6)]
    first_file.writelines(text_for_wr)

with open("test_9_06(1).txt", "w") as second_file:
    text_for_wr: List[str] = [f"{i}. Text line\n" for i in range(1, 11) if i % 2]
    second_file.writelines(text_for_wr)

with open("test_9_06.txt") as first_file:
    first_file_data: List[str] = first_file.readlines()

with open("test_9_06(1).txt") as second_file:
    second_file_data: List[str] = second_file.readlines()

counter: int = 0
while True:
    if counter == len(first_file_data) or counter == len(second_file_data):
        print("One of the files ended")
        break
    else:
        if first_file_data[counter] == second_file_data[counter]:
            counter += 1
            continue
        else:
            print(f"File lines doesn't match in {counter + 1} line:",
                  f"'{first_file_data[counter].strip()}' <-> '{second_file_data[counter].strip()}'", sep="\n")
            break
