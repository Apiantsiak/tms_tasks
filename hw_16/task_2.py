# Ex.2
# реализовать класс, который имеет атрибут журнала логирования,
# куда попадают строки вида
# <дата-время вызова>-<класс>-<вызываемый
#
# * реализовать декоратор, которым можно будет оборачивать тот метод,
# который мы захотим залогировать


from datetime import datetime
from typing import Dict


def login_action_deco(meth):

    def wrapper(self, *args, **kwargs):
        self.__class__.logs[f'{datetime.now()}'] = {self.__class__.__name__: meth.__name__}
        return meth(self, *args, **kwargs)

    return wrapper


class Base:

    logs: Dict[str, Dict[str, str]] = {}

    @login_action_deco
    def __init__(self):
        self.value = self.__class__

    @login_action_deco
    def show(self):
        return self.value


def test_change_logs():
    initial_logs_len = len(Base.logs)
    b = Base()
    b.show()
    assert len(Base.logs) != initial_logs_len
    assert len(Base.logs) == 2
