

import sqlite3


class DbConnector:

    def __init__(self, config: str):
        self._config = config

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, new_config: str):
        self._config = new_config

    def __enter__(self):
        self.connection = sqlite3.connect(self._config)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type:
            raise exc_type(exc_value)
