import pymysql



try:
    db = pymysql.connect(
        host='35.232.17.130',
        user='standart',
        password='1',
        database='bot_ege',
        cursorclass=pymysql.cursors.DictCursor)
    cur = db.cursor()
    # cur.execute("""CREATE TABLE users_info4 (
    #     id text,
    #     score integer,
    #     temp integer,
    #     num integer,
    #     activity integer,
    #     first_name text,
    #     last_name text
    # )""")
    id_user = 'test'
    score = 0
    temp = 0
    num = 0
    activity = 0
    first_name = "zavupach"
    last_name = "something"
    #cur.execute(f"INSERT INTO users_info4 (id, score, temp, num, activity, first_name, last_name) VALUES ('{id_user}', '{score}', '{temp}', '{num}', '{activity}', '{first_name}', '{last_name}')")
    cur.execute("SELECT * FROM users_info4")
    print(cur.fetchall())
    #cur.execute("SELECT * FROM users_info4 WHERE id = '138783508'")
    #cur.execute("DELETE FROM users_info4 WHERE id = '1387835083'")
    db.commit()
    cur.execute("SELECT * FROM users_info4 WHERE id = '1387835083'")
    cur.execute("SELECT score FROM users_info4 WHERE id = 'test'")
    print(cur.fetchall()[0]["score"])
    db.commit()
    db.close()

except Exception as e:
    print("Что-то пошло не так!")
    print(e)

