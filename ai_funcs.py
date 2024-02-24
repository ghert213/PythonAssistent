from dotenv import load_dotenv
import assemblyai as aai
import os

load_dotenv()
AAI_TOKEN = os.getenv("AAI_TOKEN")

aai.settings.api_key = AAI_TOKEN
transcriber = aai.Transcriber()
config = aai.TranscriptionConfig(language_code="ru")

def recognize_speech(file_name: str) -> str:
    transcript = transcriber.transcribe(file_name, config)
    return transcript.text