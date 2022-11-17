from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_keyboard():
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Skapa biljett', callback_data='generate_ticket')
    keyboard.add(button)
    return keyboard
