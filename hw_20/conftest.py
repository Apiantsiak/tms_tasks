
import pytest
from typing import Dict
from pprint import pprint

from session import open_db_session
from queries import QUERIES


@pytest.fixture
def execute_queries() -> Dict[str, str]:
    results: Dict[str, str] = {}
    with open_db_session() as session:
        for key, value in QUERIES.items():
            results[key] = session.execute(value).fetchall()
    return results
