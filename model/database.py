import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="Sistema de Biblioteca Universitaria",
            user="postgres",
            password="607337",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
