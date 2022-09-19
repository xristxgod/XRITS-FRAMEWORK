import os
import sqlite3
from typing import Optional


class DBConnector:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(DBConnector, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, database_path: str):
        self.__connection: sqlite3.Connection = sqlite3.connect(database_path)

    def fetch(self, query: str):
        cursor = self.__connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    
