from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from adapters.telegram_bot.keyboards import inline_links, main_keyboard

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
    await message.answer("Вот ваши ссылки:", reply_markup=inline_links.MARKUP)
