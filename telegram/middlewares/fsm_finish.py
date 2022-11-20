from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from settings.config import dp


class FinishStateMiddleware(BaseMiddleware):

    async def on_pre_process_callback_query(self,
                                            callback: types.CallbackQuery,
                                            data: dict):
        state = dp.current_state(chat=callback.from_user.id,
                                 user=callback.from_user.id)
        await callback.answer()
        if state:
            await state.finish()

