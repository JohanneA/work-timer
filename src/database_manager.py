import sqlite3 as db
from sqlite3 import Error
from os import path

class Database:
    def __init__(self):
        self.connection = ""

    def start(self):
        db_path = path.join(path.dirname(path.dirname(path.abspath(__file__))), "database", "database.db")
        try:
            self.connection = db.connect(db_path)
        except Error as err:
            print(err)

    def close(self):
        self.connection.close()

    def create_new_job(self, name):
        pass

    def get_stats(self, earnings, period):
        pass

    def store_session(self, session):
        pass

    def create_tables(self):
        job_table_sql = "CREATE TABLE IF NOT EXISTS jobs (id integer PRIMARY KEY, name text NOT NULL, salary double); "
        session_table_sql = "CREATE TABLE IF NOT EXISTS sessions (id integer PRIMARY KEY, job_id, integer NOT NULL, session_date text, seconds int, FOREIGN KEY (job_id) REFERENCES jobs(id)); "

        try:
            cursor = self.connection.cursor()
            cursor.execute(job_table_sql)
            cursor.execute(session_table_sql)
        except Error as e:
            print(e)


class Session:
    def __init__(self, date, time):
        self.date = date#get today's date
        self.time = time
