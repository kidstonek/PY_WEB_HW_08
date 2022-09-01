from random import randint

import psycopg2
# from faker import Faker
from contextlib import contextmanager

from faker import Faker


@contextmanager
def create_connection():
    conn = None
    """ create a database connection to a Postgres database """
    try:
        conn = psycopg2.connect(database="postgres", user="postgres", password="mysecretpassword", host="localhost")
        # print(conn)
        yield conn
        conn.commit()
    except:
        conn.rollback()
        # print(e)
    finally:
        conn.close()


def create_table(conn, create_table_sql):
    c = None
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except:
        pass


fake = Faker()

if __name__ == "__main__":
    # sql_create_table = """CREATE TABLE courses(
    #                     c_no text PRIMARY KEY,
    #                     title text,
    #                     hours integer
    #                     );"""

    sql_create_table = """CREATE TABLE exams(
s_id integer REFERENCES students(s_id),
c_no text REFERENCES courses(c_no),
score integer,
CONSTRAINT pk PRIMARY KEY(s_id, c_no)
);
"""

    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_table)
        else:
            print("Filed to connect to database")
    #
    # sql_insert_table = "INSERT INTO courses(c_no, title, hours) VALUES(%s, %s, %s)"
    #
    # with create_connection() as conn:
    #     if conn is not None:
    #         cr = conn.cursor()
    #         for _ in range(10):
    #             cr.execute(sql_insert_table, (randint(100, 200), fake.name(), randint(1, 10)))
    #         cr.close()
    #     else:
    #         print("Filed to connect to database")
