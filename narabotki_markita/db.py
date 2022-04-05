
import pymysql as sql

def create_database():
    connect = sql.connect(
        host = "0.0.0.0",
        user = "root",
        passwd = ""
    )
    cur = connect.cursor()
    cur.execute("CREATE DATABASE ege_russian_db;")
    connect.commit()

def create_table():
    connect = sql.connect(
        host = "0.0.0.0",
        user = "root",
        database = "ege_russian_db",
        passwd = ""
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
        host = "0.0.0.0",
        user = "root",
        database = "ege_russian_db",
        passwd = ""
    )
    cur = connect.cursor()
    drop_query = "DROP TABLE IF EXISTS users;"
    cur.execute(drop_query)
    connect.commit()
    print("Table was dropped sucessfully\n")
    

print(f"Input\n1: create db\n2: create table\n3: drop table\n")
match input():
    case "1":
        create_database()
    case "2":
        create_table()
    case "3":
        drop_table()