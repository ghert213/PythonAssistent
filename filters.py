from aiogram.types import Message, ContentType
from aiogram.filters import Filter


class AudioFilter(Filter):
    def __init__(self) -> None:
        return
    async def __call__(self, message: Message) -> bool:
        return message.content_type == ContentType.VOICE