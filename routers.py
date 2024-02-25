from aiogram import Router
from aiogram.types import Message
from filters import AudioFilter
from aiogram import Bot

from os import remove, environ

from ai_funcs import recognize_speech, recognize_sentence, create_task

PROJECT_ID = environ["PROJECT_ID"]
secretary = Router()

@secretary.message(AudioFilter())
async def add_task(message: Message, bot: Bot) -> None:
    await bot.download(message.voice.file_id,  f"{message.voice.file_id}.wav")
    await message.answer(f"Пытасюь разобрать текст...")
    recognized_text = recognize_speech(f"{message.voice.file_id}.wav")
    date, task = recognize_sentence(recognized_text)
    await message.answer(recognized_text)
    await message.answer(f"Обнаружил дату - {date}")
    await message.answer(f"Обнаружил задачу - {task}")
    create_task(task, PROJECT_ID, date)
    remove(f"{message.voice.file_id}.wav")
