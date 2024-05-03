from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.adapters.telegram_bot.keyboards import contacts, github_, main_keyboard

router = Router()


@router.message(F.text, Command("menu"))
async def italics_message_handler(message: Message) -> None:
    await message.answer("Главное меню", reply_markup=main_keyboard.MARKUP)


@router.message(F.text.lower() == "btn1")
async def btn_1_handler(message: Message) -> None:
    await message.reply("Button 1")


@router.message(F.text.lower() == "btn2")
async def btn_2_handler(message: Message) -> None:
    await message.reply("Button 2")


@router.message(F.text.lower() == "btn3")
async def btn_3_handler(message: Message) -> None:
    await message.reply("Button 3")


@router.message(F.text.lower() == "links")
async def inline_btn_handler(message: Message) -> None:
    # await message.answer("Вот ваши ссылки:", reply_builder=github_.MARKUP)
    await message.answer(
        "Вот ваши ссылки:",
        reply_markup=github_.BUILDER.as_markup(),
    )


@router.message(Command("contacts"))
async def contacts_handler(message: Message) -> None:
    await message.answer(
        "Запрос контактов",
        reply_markup=contacts.BUILDER.as_markup(
            one_time_keyboard=True,
            resize_keyboard=True,
        ),
    )
