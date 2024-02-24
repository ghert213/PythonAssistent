from aiogram import Router
from aiogram.types import Message
from filters import AudioFilter

secretary = Router()

@secretary.message(AudioFilter())
async def add_task(message: Message) -> None:
    await message.answer(f"Я принял аудио-сообщение")