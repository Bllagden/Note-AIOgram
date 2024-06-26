import contextlib
from collections.abc import AsyncIterator, Sequence
from datetime import UTC, datetime

from aiogram import Bot, Dispatcher, Router
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.types import BotCommand
from aioinject import Container
from aioinject.ext.aiogram import AioInjectMiddleware

from app.di import create_container
from app.settings import TelegramBotSettings
from lib.settings import get_settings

from .middleware import SomeMiddleware
from .routers import (
    echo,
    r1_reply,
    r2_extra_params,
    r3_text,
    r4_keyboards,
    r5_callbacks,
    r6_callbacks_more,
    start,
)

MAIN_ROUTERS: Sequence[Router] = [
    start.router,
    r1_reply.router,
    r2_extra_params.router,
    r3_text.router,
    r4_keyboards.router,
    r5_callbacks.router,
    r6_callbacks_more.router,
    echo.router,
]


def _configure_middlewares(core_router: Router, container: Container) -> None:
    core_router.message.outer_middleware.register(AioInjectMiddleware(container))
    core_router.callback_query.outer_middleware.register(AioInjectMiddleware(container))

    core_router.message.outer_middleware.register(SomeMiddleware())
    core_router.callback_query.outer_middleware.register(SomeMiddleware())


def _register_routes(core_router: Router, routers: Sequence[Router]) -> None:
    for router in routers:
        core_router.include_router(router)


@contextlib.asynccontextmanager
async def create_bot() -> AsyncIterator[Bot]:
    """token=settings.token.get_secret_value()"""
    settings = get_settings(TelegramBotSettings)
    async with AiohttpSession() as session:
        yield Bot(token=settings.token, session=session)  # parse_mode=ParseMode.HTML


async def main_bot() -> None:
    # logging.basicConfig(level=logging.DEBUG)

    main_router = Router()
    container = create_container()

    _configure_middlewares(main_router, container)
    _register_routes(main_router, MAIN_ROUTERS)

    dispatcher = Dispatcher()
    dispatcher.include_router(main_router)
    dispatcher["started_at"] = datetime.now(tz=UTC).strftime("%Y-%m-%d, %H:%M")

    async with create_bot() as bot:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(
            commands=[
                BotCommand(command="start", description="Старт"),
                BotCommand(command="reply", description="Ответить"),
                BotCommand(command="r", description="Сокращение от '/reply'"),
                BotCommand(command="dice", description="Ответить кубиком"),
                BotCommand(command="dice_bot", description="Написать кубиком"),
                BotCommand(command="extra_time", description="Время запуска"),
                BotCommand(command="extra_list_show", description="Список"),
                BotCommand(command="extra_list_add", description="Добавить в список"),
                BotCommand(command="italics", description="Курсив"),
                BotCommand(command="aiogram_text", description="Text()"),
                BotCommand(command="aiogram_as_list", description="as_list()"),
                BotCommand(command="settimer", description="команда с аргументами"),
                BotCommand(command="menu", description="Меню"),
                BotCommand(command="contacts", description="Контакты"),
                BotCommand(command="random", description="Рандом_call"),
            ],
        )
        await dispatcher.start_polling(bot, extra_list=[1, 2, 3])
