# Ex.3
# Реализовать класс, который опрашивает ресурс http://numbersapi.com/
# Метод класса должен принимать любое число в соответствии с api и
# сохранять результат в локальном хранилище в формате
#                 number: info
# Класс должен иметь возможность преобразовывать информацию в json
#
# Ex.4*
# В качестве локального хранилища использовать собственную базу. Схему и таблицы продумать самим


import requests
from typing import Literal, Union, NoReturn

from models import RequestsLog
from session import open_db_session


class AskNumbersApi:
    _req_types = Literal['trivia', 'math', 'date', 'year']

    def __init__(self, number: Union[int, str], req_type: _req_types) -> NoReturn:
        self.number = number
        self.req_type = req_type
        self._url = f'http://numbersapi.com/{self.number}/{self.req_type}'.strip()

    @property
    def url(self):
        return self._url

    def change_req_params(self, number: Union[int, str], req_type: _req_types) -> NoReturn:
        self.number = number
        self.req_type = req_type
        self._url = f'http://numbersapi.com/{self.number}/{self.req_type}'

    def send_request(self, parameter: str = None):
        if parameter:
            self._url += f'?{parameter}'
        req_res = requests.get(self._url, json=True)
        with open_db_session(with_commit=True) as session:
            log = RequestsLog(
                number=req_res.json()['number'],
                info=req_res.json()['text']
            )
            session.add(log)
        return req_res.json() if req_res.status_code == 200 else f'Something wrong status code: {req_res.status_code}'
