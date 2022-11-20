from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from database.db import db_obj


async def change_pos(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state('input_position')
    await callback.message.answer('Ange en ny plats')
    await callback.answer()


async def save_pos(message: types.Message, state: FSMContext):
    if len(message.text) > 35:
        await message.answer('Längden överstiger 35 tecken!')
        return
    db_obj.change_position(position=message.text)
    await message.answer('<b>Platsen har ändrats!</b>')
    await state.finish()


async def change_date(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state('input_date')
    await callback.message.answer('Ange datum i valfritt format')
    await callback.answer()


async def save_date(message: types.Message, state: FSMContext):
    if len(message.text) > 35:
        await message.answer('Längden överstiger 35 tecken!')
        return
    db_obj.change_date(date=message.text)
    await message.answer('<b>Datumet har ändrats!</b>')
    await state.finish()


def register_pos_date_handler(dp: Dispatcher):
    dp.register_callback_query_handler(change_pos, text='change_position')
    dp.register_message_handler(save_pos, state='input_pos')

    dp.register_callback_query_handler(change_date, text='change_date')
    dp.register_message_handler(save_date, state='input_date')
