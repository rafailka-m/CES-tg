from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_keyboard():
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='Skapa biljett', callback_data='generate_ticket')
    button2 = InlineKeyboardButton(text='Aktiverade QR',
                                   callback_data='get_activated_qrs')
    button3 = InlineKeyboardButton(text='Totalt antal QR', callback_data='get_total_qrs')
    keyboard.add(button1, button2, button3)
    return keyboard
