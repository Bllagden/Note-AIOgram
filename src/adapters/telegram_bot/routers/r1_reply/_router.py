from aiogram import Bot, Router
from aiogram.enums import DiceEmoji
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=["reply", "r"]))
async def reply_handler(message: Message) -> None:
    await message.reply("Ответить в текушем чате")


@router.message(Command("dice"))
async def dice_handler(message: Message) -> None:
    await message.reply_dice(emoji="🎲")


@router.message(Command("dice_bot"))
async def dice_bot_handler(message: Message, bot: Bot) -> None:
    """Написать в выбранном чате"""
    await bot.send_dice(message.chat.id, emoji=DiceEmoji.DICE)
