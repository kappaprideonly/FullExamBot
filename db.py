
import pymysql as sql

def create_database():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        passwd = "1"
    )
    cur = connect.cursor()
    cur.execute("CREATE DATABASE ege_russian_db;")
    connect.commit()

def create_table():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1"
    )
    cur = connect.cursor()
    query = """CREATE TABLE users
                (
                    id text,
                    first_name text,
                    last_name text,
                    activity integer,
                    answer text,
                    task_number integer,
                    records MEDIUMTEXT,
                    current_score MEDIUMTEXT
                )"""
    cur.execute(query)
    connect.commit()
    print("Table users was created sucessfully")

def drop_table():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1"
    )
    cur = connect.cursor()
    drop_query = "DROP TABLE IF EXISTS users;"
    cur.execute(drop_query)
    connect.commit()
    print("Table was dropped sucessfully\n")

def nenavision():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1"
    )
    cur = connect.cursor()
    records = "1." * 25 + "1"
    cur.execute(f"UPDATE users SET records = '{records}' WHERE first_name = 'nenavision'")
    connect.commit()
    print("Nenavision up-up!\n")    

print(f"Input\n1: create db\n2: create table\n3: drop table\n4: up-up nenavision")
match input():
    case "1":
        create_database()
    case "2":
        create_table()
    case "3":
        drop_table()
    case "4":
        nenavision()
    