from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BUTTONS = [
    InlineKeyboardButton(text='Skapa biljett', callback_data='generate_ticket'),
    InlineKeyboardButton(text='Aktiverade QR', callback_data='get_activated_qrs'),
    InlineKeyboardButton(text='Totalt antal QR', callback_data='get_total_qrs'),
    InlineKeyboardButton(text='Radera alla QR', callback_data='delete_all_qr'),
    InlineKeyboardButton(text='Ändra ett datum', callback_data='change_date'),
    InlineKeyboardButton(text='Ändra en plats', callback_data='change_position')
]


def generate_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(BUTTONS[0], BUTTONS[3])
    keyboard.row(BUTTONS[1], BUTTONS[2])
    keyboard.row(BUTTONS[-2], BUTTONS[-1])
    return keyboard
