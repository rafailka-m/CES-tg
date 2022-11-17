import logging
import os.path
import random
import string

from cloudinary import uploader
from PIL import Image, ImageFont, ImageDraw
from qrcode import QRCode

from database.db import db_obj
from settings import config


symbols = [string.ascii_letters, string.digits]


class Ticket:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.code = ''
        self.ticket = os.path.abspath('media/tickets/')
        self.qr = os.path.abspath('media/qr/')
        self._generate_ticket_image()

    def _upload_to_cloud(self):
        uploader.upload(self.qr, folder='media')

    def _generate_code(self):
        while True:
            for _ in range(32):
                self.code += random.choice(random.choice(symbols))

            if not db_obj.check_code_exists(self.code):
                break

    def _generate_qr_image(self):
        self._generate_code()

        qr = QRCode(version=1, box_size=8)
        qr.add_data(f'{config.QR_PATH}{self.code}')
        qr.make()

        qr_img = qr.make_image(fill_color='white', back_color='black')
        qr_img.save(f'media/qr/{self.code}.png')
        self.qr += f'/{self.code}.png'
        self._upload_to_cloud()
        db_obj.insert_code(name=self.name,
                           surname=self.surname,
                           code=self.code,
                           photo=f'{self.code}.png')

    def _generate_ticket_image(self):
        self._generate_qr_image()
        template_path = os.path.abspath('img/ticket_template.png')
        template = Image.open(template_path)

        font_path = os.path.abspath('font/DejaVuSansMono.ttf')
        font = ImageFont.truetype(font_path, 37)

        text_name = f'{self.name} {self.surname}'
        editable_template = ImageDraw.Draw(template)
        qr = Image.open(self.qr)

        set_dict = {0: [config.NAME_X, config.NAME_Y, text_name],
                    1: [config.DATE_X, config.DATE_Y, config.DATE_STR],
                    2: [config.GEO_X, config.GEO_Y, config.GEO_STR]}
        for value in set_dict.values():
            editable_template.text(
                (value[0], value[1]),
                value[2],
                'white',
                font
            )

        template.paste(qr, (config.QR_X, config.QR_Y))
        self.ticket += f'/{self.code}.png'
        template.save(self.ticket)
        logging.info(f'{self} GENERATED SUCCESSFULLY')

    def __repr__(self):
        return f'{self.__class__}: {self.code}'
