import assemblyai as aai
import os

aai.settings.api_key = os.environ['AAI_TOKEN']
transcriber = aai.Transcriber()
config = aai.TranscriptionConfig(language_code="ru")

def recognize_speech(file_name: str) -> str:
    transcript = transcriber.transcribe(file_name, config)
    return transcript.text