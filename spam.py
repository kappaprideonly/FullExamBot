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
text = "Из-за самоуверенности и необдуманных действий база данных была повреждена, был сделан, так называемый, backup не первой свежести. Поэтому скорее всего все ваши сегодняшние действия были утеряны, а некоторых и вовсе нет в базе данных. Продлеваем конкурс до 14 апреля 23:59:59 МСК. Всем спасибо за внимание! Вернем последний /oversize в базу данных. Ваши сегодняшние текущие рекорды можем восстановить, если вы их скинете в личные сообщения скриншотом!"
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

