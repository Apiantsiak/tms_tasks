from pydantic import BaseModel

from settings import *


class DbConfig(BaseModel):
    driver: str = 'postgresql'
    host: str
    port: int
    user: str
    pwd: str
    database: str

    @property
    def connection_str(self):
        return f"{self.driver}://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.database}"


DB_CONFIG = DbConfig(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    pwd=DB_PWD,
    database=DB_NAME
)
