from aiogram import Bot, Dispatcher, executor, types
import os

KEY_TG = os.environ.get('KEY_TG')
bot = Bot(token=KEY_TG)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    text = "TEST"
    await message.answer(text)


@dp.message_handler()
async def go_something(message: types.Message):
    text = "TEST DO"
    await message.answer(text)


while True:
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        time.sleep(15)