from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3 as sql
from config import TOKEN


bot = Bot(token = TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
@dp.message_handler(commands = "start")
async def cmd_start(message: types.Message):
    connect = sql.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER
    )""")

    connect.commit()
    
    user_id = message.chat.id
    cursor.execute(f"SELECT id FROM user WHERE id = {user_id}")
    data = cursor.fetchone()
    if data is None:
        user_data = [message.chat.id]
        cursor.execute("INSERT INTO user VALUES(?);", user_data)
        connect.commit()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
