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
        conn = psycopg2.connect(database="postgres", user="postgres", password="111222333", host="localhost")
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


fake = Faker('uk_UA')

if __name__ == "__main__":
    # sql_create_table = """CREATE TABLE courses(
    #                     c_no text PRIMARY KEY,
    #                     title text,
    #                     hours integer
    #                     );"""

    # sql_create_table = """CREATE TABLE students(
    #                     id INTEGER PRIMARY KEY,
    #                     student_name text
    #                     );"""

    # sql_create_table = """CREATE TABLE teachers(
    #                     id INTEGER PRIMARY KEY,
    #                     teacher_name text,
    #                     );"""

    # sql_create_table = """CREATE TABLE s_groups(
    #                     group_id integer PRIMARY KEY,
    #                     group_name VARCHAR(20)
    #                     );"""

#     sql_create_table = """CREATE TABLE subjects(
#                         s_id integer PRIMARY KEY,
#                         subject_name VARCHAR(20),
#                         t_id integer
#                         );"""
#
#      sql_create_table = """CREATE TABLE grades(
#                     g_id serial PRIMARY KEY,
#                     student_id integer,
#                     sub_id integer,
#                     grade integer
#                     );"""
# #
#     with create_connection() as conn:
#         if conn is not None:
#             create_table(conn, sql_create_table)
#             print('ok')
#         else:
#             print("Filed to connect to database")
    #
    # sql_insert_table = "INSERT INTO s_groups(group_id, group_name) VALUES(%s, %s)"
    # sql_insert_table = "INSERT INTO students(id, student_name, s_group_id) VALUES(%s, %s, %s)"
    # sql_insert_table = "INSERT INTO teachers(id, teacher_name, subj_id) VALUES(%s, %s)"
    # sql_insert_table = "INSERT INTO subjects(g_id, student_id, sub_id, grade) VALUES(%s, %s, %s, %s)"
    sql_insert_table = "INSERT INTO grades(student_id, sub_id, grade) VALUES(%s, %s, %s)"

    # # gp = ['Фин-01', "ПЗ-04", "ИЛ-05", "ФІН-21"]
    # # Add students
    # with create_connection() as conn:
    #     if conn is not None:
    #         cr = conn.cursor()
    #         for i in range(30):
    #             cr.execute(sql_insert_table, (i+1, fake.name(), randint(0, 2)))
    #         cr.close()
    #     else:
    #         print("Filed to connect to database")

    # add teachers
    # with create_connection() as conn:
    #     if conn is not None:
    #         cr = conn.cursor()
    #         for i in range(3):
    #             cr.execute(sql_insert_table, (i+1, fake.name())
    #         cr.close()
    #     else:
    #         print("Filed to connect to database")

    # subj = ['Вища математика', "Фізика", "Кібірнетика", "Фіз-ра", "Механіка"]
    # # add subjects
    # with create_connection() as conn:
    #     if conn is not None:
    #         cr = conn.cursor()
    #         for i in range(len(subj)):
    #             cr.execute(sql_insert_table, (i+1, subj[i], randint(1, 3)))
    #         cr.close()
    #     else:
    #         print("Filed to connect to database")

    # add grades
    with create_connection() as conn:
        if conn is not None:
            cr = conn.cursor()
            for stud in range(30):
                for sub in range(5):
                    cr.execute(sql_insert_table, (stud+1, sub+1, randint(1, 12)))
            cr.close()
        else:
            print("Filed to connect to database")