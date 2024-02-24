from aiogram import Router, F, html,  types
from aiogram.types import Message, ContentType, Voice
from aiogram.filters import Filter
from aiogram.types import Message


secretary = Router()

@secretary.message()
async def add_task(message: Message) -> None:
    pass