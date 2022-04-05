from aiogram import Bot, Dispatcher, executor, types
import random

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

def keyboard_no_yes_choose():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='Нет')
    key_choose = types.InlineKeyboardButton(text='Выбрать другое задание', callback_data='Выбрать другое задание')
    keyboard.add(key_yes, key_no, key_choose)
    return keyboard

# Генерация клавиатуры с заданиями
def get_keyboard():
    buttons = [
        types.InlineKeyboardButton(text=str(i), callback_data=("num_" + str(i))) for i in range(1, 27)
    ]
    buttons.append(types.InlineKeyboardButton(text="Похрен", callback_data=("num_" + str(random.randint(1, 27)))))
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard

# Клавиатура, возвращающая к выбору задания
def yes_no_back_to_tasks_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='Нет')
    key_back_to_tasks = types.InlineKeyboardButton(text='Выбрать другое задание', callback_data='Выбрать другое задание')
    keyboard.add(key_yes, key_no, key_back_to_tasks)
    return keyboard