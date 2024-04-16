from aiogram import Router, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    user_names = f"{html.quote(message.from_user.full_name)}"
    user_link = f"<a href='tg://user?id={message.from_user.id}'>{user_names}</a>"
    await message.answer(f"Hi {user_link}!", parse_mode=ParseMode.HTML)
