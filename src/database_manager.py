import sqlite3 as db
from sqlite3 import Error
from os import path
from datetime import datetime

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
        self.connection.commit()
        self.connection.close()

    def create_new_job(self, data):
        sql = "INSERT INTO jobs(name, salary) VALUES(?,?)"

        cur = self.connection.cursor()
        cur.execute(sql, data)

    def list_jobs(self):
        sql = "SELECT * FROM jobs"

        cur = self.connection.cursor()
        cur.execute(sql)
        for row in cur:
            print("- {:s}, {:.2f}".format(row[1], row[2]))

    def parse_period(self, period):
        print(period)
        if period is None:
            past = '2018-01-01 00:00:00'
            future = '2050-12-31 00:00:00'
            return [past, future]
        else:
            format = '%d/%m/%Y'
            try:
                return [datetime.strptime(period[0], format), datetime.strptime(period[1], format)]
            except:
                print("Invalid period")


    def get_stats(self, job, earnings, period):
        sql = "SELECT jobs.name, jobs.salary, SUM(sessions.seconds) FROM jobs JOIN sessions ON jobs.id = sessions.job_id WHERE sessions.session_date >= Datetime(?) AND sessions.session_date <= Datetime(?)"
        parsed_period = self.parse_period(period)

        cur = self.connection.cursor()
        cur.execute(sql, parsed_period)
        result = cur.fetchone()

        if job is not None:
            output = ["", ""]
            if earnings:
                output[0] = result[2]/3600 * result[1] #Total hours multiplied by hourly rate
            if period is not None:
                m, s = divmod(result[2], 60)
                h, m = divmod(m, 60)
                output[1] = "{:d}:{:02d}:{:02d}".format(h, m, s)
            print("{:s} {:s} {:.2f}".format(job, output[1], output[0]))

        #If earnings is true, print earnings
        #If period is not none, print period

    def get_job_id(self, job_name):
        sql = "SELECT id FROM jobs WHERE name = ?"

        cur = self.connection.cursor()
        cur.execute(sql, [job_name])

        result = cur.fetchone()[0]
        if not result == None:
            return result

    def parse_data(self, data):
        job_id = self.get_job_id(data.name)
        return [job_id, str(data.date), data.time]

    def store_session(self, session):
        sql = "INSERT INTO sessions (job_id, session_date, seconds) VALUES(?,?,?)"
        data = self.parse_data(session)

        cur = self.connection.cursor()
        cur.execute(sql, data)

    def create_tables(self):
        job_table_sql = "CREATE TABLE IF NOT EXISTS jobs (id integer PRIMARY KEY, name text NOT NULL, salary double); "
        session_table_sql = "CREATE TABLE IF NOT EXISTS sessions (id integer PRIMARY KEY, job_id integer NOT NULL, session_date text, seconds int, FOREIGN KEY (job_id) REFERENCES jobs(id)); "

        try:
            cursor = self.connection.cursor()
            cursor.execute(job_table_sql)
            cursor.execute(session_table_sql)
        except Error as e:
            print(e)

class Session:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time
