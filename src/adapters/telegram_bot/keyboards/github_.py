from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

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
