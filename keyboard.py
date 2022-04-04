from aiogram import Bot, Dispatcher, executor, types

def keyboard_no_yes():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='Нет')
    keyboard.add(key_yes, key_no)
    return keyboard

def keyboard_answer():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    key_1 = types.InlineKeyboardButton(text='1', callback_data='1')
    key_2 = types.InlineKeyboardButton(text='2', callback_data='2')
    keyboard.add(key_1, key_2)
    key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
    key_4 = types.InlineKeyboardButton(text='4', callback_data='4')
    keyboard.add(key_3, key_4)
    return keyboard