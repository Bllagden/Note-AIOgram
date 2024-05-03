from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from adapters.telegram_bot.callbacks import NumbersCallback

CHANGE_1_BUTTON = InlineKeyboardButton(
    text="-2",
    callback_data=NumbersCallback(action="change", value=-2).pack(),
)
CHANGE_2_BUTTON = InlineKeyboardButton(
    text="-1",
    callback_data=NumbersCallback(action="change", value=-1).pack(),
)
CHANGE_3_BUTTON = InlineKeyboardButton(
    text="1",
    callback_data=NumbersCallback(action="change", value=1).pack(),
)
CHANGE_4_BUTTON = InlineKeyboardButton(
    text="2",
    callback_data=NumbersCallback(action="change", value=2).pack(),
)
FINISH_BUTTON = InlineKeyboardButton(
    text="Подтвердить",
    callback_data=NumbersCallback(action="finish").pack(),
)

BUILDER = InlineKeyboardBuilder(
    markup=[
        [
            CHANGE_1_BUTTON,
            CHANGE_2_BUTTON,
            CHANGE_3_BUTTON,
            CHANGE_4_BUTTON,
        ],
        [
            FINISH_BUTTON,
        ],
    ],
)


def get_keyboard_fab() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="-2",
        callback_data=NumbersCallback(action="change", value=-2),
    )
    builder.button(
        text="-1",
        callback_data=NumbersCallback(action="change", value=-1),
    )
    builder.button(
        text="+1",
        callback_data=NumbersCallback(action="change", value=1),
    )
    builder.button(
        text="+2",
        callback_data=NumbersCallback(action="change", value=2),
    )
    builder.button(
        text="Подтвердить",
        callback_data=NumbersCallback(action="finish"),
    )
    # Выравниваем кнопки по 4 в ряд, чтобы получилось 4 + 1
    builder.adjust(4)
    return builder.as_markup()
