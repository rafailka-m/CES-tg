from aiogram import Dispatcher, types

from database.db import db_obj


async def delete_all_qr(callback: types.CallbackQuery):
    db_obj.delete_all_data()
    await callback.message.answer('<b>Successivt raderat</b>')


def register_delete_handler(dp: Dispatcher):
    dp.register_callback_query_handler(delete_all_qr, text='delete_all_qr')
