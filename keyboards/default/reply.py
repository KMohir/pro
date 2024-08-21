from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db import db
from translation import _


def get_lang_for_button(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Texnik yordamga habar yozish",lang)
    )
            ],
            [
                KeyboardButton(text=_("Tilni o'zgartirish",lang))
            ],
            [
                KeyboardButton(text=_("ProTestim haqida bilish", lang))
            ],

        ],
        resize_keyboard=True
    )
    return button


# def get_project_for_user(message):
#     lang = db.get_lang(message.from_user.id)
#     button=ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=_("Protestim",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("2 chi proyekt",lang))
#             ],
#             [
#                 KeyboardButton(text=_("3 chi proyekt",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("4 chi proyekt",lang))
#             ],
#
#         ],
#         resize_keyboard=True
#     )
#     return button


def change_lang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Русский язык")

            ],
            [
                KeyboardButton(text="O'zbek tili")
            ],

        ],
        resize_keyboard=True
    )
    return button

def gender():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Erkak")

            ],
            [
                KeyboardButton(text="Ayol")
            ],

        ],
        resize_keyboard=True
    )
    return button



def country():
    button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Uzbekistan")],
            [KeyboardButton(text="Armenia")],
            [KeyboardButton(text="Azerbaijan")],
            [KeyboardButton(text="Belarus")],
            [KeyboardButton(text="Kazakhstan")],
            [KeyboardButton(text="Kyrgyzstan")],
            [KeyboardButton(text="Moldova")],
            [KeyboardButton(text="Russia")],
            [KeyboardButton(text="Tajikistan")],
            [KeyboardButton(text="Turkmenistan")],
            [KeyboardButton(text="Ukraine")]
        ],
        resize_keyboard=True
    )
    return button

def changelang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Tilni o'zgartirish")

            ],

        ],
        resize_keyboard=True
    )
    return button

def skip():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Skip")

            ],

        ],
        resize_keyboard=True
    )
    return button
def key(lang):
    if lang=='uz':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Kontakni yuborish",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
    elif lang=='ru':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Отправить контакт",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
    return keyboardcontakt