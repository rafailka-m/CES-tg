from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.emoji import emojize

from settings.config import STAFF


SWEDEN_FLAG = emojize(':flag_se:')
UK_FLAG = emojize(':gb:')


class AccessMiddleware(BaseMiddleware):

    async def pre_process_message(self,
                                  message: types.Message,
                                  dict):
        if message.from_user.id not in STAFF:
            await message.answer(
                f'{SWEDEN_FLAG} <b>Ingen åtkomst!</b>'
                f'{UK_FLAG} <b>No access!</b>'
            )
            raise CancelHandler()

    async def pre_process_callback_query(self,
                                  callback: types.CallbackQuery,
                                  dict):
        if callback.from_user.id not in STAFF:
            await callback.message.answer(
                f'{SWEDEN_FLAG} <b>Ingen åtkomst!</b>'
                f'{UK_FLAG} <b>No access!</b>'
            )
            await callback.answer()
            raise CancelHandler()
