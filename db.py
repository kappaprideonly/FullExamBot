import psycopg2 as pymysql
from psycopg2.extras import RealDictCursor
import time
from config import _password, _host, _user, _port, _db_name
from pprint import pprint

def create_database():
    return 0
    # connect = pymysql.connect(
    #     host = "35.232.17.130",
    #     user = "standart",
    #     passwdord = "1",
    #     port = "5432"
    # )
    # cur = connect.cursor(cursor_factory=DictCursor)
    # cur.execute("CREATE DATABASE ege_russian_db;")
    # connect.commit()

def create_table():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    query = """CREATE TABLE users
                (
                    id text,
                    first_name text,
                    last_name text,
                    activity integer,
                    answer text,
                    task_number integer,
                    records text,
                    current_score text
                )"""
    cur.execute(query)
    connect.commit()
    print("Table users was created sucessfully")

def drop_table():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    drop_query = "DROP TABLE IF EXISTS users;"
    cur.execute(drop_query)
    connect.commit()
    print("Table was dropped sucessfully\n")

def nenavision():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    records = "10." * 25 + "10"
    cur.execute(f"UPDATE users SET records = '{records}' WHERE first_name = 'nenavision'")
    connect.commit()
    print("Nenavision up-up!\n")

def But():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
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
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    print("ПОЕХАЛИ")
    cur.execute(f"ALTER TABLE users ADD COLUMN right_ans integer NOT NULL DEFAULT 0;")
    connect.commit()
    cur.execute(f"ALTER TABLE users ADD COLUMN wrong_ans integer NOT NULL DEFAULT 0;")
    connect.commit()
    print("ДОБАВИЛОСЬ ВРОДЕ =)")

def delete():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    print("ПОЕХАЛИ")
    cur.execute(f"ALTER TABLE users DROP COLUMN `right`;")
    connect.commit()
    cur.execute(f"ALTER TABLE users DROP COLUMN `wrong`;")
    connect.commit()
    print("Удалилось ВРОДЕ =)")

def info():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users")
    info = cur.fetchall()
    print(len(info))
    for j in info:
        print(j)
    return

def stats():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
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
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
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
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users WHERE first_name = '🦋'")
    info = cur.fetchall()[0]
    fff = "30.30.30.30.30.30.30.30.30.30.30.30.30.30.31.30.30.30.30.31.30.30.30.30.30.29"
    cur.execute(f"UPDATE users SET records = '{fff}', current_score = '{fff}' WHERE first_name = '🦋'")
    connect.commit()
    print("HAIL")
  

def leaders():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT first_name, last_name, id, records FROM users")
    info = cur.fetchall()
    leader_board = [{} for _ in range(len(info))]
    for j in range(len(info)):
        leader_board[j]["first_name"] = info[j]["first_name"]
        leader_board[j]["last_name"] = info[j]["last_name"]
        leader_board[j]["id"] = info[j]["idss"]
        records = [int(x) for x in info[j]["records"].split(".")]
        leader_board[j]["score"] = min(records)
    leader_board.sort(key=lambda x: x["score"])
    num = 0
    for j in reversed(leader_board):
        num += 1
        if (num == 11):
            break
        print(num, j["id"])
        

def test_db():
    connect = pymysql.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _db_name
    )
    cur = connect.cursor(cursor_factory=RealDictCursor)
    _id = "1"
    first_name = "Русские буквы"
    last_name = "None"
    activity = 0
    task_number = 0
    answer = "-1"
    records = "0." * 25 + "0"
    current_score = "0." * 25 + "0"

    query = f"INSERT INTO users(id, first_name, last_name, activity, task_number, answer, records, current_score) VALUES('{_id}', '{first_name}', '{last_name}', '{activity}', '{task_number}', '{answer}', '{records}', '{current_score}')"
    cur.execute(query)
    connect.commit()

    query = f"SELECT * FROM users"
    cur.execute(query)
    result = cur.fetchall()
    pprint(result)

    query = f"DELETE FROM users WHERE id = '{_id}'"
    cur.execute(query)
    connect.commit()

    query = f"SELECT * FROM users WHERE id = 'test'"
    cur.execute(query)
    result = cur.fetchall()
    print(result)
    

# But()
# Jamboid()
# Aristarch_up()
# leaders()
print(f"Input\n1: create db\n2: create table\n3: drop table\n4: up-up nenavision\n5: add columns\n6: delete columns\n7: info\n8: stats\n9: Aristarch_up \n10: test")
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
    case 10:
        test_db()

