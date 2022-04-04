from aiogram import Bot, Dispatcher, executor, types
import pymysql
import random
import os
from keyboard import keyboard_answer, keyboard_no_yes
#from pprint import pprint


#так называемый препроцессинг
full_info = [[] for _ in range(26)]
for i in range(26):
    with open(f"data/task_{i + 1}.txt", "r") as file:
        f = file.read()
    for j in f.split("&\n"):
        if (len(j) < 2):
            continue
        info = j.split("#\n")
        text = info[0].strip()
        answer = info[1].strip()
        full_info[i].append([text, answer])
#print(full_info[25][0][1]) 26 номер 1 вариант ответ



token = os.environ.get('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)
db = pymysql.connect(
        host='35.232.17.130',
        user='standart',
        password='1',
        database='ege_russian_db',
        cursorclass=pymysql.cursors.DictCursor)
cur = db.cursor()

# query = """CREATE TABLE users
#                 (
#                     id text,
#                     first_name text,
#                     last_name text,
#                     activity integer,
#                     task_number integer,
#                     records MEDIUMTEXT,
#                     current_score MEDIUMTEXT
#                 )"""


def find_in_data(id_user):
    cur.execute(f"SELECT * FROM users WHERE id = '{id_user}'")
    res = cur.fetchall()
    return res != ()

@dp.message_handler(commands="start")
async def start(message: types.Message):
    if not find_in_data(message.from_user.id):
        id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        activity = 0
        task_number = 0
        answer = "-1"
        records = "0." * 25 + "0"
        current_score = "0." * 25 + "0"
        query = f"INSERT INTO users(id, first_name, last_name, activity, task_number, answer, records, current_score) VALUES('{id}', '{first_name}', '{last_name}', '{activity}', '{task_number}', '{answer}', '{records}', '{current_score}')"
        cur.execute(query)
        db.commit()
    activity = 0
    task_number = 0
    answer = "-1"
    cur.execute(f"UPDATE users SET activity = '{activity}', current_score = '{current_score}', task_number = '{task_number}', answer = '{answer}' WHERE id = '{message.from_user.id}'")
    db.commit()
    text = f"🖐🏾 Привет, <b>{message.from_user.first_name}</b>.\nНачать тренировку?"
    keyboard = keyboard_no_yes()
    await message.answer(text, parse_mode="html", reply_markup=keyboard)


@dp.message_handler(commands="record")
async def record(message: types.Message):
    if not find_in_data(str(message.from_user.id)):
        text = f"Вас нет в базе данных! Нажмите на /start, {message.from_user.id.first_name}"
        await message.answer(text, parse_mode="html")
        return
    cur.execute(f"SELECT task_number, records FROM users WHERE id = '{message.from_user.id}'")
    info = cur.fetchall()[0]
    task_number = info["task_number"]
    records = info["records"]
    if task_number == 0:
        await message.answer("Вы не выбрали задание!")
    record = records.split(".")[task_number - 1]
    text = f"🏋🏿‍♀️ Ваш рекорд в задании № {task_number}: {record}"
    await message.answer(text, parse_mode="html")


@dp.message_handler(commands="users")
async def users(message: types.Message):
    cur.execute("SELECT * FROM users")
    res = cur.fetchall()
    text = f"📊 Количество пользователей: {len(res)}"
    await message.answer(text, parse_mode="html")


@dp.message_handler(commands="update")
async def update(message: types.Message):
    cur.execute(f"UPDATE users SET first_name = '{message.from_user.first_name}', last_name = '{message.from_user.last_name}' WHERE id = '{message.from_user.id}'")
    db.commit()
    text = f"😉 Имя пользователя обновлено!"
    await message.answer(text, parse_mode="html")


@dp.message_handler(commands="leaderboard")
async def leaderboard(message: types.Message):
    cur.execute(f"SELECT task_number FROM users WHERE id = '{message.from_user.id}'")
    task_number = cur.fetchall()[0]["task_number"]
    if (task_number == 0):
        await message.answer("Вы не выбрали задание!")
    cur.execute("SELECT first_name, last_name, records FROM users")
    info = cur.fetchmany(10)
    leader_board = [{} for _ in range(len(info))]
    for j in range(len(info)):
        leader_board[j]["first_name"] = info[j]["first_name"]
        leader_board[j]["last_name"] = info[j]["last_name"]
        leader_board[j]["score"] = int(info[j]["records"].split(".")[task_number - 1])
    leader_board.sort(key=lambda x: x["score"])
    text = f"🏆 Таблица лидеров по заданию {task_number}:\n\n"
    num = 0
    for j in reversed(leader_board):
        num += 1
        first_name = j["first_name"]
        last_name = j["last_name"]
        score = j["score"]
        if num == 1:
            text += "🥇 "
        elif num == 2:
            text += "🥈 "
        elif num == 3:
            text += "🥉 "
        else:
            text += f" {num}. "
        if last_name != 'None':
            text += f"{first_name} {last_name} — {score}\n"
        else:
            text += f"{first_name} — {score}\n"
    await message.answer(text, parse_mode="html")

@dp.message_handler()
async def training(message: types.Message):
    if not find_in_data(str(message.from_user.id)):
        text = f"Вас нет в базе данных! Нажмите на /start, {message.from_user.first_name}"
        await message.answer(text, parse_mode="html")
        return
    cur.execute(f"SELECT activity, task_number FROM users WHERE id = '{message.from_user.id}'")
    info = cur.fetchall()[0]
    activity = info["activity"]
    task_number = info["task_number"]
    if activity:
        activity = 0
        user_id = message.from_user.id

        cur.execute(f"SELECT answer, current_score, records, task_number FROM users WHERE id = '{user_id}'")
        info = cur.fetchall()[0]
        task_number = info["task_number"]
        answer = info["answer"]
        current_score = int(info["current_score"].split(".")[task_number - 1])
        score = int(info["records"].split(".")[task_number - 1])
        if message.text == answer:
            current_score += 1
            if current_score > score:
                score = current_score
            answer = ""
            text = f"✅ <b>Верно!</b> Желаете ли вы продолжить дальше?\n<b>score:{current_score}</b>"
            keyboard = keyboard_no_yes()
            records = info["records"].split(".")
            records[task_number - 1] = str(score)
            records = ".".join(records)
            current_scores = info["current_score"].split(".")
            current_scores[task_number - 1] = str(current_score)
            current_scores = ".".join(current_scores)
            cur.execute(f"UPDATE users SET activity = '{activity}', answer = '{answer}', current_score = '{current_scores}', records = '{records}' WHERE id = '{message.from_user.id}'")
            db.commit()
            await message.answer(text, parse_mode="html", reply_markup=keyboard)
        else:
            if current_score > score:
                score = current_score
            current_score = 0
            text = f"❌ <b>НЕВЕРНО! </b>\n Желаете ли вы начать заново?"
            keyboard = keyboard_no_yes()
            answer = ""
            records = info["records"].split(".")
            records[task_number - 1] = str(score)
            records = ".".join(records)
            current_scores = info["current_score"].split(".")
            current_scores[task_number - 1] = str(current_score)
            current_scores = ".".join(current_scores)
            cur.execute(f"UPDATE users SET activity = '{activity}', answer = '{answer}', current_score = '{current_scores}', records = '{records}' WHERE id = '{message.from_user.id}'")
            db.commit()
            await message.answer(text, parse_mode="html", reply_markup=keyboard)
    elif message.text == "Да" and task_number == 0:
        text = "🤩 Выбери номер задания от 1 до 26"
        await message.answer(text, parse_mode="html")
    elif task_number == 0 and any(message.text == str(x + 1) for x in range(26)):
        text = f"😱 Вы выбрали номер задания {message.text}\nВсе команды меню работают с этим заданием!\nНачать тренировку по этому заданию!?"
        task_number = message.text
        cur.execute(f"UPDATE users SET task_number = '{task_number}' WHERE id = '{message.from_user.id}'")
        db.commit()
        await message.answer(text, parse_mode="html")
    elif message.text == "Да" or message.text == "Далее" and not activity:
        activity = 1
        text, answer = get_variant(task_number - 1)
        cur.execute(f"UPDATE users SET activity = '{activity}', answer = '{answer}' WHERE id = '{message.from_user.id}'")
        db.commit()
        await message.answer(text, parse_mode="html")
    elif message.text == "Нет":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key_start = types.InlineKeyboardButton(text='/start', callback_data='/start')
        keyboard.add(key_start)
        text = "😳 Хорошо, но задумайся над пословицей:\nШевели раньше <b>мозгами</b>, а то поплатишься <b>щеками</b>."
        await message.answer(text, parse_mode="html", reply_markup=keyboard)
    else:
        await message.answer(
                         f"😡 Я тебя не понимаю, дружище. Соберитесь, <b>{message.from_user.first_name}</b>",
                         parse_mode="html")

while True:
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        time.sleep(15)
db.close()
