
from contextlib import contextmanager
from typing import ContextManager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import DB_CONFIG


ENGINE = create_engine(DB_CONFIG.connection_str)
DB_SESSION = sessionmaker(bind=ENGINE)


@contextmanager
def open_db_session(with_commit=False) -> ContextManager[DB_SESSION]:
    session = DB_SESSION()
    try:
        yield session
        if with_commit:
            session.commit()
    except:
        session.rollback()
        raise
    session.close()
