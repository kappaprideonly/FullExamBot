
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked
import aiogram.utils.markdown as fmt
import pymysql as sql
from config import TOKEN


bot = Bot(token = TOKEN, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)

db = sql.connect(
    host = "35.232.17.130",
    user = "standart",
    database = "ege_russian_db",
    passwd = "1"
)
cur = db.cursor()

def find_in_data(id_user):
    print("find in data begins\n")
    cur.execute(f"SELECT * FROM users WHERE id = '{id_user}'")
    res = cur.fetchall()
    print("find in data ends\n")
    return res != ()

# START
@dp.message_handler(commands = "start")
async def cmd_start(message: types.Message):
    if not find_in_data(message.from_user.id):
        id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        activity = 0
        task_number = 0
        records = "0." * 25 + "0"
        current_score = "0." * 25 + "0"
        query = f"INSERT INTO users(id, first_name, last_name, activity, task_number, records, current_score) VALUES('{id}', '{first_name}', '{last_name}', '{activity}', '{task_number}', '{records}', '{current_score}')"
        cur.execute(query)
        db.commit()
    

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    buttons = ["Описание заданий", "Выбрать задание"]
    keyboard.add(*buttons)
    await message.answer("*Приветствие*", reply_markup = keyboard)
    # res = "SELECT * FROM users"
    # cur.execute(res)
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)


# Декларирование заданий
@dp.message_handler(lambda message: message.text == "Описание заданий")
async def description(message: types.Message):
    await message.answer("Всего 26 заданий в первой части!")


@dp.message_handler(lambda message: message.text == "Выбрать задание")
async def return_tasks(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    buttons = [str(i + 1) for i in range(8, 12)]
    keyboard.add(*buttons)
    await message.answer("Выберите задание", reply_markup = keyboard)


@dp.message_handler(commands = "9")
async def cmd_test2(message: types.Message):

    await message.answer("")


# @dp.message_handler(commands = "test2")
# async def cmd_test2(message: types.Message):
#     await message.answer(
#         fmt.text(
#             fmt.text(fmt.hunderline("GIANT")," - is", fmt.hstrikethrough("gant"), " giambo"), 
#             sep = '\n'
#         )
#     )



@dp.errors_handler(exception = BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
