from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder

CONTACTS_GEO_BUTTON = KeyboardButton(
    text="Запросить геолокацию",
    request_location=True,
)

CONTACTS_NUM_BUTTON = KeyboardButton(
    text="Запросить контакт",
    request_contact=True,
)

# Кнопки в строчку
BUILDER = ReplyKeyboardBuilder(
    markup=[
        [
            CONTACTS_GEO_BUTTON,
            CONTACTS_NUM_BUTTON,
        ],
    ],
)

# Кнопки в столбик
BUILDER2 = ReplyKeyboardBuilder(
    markup=[
        [CONTACTS_GEO_BUTTON],
        [CONTACTS_NUM_BUTTON],
    ],
)
