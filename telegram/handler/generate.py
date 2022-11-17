from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from keyboard.keyboard import generate_keyboard
from objects.ticket import Ticket


async def start(message: types.Message):
    text = 'Hallå! ' \
           'Klicka på knappen nedan för att skapa en biljett.'
    keyboard = generate_keyboard()
    await message.answer(text, reply_markup=keyboard)


async def generate_ticket_info(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state('input_name')
    await callback.message.answer('Ange kundens för- och efternamn\n'
                                  '\n<b>Exempel:</b> Maria Andersson')


async def generate_ticket(message: types.Message, state: FSMContext):
    name, surname = message.text.split()
    ticket_obj = Ticket(name=name, surname=surname)

    photo = ticket_obj.ticket
    keyboard = generate_keyboard()
    await message.answer_photo(open(photo, 'rb'),
                               'Framgångsrikt genererat!',
                               reply_markup=keyboard)
    await state.finish()


def register_generate_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_callback_query_handler(generate_ticket_info, text='generate_ticket')
    dp.register_message_handler(generate_ticket, state='input_name')
