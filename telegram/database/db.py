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
                autocommit=True,
                init_command="SET SESSION time_zone='+00:00'"
            )
        except Exception as ex:
            logging.exception('SOMETHING WENT WRONG WHILE CONNECTING TO DB - %s' % ex)

    def check_code_exists(self, code: str) -> tuple:
        with self.conn.cursor() as cursor:
            cursor.execute(
                f'SELECT * FROM `club_qr_qrcodes` '
                'WHERE qr_code = %s',
                (code,)
            )
            return cursor.fetchone()

    def insert_code(self, name: str, surname: str, code: str, photo: str):
        with self.conn.cursor() as cursor:
            cursor.execute(
                f'INSERT INTO `club_qr_qrcodes` '
                '(name, surname, qr_code, photo, date_create, activated) '
                'VALUES (%s, %s, %s, %s, NOW(), true)',
                (name, surname, code, photo)
            )

    def get_qrs_count(self, *args) -> int:
        '''
        Gets total qr codes count
        :param args: `False, True` if you want total count.
        If you want total count of activated qr codes type `True, False`
        :return: total count
        '''
        sub_query = None
        if not args[0] and args[1]:
            sub_query = ''
        if args[0] and not args[1]:
            sub_query = ' WHERE activated = false'

        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM `club_qr_qrcodes`' + sub_query)
            result = cursor.fetchall()
            return len(result) if result else 0

    def delete_all_data(self):
        with self.conn.cursor() as cursor:
            cursor.execute('DELETE FROM `club_qr_qrcodes`')

    def change_position(self, position: str):
        with self.conn.cursor() as cursor:
            cursor.execute(
                'UPDATE `club_qr_posdate` SET `position` = %s',
                (position, )
            )

    def change_date(self, date: str):
        with self.conn.cursor() as cursor:
            cursor.execute(
                'UPDATE `club_qr_posdate` SET `date` = %s',
                (date, )
            )

    def get_position(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT `position` FROM `club_qr_posdate`')
            return cursor.fetchone()[0]

    def get_date(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT `date` FROM `club_qr_posdate`')
            return cursor.fetchone()[0]


db_obj = Database()
