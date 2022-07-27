# from telebot import types
import telebot
import psycopg2 as pymysql
from psycopg2.extras import RealDictCursor
from config import password, host, user, port
token = input("TOKEN: ")



bot = telebot.TeleBot(token)
db = pymysql.connect(
        host='35.232.17.130',
        user='standart',
        password='1',
        database='ege_russian_db',
    )
cur = db.cursor(cursor_factory=RealDictCursor)


cur.execute("SELECT id, first_name FROM users")
res = cur.fetchall()
text = "Поздравляю с победой! Напиши кодовое слово 'JamboTea' в личные сообщения @Markit125"
num = 0
print(text)
input()
num = 0
# for user in res:
#     num += 1    
#     try:
#         # if user["id"] == "5171198119":
#         if user["id"] == "595859649" or user["id"] == "908509325":
#             print(user["first_name"])
#             bot.send_message(user["id"], text)
#             print("gig")
#     except Exception:
#         print("Blocked")
# print(num)

