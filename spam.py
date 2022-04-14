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
text = """

Конкурс завершился!!!!

🏆 Таблица лидеров по всем заданиям:

🥇 🦋 — 29 - 500р
🥈 Анастасия — 25 - 400р
🥉 The President — 20 - 300р
 4. Aristarch Samosski — 18
 5. Антон — 17
 6. Галия — 17
 7. Mortimer mortis — 14
 8. nenavision — 10
 9. оля — 7
 10. Vadim — 1

С призерами свяжемся в ближайшее время!
""" 
print(text)
input()
num = 0
for user in res:
    num += 1    
    try:
        bot.send_message(user["id"], text)
    except Exception:
        print("Blocked")
print(num)

