"""Create files for tasks"""


from typing import List
from pathlib import Path


def file_creator(file_name: str, type_of_task: str, start: int, end: int):
    files_name_ls: List[str] = []
    if type_of_task == "hw":
        files_name_ls = [f"{file_name}_{numb}.py" for numb in range(start, end + 1)]
    elif type_of_task == "clw":
        if end < 10:
            files_name_ls = [f"{file_name}_0{numb}.py" for numb in range(start, end + 1)]
        elif end >= 10:
            files_name_ls = [f"{file_name}_0{numb}.py" for numb in range(start, 10)]
            delta: int = end - 10
            files_name_ls.extend([f"{file_name}_{numb}.py" for numb in range(10, 11 + delta)])

    for name in files_name_ls:
        if not Path.is_file(Path(name)):
            with open(name, "w") as file:
                file.write("")
            print(f"File {name} was created")


if __name__ == "__main__":
    file_creator("test", "hw", 1, 1)
