from multiprocessing import connection
import pymysql as sql
import time


def create_database():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    cur.execute("CREATE DATABASE ege_russian_db;")
    connect.commit()

def create_table():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
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
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
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
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    records = "10." * 25 + "10"
    cur.execute(f"UPDATE users SET records = '{records}' WHERE first_name = 'nenavision'")
    connect.commit()
    print("Nenavision up-up!\n")

def But():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass = sql.cursors.DictCursor
    )
    cur = connect.cursor()
    cur.execute(f"SELECT current_score, records FROM users WHERE first_name = '🦋'")
    info = cur.fetchall()[0]
    records = info["records"]
    print(f"         {records}")
    records = records.split(".")
    records[13] = str(26)
    records = ".".join(records)
    print(f"New rec: {records}")
    current_scores = info["current_score"]
    print(f"         {current_scores}")
    current_scores = current_scores.split(".")
    current_scores[7 - 1] = str(16)
    current_scores = ".".join(current_scores)
    print(f"New cur: {current_scores}")
    cur.execute(f"UPDATE users SET records = '{records}' WHERE first_name = '🦋'")
    cur.execute(f"UPDATE users SET current_score = '{current_scores}' WHERE first_name = '🦋'")
    connect.commit()
    print("E|3 up-up!\n")

def add():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    print("ПОЕХАЛИ")
    cur.execute(f"ALTER TABLE users ADD COLUMN `right_ans` integer NOT NULL DEFAULT 0;")
    connect.commit()
    cur.execute(f"ALTER TABLE users ADD COLUMN `wrong_ans` integer NOT NULL DEFAULT 0;")
    connect.commit()
    print("ДОБАВИЛОСЬ ВРОДЕ =)")

def delete():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    print("ПОЕХАЛИ")
    cur.execute(f"ALTER TABLE users DROP COLUMN `right`;")
    connect.commit()
    cur.execute(f"ALTER TABLE users DROP COLUMN `wrong`;")
    connect.commit()
    print("Удалилось ВРОДЕ =)")

def info():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    cur.execute("SELECT * FROM users")
    info = cur.fetchall()
    print(len(info))
    for j in info:
        print(j)
    return

def stats():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    query = """CREATE TABLE stats
                (
                    id integer,
                    counter integer
                )"""
    cur.execute(query)
    connect.commit()
    cur.execute("INSERT INTO stats (id, counter) VALUES ('1', '0')")
    connect.commit()
    print("Table stats was created sucessfully")

def Aristarch_up():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    number = 0
    for i in range(5 * 26):
    # for i in range(1):
        cur.execute(f"SELECT current_score, records FROM users WHERE last_name = 'Samosski'")
        info = cur.fetchall()[0]
        records = info["records"]
        print(f"         {records}")
        records = records.split(".")
        records[number] = str(int(records[number]) + 1)
        records = ".".join(records)
        print(f"New rec: {records}")
        current_scores = info["current_score"]
        print(f"         {current_scores}")
        current_scores = current_scores.split(".")
        current_scores[number] = str(int(current_scores[number]) + 1)
        current_scores = ".".join(current_scores)
        print(f"New cur: {current_scores}")
        cur.execute(f"UPDATE users SET records = '{records}' WHERE last_name = 'Samosski'")
        cur.execute(f"UPDATE users SET current_score = '{current_scores}' WHERE last_name = 'Samosski'")
        connect.commit()
        print("Ja up-up!\n")
        time.sleep(10)
        number += 1


def Jamboid():
    connect = sql.connect(
        host = "35.232.17.130",
        user = "standart",
        database = "ege_russian_db",
        passwd = "1",
        cursorclass=sql.cursors.DictCursor
    )
    cur = connect.cursor()
    cur.execute("SELECT * FROM users WHERE first_name = '🦋'")
    info = cur.fetchall()[0]
    fff = "30.30.30.30.30.30.30.30.30.30.30.30.30.30.31.30.30.30.30.31.30.30.30.30.30.29"
    cur.execute(f"UPDATE users SET records = '{fff}', current_score = '{fff}' WHERE first_name = '🦋'")
    connect.commit()
    print("HAIL")
  

# But()
#Jamboid()
# Aristarch_up()

print(f"Input\n1: create db\n2: create table\n3: drop table\n4: up-up nenavision\n5: add columns\n6: delete columns\n7: info\n8: stats\n9: Aristarch_up")
match int(input()):
    case 1:
        create_database()
    case 2:
        create_table()
    case 3:
        drop_table()
    case 4:
        nenavision()
    case 5:
        add()
    case 6:
        delete()
    case 7:
        info()
    case 8:
        stats()
    case 9:
        Aristarch_up()
    
