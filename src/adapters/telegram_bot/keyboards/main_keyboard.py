from aiogram.filters.callback_data import CallbackData
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

MARKUP = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Btn1"), KeyboardButton(text="Btn2")],
        [KeyboardButton(text="Btn3")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True,
)
