
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

from session import ENGINE

Base = declarative_base()


class RequestsLog(Base):
    __tablename__ = "request_log"

    request_id = Column(Integer, primary_key=True)
    number = Column(String(50))
    info = Column(Text)


if __name__ == '__main__':
    Base.metadata.create_all(ENGINE)
