from random import randint

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import Message

from app.adapters.telegram_bot.keyboards import random_call

router = Router()


@router.message(Command("random"))
async def random_handler(message: Message) -> None:
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=random_call.BUILDER.as_markup(),
    )


@router.callback_query(F.data == "random_value")
async def random_callback(callback: CallbackQuery) -> None:
    await callback.message.answer(str(randint(1, 10)))  # noqa: S311
    await callback.answer()
    # await callback.answer(
    #     text="Спасибо, что воспользовались ботом!",
    #     show_alert=True,
    # )
