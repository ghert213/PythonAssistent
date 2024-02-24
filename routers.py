from aiogram import Router
from aiogram.types import Message
from filters import AudioFilter
from aiogram import Bot
from ai_funcs import recognize_speech

secretary = Router()

@secretary.message(AudioFilter())
async def add_task(message: Message, bot: Bot) -> None:
    await bot.download(message.voice.file_id,  f"{message.voice.file_id}.wav")
    await message.answer(f"Я принял аудио-сообщение")
    recognized_text = recognize_speech(f"{message.voice.file_id}.wav")
    await message.answer(f"{recognized_text}")