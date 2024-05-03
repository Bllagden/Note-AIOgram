from typing import TypeVar

from pydantic_settings import BaseSettings, SettingsConfigDict

# from pydantic import SecretStr

TSettings = TypeVar("TSettings", bound=BaseSettings)


class TelegramBotSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="bot_")

    token: str  # SecretStr
