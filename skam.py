import pymysql
import time


with open("id_nenavision.txt") as file:
    id_f = file.readline().strip()

db = pymysql.connect(
        host='35.232.17.130',
        user='standart',
        password='1',
        database='ege_russian_db',
        cursorclass=pymysql.cursors.DictCursor)
cur = db.cursor()

current_task = 0

while True:
    cur.execute(f"SELECT * FROM users WHERE id = '{id_f}'")
    info = cur.fetchall()[0]
    input()
    records = info["records"].split(".")
    print(records)
    if (records[25] == '32'):
        break
    if (records[current_task] == "32"):
        current_task += 1
    time.sleep(23)
    records[current_task] = str(int(records[current_task]) + 1)
    records = ".".join(records)
    cur.execute(f"UPDATE users SET records = '{records}' WHERE id = {id_f}")
    db.commit()
