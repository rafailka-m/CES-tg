from aiogram import executor

from handler.generate import register_generate_handler
from handler.statistic import register_statistic_handler
from settings.config import dp, logger_init


if __name__ == '__main__':
    logger_init()
    register_generate_handler(dp)
    register_statistic_handler(dp)
    executor.start_polling(dp, skip_updates=True)
