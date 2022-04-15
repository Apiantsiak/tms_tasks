# Ex.2
# Написать фикстуру, которая окрывает соединение к тестовой базе данных
# и возвращает объект сессии/соединения.
# Из less_020 с помощью ORM записать в базу данные о книгах/издателях.
# Написать тест, который проверяет, что все записи были добавлены в бд.
# После выполнения теста соединение к бд должно быть закрыто в фикстуре

# Ex.3
# Написать фикстуру, которая генерирует строку случайных символов заданной длины

import pytest

from string import ascii_letters
from random import choice, shuffle
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


@pytest.fixture(params=[15, 20, 25, 30])
def gen_random_letters_range(request) -> str:
    ascii_ls = list(ascii_letters)
    shuffle(ascii_ls)
    random_chars_str = "".join([choice(ascii_ls) for _ in range(request.param)])
    return random_chars_str


@pytest.fixture
def open_db_test_session():
    db_connect_str = "postgresql://avp:avp@localhost:8432/test_DB"
    engine = create_engine(db_connect_str)
    session = Session(engine)
    yield session
    session.commit()
    session.close()
