from datetime import UTC, datetime

from aiogram import F, Router, html
from aiogram.enums import ParseMode
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def echo_with_time_handler(message: Message) -> None:
    time_now = datetime.now(tz=UTC).strftime("%H:%M")
    added_text = html.underline(f"Команда не распознана\nСоздано по UTC в {time_now}")
    await message.answer(f"{message.text}\n\n{added_text}", parse_mode=ParseMode.HTML)
