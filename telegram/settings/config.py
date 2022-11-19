import logging
import os
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import cloudinary


# Cloudinary config
cloudinary.config(
    cloud_name = os.getenv('CLOUD_NAME'),
    api_key = os.getenv('CLOUD_KEY'),
    api_secret = os.getenv('CLOUD_SECRET')
)


# Telegram config
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


# Database config
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')


# Website config
QR_PATH = input('Type here full path to qr page (including "/" in the end): ')
GEO_STR = 'Vretensborgsvägen 5 Hägersten'
DATE_STR = 'Februari 26, 2023'
QR_X, QR_Y = 1111, 88
GEO_X = 118
GEO_Y = 252
DATE_X = 118
DATE_Y = 376
NAME_X = 118
NAME_Y = 314


# Logger config
def logger_init():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatterError = logging.Formatter(
        "[%(asctime)s] - [%(levelname)s] - [%(name)s(%(filename)s) - %(funcName)s%(lineno)d] "
        "- %(message)s\n[%(processName)s:%(process)d] [%(threadName)s:%(thread)d] - %("
        "pathname)s\n"
    )
    formatter = logging.Formatter("[%(asctime)s] - [%(levelname)s] -->  %(message)s")

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler_debug = logging.FileHandler("logs/debug.log")
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_debug.setFormatter(formatter)

    file_handler_warning = logging.FileHandler("logs/warning.log")
    file_handler_warning.setLevel(logging.WARNING)
    file_handler_warning.setFormatter(formatterError)

    file_handler_errors = logging.FileHandler("logs/error.log")
    file_handler_errors.setLevel(logging.ERROR)
    file_handler_errors.setFormatter(formatterError)

    file_handler_info = logging.FileHandler("logs/info.log")
    file_handler_info.setLevel(logging.INFO)
    file_handler_info.setFormatter(formatter)

    file_handler_warn = logging.FileHandler("logs/warn.log")
    file_handler_warn.setLevel(logging.WARN)
    file_handler_warn.setFormatter(formatter)

    file_handler_critical = logging.FileHandler("logs/critical.log")
    file_handler_critical.setLevel(logging.CRITICAL)
    file_handler_critical.setFormatter(formatterError)

    file_handler_fatal = logging.FileHandler("logs/fatal.log")
    file_handler_fatal.setLevel(logging.FATAL)
    file_handler_fatal.setFormatter(formatterError)

    logger.addHandler(file_handler_debug)
    logger.addHandler(file_handler_warning)
    logger.addHandler(file_handler_errors)
    logger.addHandler(file_handler_info)
    logger.addHandler(file_handler_warn)
    logger.addHandler(file_handler_critical)
    logger.addHandler(file_handler_fatal)
    logger.addHandler(stdout_handler)
    dp.middleware.setup(LoggingMiddleware())
