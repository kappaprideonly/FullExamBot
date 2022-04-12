from telebot import types
import telebot
import pymysql
token = input("TOKEN: ")



bot = telebot.TeleBot(token)
db = pymysql.connect(
        host='35.232.17.130',
        user='standart',
        password='1',
        database='ege_russian_db',
        cursorclass=pymysql.cursors.DictCursor)
cur = db.cursor()


cur.execute("SELECT id FROM users")
res = cur.fetchall()
text = "/stats /users"
num = 0
print(text)
input()
for user in res:
    num += 1    
    try:
        bot.send_message(user["id"], text)
    except Exception:
        print("Blocked")
print(num)

