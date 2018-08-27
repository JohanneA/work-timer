import sqlite3 as db
from sqlite3 import Error
from os import path

class Database:
    def __init__(self):
        connection = ""

    def start(self):
        db_path = path.join(path.dirname(path.dirname(path.abspath(__file__))), "database", "database.db")
        try:
            self.connection = db.connect(db_path)
        except Error as err:
            print(err)

    def close(self):
        self.connection.close()
