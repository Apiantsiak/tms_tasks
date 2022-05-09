
from sqlalchemy import (
    Column, ForeignKey, Integer, String
)
from sqlalchemy.orm import declarative_base, relationship
from pprint import pprint

from DB_session import open_db_session, ENGINE

Base = declarative_base()


class Publishers(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __repr__(self):
        return f'Publisher(id={self.id}, name={self.name})'


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_name = Column(String(40), nullable=False)
    publisher_id = Column(Integer, ForeignKey('publishers.id'), nullable=False)

    def __repr__(self):
        return f'Books(id={self.id}, book_name={self.book_name}, publisher_id={self.publisher_id})'


def insert_into_tables():
    joanne_rowling = Publishers(
        name='Joanne Rowling'
    )
    harry_potter = Books(
        book_name='Harry Potter',
        publisher_id=1
    )
    with open_db_session(with_commit=True) as session:
        session.add_all([joanne_rowling, harry_potter])


def test_check_db_data(open_db_test_session):
    result_pub = open_db_test_session.query(Publishers).all()
    result_book = open_db_test_session.query(Books).all()
    assert result_pub[0].name == 'Joanne Rowling'
    assert result_book[0].book_name == 'Harry Potter'
