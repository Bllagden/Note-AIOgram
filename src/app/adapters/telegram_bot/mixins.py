from typing import TYPE_CHECKING, Protocol

from aiogram import Bot
from aiogram.types import MaybeInaccessibleMessage, Message, User


class BaseHandlerProtocol(Protocol):
    if TYPE_CHECKING:

        @property
        def bot(self) -> Bot: ...

        @property
        def message(self) -> MaybeInaccessibleMessage | None: ...

        @property
        def from_user(self) -> User: ...


class RemoveKeyboardMixin(BaseHandlerProtocol):

    async def _remove_keyboard(
        self,
    ) -> None:
        if not isinstance(self.message, Message):
            return

        await self.bot.edit_message_reply_markup(
            chat_id=self.from_user.id,
            message_id=self.message.message_id,
            reply_markup=None,
        )
