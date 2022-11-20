from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from emoji import emojize

from settings.config import STAFF


SWEDEN_FLAG = emojize(':Sweden:')
UK_FLAG = emojize(':United_Kingdom:')


class AccessMiddleware(BaseMiddleware):

    async def on_pre_process_message(self,
                                     message: types.Message,
                                     data: dict):
        if message.from_user.id not in STAFF:
            await message.answer(
                f'{SWEDEN_FLAG} <b>Ingen åtkomst!</b>\n'
                f'{UK_FLAG} <b>No access!</b>'
            )
            raise CancelHandler()

    async def on_pre_process_callback_query(self,
                                            callback: types.CallbackQuery,
                                            data: dict):
        if callback.from_user.id not in STAFF:
            await callback.message.answer(
                f'{SWEDEN_FLAG} <b>Ingen åtkomst!</b>\n'
                f'{UK_FLAG} <b>No access!</b>'
            )
            await callback.answer()
            raise CancelHandler()
