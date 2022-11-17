from aiogram import Dispatcher, types

from database.db import db_obj


async def get_total_qrs(callback: types.CallbackQuery):
    total_qrs = db_obj.get_qrs_count(False, True)
    await callback.message.answer(f'Totalt antal QR-koder: <b>{total_qrs}</b>')
    await callback.answer()


async def get_total_activated_qrs(callback: types.CallbackQuery):
    total_qrs = db_obj.get_qrs_count(True, False)
    await callback.message.answer('Totalt antal aktiverade '
                                  f'QR-koder: <b>{total_qrs}</b>')
    await callback.answer()


def register_statistic_handler(dp: Dispatcher):
    dp.register_callback_query_handler(get_total_qrs, text='get_total_qrs')
    dp.register_callback_query_handler(
        get_total_activated_qrs,
        text='get_activated_qrs'
    )
