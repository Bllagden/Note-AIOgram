import functools
import itertools
from collections.abc import Iterable

import aioinject
from pydantic_settings import BaseSettings

# from app.db.dependencies import create_session
# from app.settings import AppSettings
from lib.settings import get_settings
from lib.types import Providers

from .modules import some

MODULES: Iterable[Providers] = [
    some.PROVIDERS,
]
# SETTINGS = (AppSettings,)


def _register_settings(
    container: aioinject.Container,
    *,
    settings_classes: Iterable[type[BaseSettings]],
) -> None:
    for settings_cls in settings_classes:
        factory = functools.partial(get_settings, settings_cls)
        container.register(aioinject.Singleton(factory, type_=settings_cls))


@functools.lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()
    # container.register(aioinject.Scoped(create_session))

    for provider in itertools.chain.from_iterable(MODULES):
        container.register(provider)

    # _register_settings(container, settings_classes=SETTINGS)

    return container
