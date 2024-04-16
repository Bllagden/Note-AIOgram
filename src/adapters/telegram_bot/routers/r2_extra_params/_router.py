from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("extra_time"))
async def time_info_handler(message: Message, started_at: str) -> None:
    """started_at из dispatcher"""
    await message.answer(f"Время запуска бота по UTC: {started_at}")


@router.message(Command("extra_list_show"))
async def list_handler(message: Message, extra_list: list[int]) -> None:
    """extra_list из dispatcher.start_polling"""
    await message.answer(f"Список: {extra_list}")


@router.message(Command("extra_list_add"))
async def add_to_list_handler(message: Message, extra_list: list[int]) -> None:
    extra_list.append(7)
    await message.answer("В список добавлено число 7")
