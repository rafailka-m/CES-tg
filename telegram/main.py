from aiogram import executor

from handler.handler import register_handler
from settings.config import dp, logger_init


if __name__ == '__main__':
    logger_init()
    register_handler(dp)
    executor.start_polling(dp, skip_updates=True)
