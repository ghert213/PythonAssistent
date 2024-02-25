import assemblyai as aai
from ticktick.oauth2 import OAuth2
from ticktick.api import TickTickClient
from rutimeparser import parse, get_last_clear_text

from datetime import datetime
from os import environ
import json

from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, EMAIL, PASSWORD

auth_client = OAuth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
client = TickTickClient(EMAIL, PASSWORD, auth_client)


aai.settings.api_key = environ['AAI_TOKEN']
transcriber = aai.Transcriber()
config = aai.TranscriptionConfig(language_code="ru")

def recognize_speech(file_name: str) -> str:
    transcript = transcriber.transcribe(file_name, config)
    return transcript.text


def recognize_sentence(text: str) -> tuple[str, str]:
    time = parse(text)
    print(type(time))
    print(time)
    task = get_last_clear_text(text)
    return time, task


def create_task(name: str, project_id:str, startDate: datetime) -> None:
    formatted_date = startDate.strftime('%Y-%m-%dT%H:%M:%SZ')
    local_task = client.task.builder(name, project_id, formatted_date)
    groceries = client.task.create(local_task)
