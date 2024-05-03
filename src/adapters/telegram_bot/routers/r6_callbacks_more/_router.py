from contextlib import suppress

from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import Message

from adapters.telegram_bot.keyboards import fabnum_call

router = Router()
