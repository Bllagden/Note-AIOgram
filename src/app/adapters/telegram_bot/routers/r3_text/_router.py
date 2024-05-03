from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.utils.formatting import (
    Bold,
    HashTag,
    Text,
    as_key_value,
    as_list,
    as_marked_section,
)

router = Router()


# Если не указать фильтр F.text,
# то хэндлер сработает даже на картинку с подписью /italics


@router.message(F.text, Command("italics"))
async def italics_message_handler(message: Message) -> None:
    await message.answer("Hello, <i>world</i>!", parse_mode=ParseMode.HTML)
    await message.answer(r"Hello, _world_\!", parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text, Command("aiogram_text"))
async def aiogram_text_handler(message: Message) -> None:
    content = Text(
        "Hello, ",
        Bold(message.from_user.full_name),
    )
    await message.answer(**content.as_kwargs())


@router.message(F.text, Command("aiogram_as_list"))
async def adv_aiogram_text_handler(message: Message) -> None:
    content = as_list(
        as_marked_section(
            Bold("Success:"),
            "Test 1",
            "Test 3",
            "Test 4",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Failed:"),
            "Test 2",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("Summary:"),
            as_key_value("Total", 4),
            as_key_value("Success", 3),
            as_key_value("Failed", 1),
            marker="  ",
        ),
        HashTag("#test"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs())


@router.message(F.text, Command("settimer"))
async def settimer_handler(message: Message, command: CommandObject) -> None:
    if command.args is None:
        await message.answer("Ошибка: не переданы аргументы")
        return

    try:
        delay_time, text_to_send = command.args.split(" ", maxsplit=1)
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n/settimer <time> <message>",
        )
        return

    await message.answer(
        f"Таймер добавлен!\nВремя: {delay_time}\nТекст: {text_to_send}",
    )
