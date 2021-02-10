from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback, setting_callback, confirmation_callback, type_work_callback
from data import config


def getSellWorkKeyboard(type_work):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data=setting_callback.new(command="exit", type="zero")),
            InlineKeyboardButton(text="Далее", callback_data=setting_callback.new(command="continue", type=type_work))
        ]
    ])


def getConfirmationKeyboard(**kwargs):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data=confirmation_callback.new(bool="Yes")),
            InlineKeyboardButton(text="Нет", callback_data=confirmation_callback.new(bool="No"))
        ]])
    for arg, text in kwargs.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=confirmation_callback.new(bool=arg)))
    return keyboard


def getCustomKeyboard(**kwargs):
    keyboard = InlineKeyboardMarkup()
    for arg, text in kwargs.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=confirmation_callback.new(bool=arg)))
    return keyboard


def getTypeWorkKeyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Курсовая работа", callback_data=type_work_callback.new(work="Курсовая")),
            InlineKeyboardButton(text="Дипломная работа", callback_data=type_work_callback.new(work="Дипломная"))
        ]
    ])
    keyboard.add(InlineKeyboardButton(text="Другие работы", callback_data=type_work_callback.new(work="other_works")))
    return keyboard


def getOtherWorks():
    keyboard = InlineKeyboardMarkup()
    for work in config.works:
        if work!="Курсовая" and work!="Дипломная":
            keyboard.add(
                InlineKeyboardButton(text=work, callback_data=type_work_callback.new(work=work)))
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data=type_work_callback.new(work="back")))
    return keyboard
