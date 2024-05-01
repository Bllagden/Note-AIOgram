from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

MARKUP = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="GitHub", url="https://github.com/Bllagden"),
            # InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=..."),
        ],
    ],
)
#####################################################################################

GITHUB_BUTTON = InlineKeyboardButton(
    text="GitHub",
    url="https://github.com/Bllagden",
)


BUILDER = InlineKeyboardBuilder(
    markup=[
        [GITHUB_BUTTON],
    ],
)
