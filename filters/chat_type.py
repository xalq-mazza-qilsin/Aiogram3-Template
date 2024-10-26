from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_types: list[ChatType]):
        self.chat_types = chat_types

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.chat_types
