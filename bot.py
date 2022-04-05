import time
from aiogram import Bot, Dispatcher, executor, types
import pymysql
import os
from keyboard import get_keyboard, yes_no_back_to_tasks_keyboard, keyboard_no_yes, keyboard_no_yes_choose
from datawork import get_variant, check_answer
from aiogram.dispatcher.filters import Text

#так называемый препроцессинг
FAQ = ""
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
    with open(f"FAQ.txt", "r") as file:
        FAQ = file.read()
#print(full_info[25][0][1]) [26 номер] [1 вариант] [ответ]


TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = pymysql.connect(
        host='35.232.17.130',
        user='standart',
        password='1',
        database='ege_russian_db',
        cursorclass=pymysql.cursors.DictCursor)
cur = db.cursor()


@dp.callback_query_handler(Text(startswith="num_"))
async def callbacks_num(call: types.CallbackQuery):
    cur.execute(f"SELECT task_number FROM users WHERE id = '{call.from_user.id}'")
    current_task = cur.fetchall()[0]["task_number"]
    if current_task:
        text = f"😤 Вы в интерфейсе задания {current_task}!"
        await call.message.answer(text, parse_mode="html")
        await call.answer()
        return
    task_number = call.data[4:]
    text = f"😱 Вы выбрали номер задания {task_number}\nВсе команды меню работают с этим заданием!\nНачать тренировку по этому заданию!?"
    cur.execute(f"UPDATE users SET task_number = '{task_number}' WHERE id = '{call.from_user.id}'")
    db.commit()
    await call.message.answer(text, parse_mode="html", reply_markup=yes_no_back_to_tasks_keyboard())
    await call.answer()

@dp.callback_query_handler(text="back_to_tasks")
async def callbacks_back_to_tasks(call: types.CallbackQuery):
    
    cur.execute(f"SELECT activity FROM users WHERE id = '{call.from_user.id}'")
    if cur.fetchall()[0]["activity"]:
        text = f"🤨 Выполните задание!"
        await call.message.answer(text, parse_mode="html")
        await call.answer()
        return
    task_number = 0
    cur.execute(f"UPDATE users SET task_number = '{task_number}' WHERE id = '{call.from_user.id}'")
    db.commit()

    await call.message.answer("📝 Вы в меню", parse_mode="html", reply_markup=types.ReplyKeyboardRemove())
    text = "🤩 Выбери номер задания от 1 до 26, гигант"
    await call.message.answer(text, parse_mode="html", reply_markup=get_keyboard())
    await call.answer()


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

@dp.message_handler(commands="FAQ")
async def faq(message: types.Message):
    await message.answer(FAQ, parse_mode="html")

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
    cur.execute(f"UPDATE users SET activity = '{activity}', task_number = '{task_number}', answer = '{answer}' WHERE id = '{message.from_user.id}'")
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
        await message.answer("❌ Вы не выбрали задание!")
        return
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
        await message.answer("❌ Вы не выбрали задание!")
        return
    cur.execute("SELECT first_name, last_name, records FROM users")
    info = cur.fetchall()
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
        if (num == 11):
            break
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
        text = f"❌ Вас нет в базе данных! Нажмите на /start, {message.from_user.first_name}"
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
        if check_answer(message.text, answer):
            current_score += 1
            if current_score > score:
                score = current_score
            answer = ""
            text = f"✅ <b>Верно!</b> Желаете ли вы продолжить дальше?\n<b>score:{current_score}</b>"
            keyboard = keyboard_no_yes_choose()
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
            text = f"❌ <b>НЕВЕРНО! </b>\n👉Ответ: {answer}👈\nЖелаете ли вы начать заново?"
            keyboard = keyboard_no_yes_choose()
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






    elif message.text.lower() == "да" and task_number == 0:
        await message.answer("📝 Вы в меню", parse_mode="html", reply_markup=types.ReplyKeyboardRemove())
        text = "🤩 Выбери номер задания от 1 до 26"
        await message.answer(text, parse_mode="html", reply_markup=get_keyboard())





    elif task_number == 0 and any(message.text == str(x + 1) for x in range(26)):
        text = f"😱 Вы выбрали номер задания {message.text}\nВсе команды меню работают с этим заданием!\nНачать тренировку по этому заданию!?"
        task_number = message.text
        cur.execute(f"UPDATE users SET task_number = '{task_number}' WHERE id = '{message.from_user.id}'")
        db.commit()
        await message.answer(text, parse_mode="html", reply_markup=yes_no_back_to_tasks_keyboard())
    elif message.text.lower() == "да" and not activity:
        activity = 1
        text, answer = get_variant(task_number - 1, full_info)
        text = f"✍️ Задание № {task_number}\n" + text 
        cur.execute(f"UPDATE users SET activity = '{activity}', answer = '{answer}' WHERE id = '{message.from_user.id}'")
        db.commit()
        if (len(text) <= 4094):
            await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer(text[:len(text) // 2]) 
            await message.answer(text[len(text) // 2:])
    elif message.text.lower() == "нет":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key_start = types.InlineKeyboardButton(text='/start', callback_data='/start')
        keyboard.add(key_start)
        text = "😳 Хорошо, но задумайся над пословицей:\nШевели раньше <b>мозгами</b>, а то поплатишься <b>щеками</b>."
        await message.answer(text, parse_mode="html", reply_markup=keyboard)
    elif message.text.lower() == "выбрать другое задание":
        activity = 0
        task_number = 0
        answer = "-1"
        cur.execute(f"UPDATE users SET activity = '{activity}', task_number = '{task_number}', answer = '{answer}' WHERE id = '{message.from_user.id}'")
        db.commit()
        await message.answer("📝 Вы в меню", parse_mode="html", reply_markup=types.ReplyKeyboardRemove())
        text = "🤩 Выбери номер задания от 1 до 26"
        await message.answer(text, parse_mode="html", reply_markup=get_keyboard())
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

