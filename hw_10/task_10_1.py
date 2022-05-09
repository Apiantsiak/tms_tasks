# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута, конструктор,
# геттеры и сеттеры для каждого атрибута, два метода.


from pathlib import Path


class File:

    def __init__(self, file_name: str, file_type: str, master: str):
        self.__file_name = file_name
        self.__file_type = file_type
        self.__master = master

    @property
    def file_name(self):
        return self.file_name

    @file_name.setter
    def file_name(self, file_name):
        self.__file_name = file_name

    @property
    def file_type(self):
        return self.__file_type

    @file_type.setter
    def file_type(self, file_type):
        self.__file_type = file_type

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    def create_file(self):
        """Create a file
        :return: None
        """
        if not Path.is_file(Path(f"{self.__file_name}{self.__file_type}")):
            with open(f"{self.__file_name}{self.__file_type}", "w") as file:
                file.write("")
            print(f"File {self.__file_name}{self.__file_type} was created")
        else:
            print(f"File {self.__file_name}{self.__file_type} already exists")

    def delete_file(self):
        """ Delete a file
        :return: None
        """
        if Path.is_file(Path(f"{self.__file_name}{self.__file_type}")):
            Path(f"{self.__file_name}{self.__file_type}").unlink()
            print(f"File {self.__file_name}{self.__file_type} was deleted")
        else:
            print(f"File {self.__file_name}{self.__file_type} does not exist")

    def file_info(self):
        print(f"Name: {self.__file_name}",
              f"Type: {self.__file_type}",
              f"Owner: {self.__master}", sep="\n")


class Txt(File):
    pass


class Json(File):
    pass


class Csv(File):
    pass


class Xml(File):
    pass


class Pdf(File):
    pass


text_file = Txt("test", ".txt", "Alexey")
text_file.file_info()
text_file.create_file()
text_file.delete_file()
