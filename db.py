import pymysql as sql

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
    records = "1." * 25 + "1"
    cur.execute(f"UPDATE users SET records = '{records}' WHERE first_name = 'nenavision'")
    connect.commit()
    print("Nenavision up-up!\n")


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

print(f"Input\n1: create db\n2: create table\n3: drop table\n4: up-up nenavision\n5: add columns\n6: delete columns\n7: info\n8: stats")
match input():
    case "1":
        create_database()
    case "2":
        create_table()
    case "3":
        drop_table()
    case "4":
        nenavision()
    case "5":
        add()
    case "6":
        delete()
    case "7":
        info()
    case "8":
        stats()

    