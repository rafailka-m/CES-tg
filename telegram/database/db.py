import logging

import pymysql

from settings import config


class Database:

    def __init__(self):
        try:
            self.conn = pymysql.connect(
                user=config.DB_USERNAME,
                password=config.DB_PASSWORD,
                database=config.DB_NAME,
                host=config.DB_HOST,
                autocommit=True
            )
        except Exception as ex:
            logging.exception('SOMETHING WENT WRONG WHILE CONNECTIG TO DB - %s' % ex)

    def check_code_exists(self, code: str) -> tuple:
        with self.conn.cursor() as cursor:
            cursor.execute(
                f'SELECT * FROM "club_qr_qrcodes" '
                'WHERE "qr_code" = %s',
                (code,)
            )
            return cursor.fetchone()

    def insert_code(self, name: str, surname: str, code: str, photo: str):
        with self.conn.cursor() as cursor:
            cursor.execute(
                f'INSERT INTO "club_qr_qrcodes" '
                '(name, surname, qr_code, photo, date_create, activated) '
                'VALUES (%s, %s, %s, %s, NOW(), true)',
                (name, surname, code, photo)
            )


db_obj = Database()
