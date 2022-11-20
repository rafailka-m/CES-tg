from aiogram import executor

from handler.delete import register_delete_handler
from handler.generate import register_generate_handler
from handler.position_date import register_pos_date_handler
from handler.statistic import register_statistic_handler
import middlewares
from settings.config import dp, logger_init


if __name__ == '__main__':
    logger_init()
    register_delete_handler(dp)
    register_generate_handler(dp)
    register_pos_date_handler(dp)
    register_statistic_handler(dp)
    executor.start_polling(dp, skip_updates=True)
