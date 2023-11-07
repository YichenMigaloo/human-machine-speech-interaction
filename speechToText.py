import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
openai.organization = "org-Zv09lXMbqC7TqcJFmH96zF6k"
openai.models.list()

def get_transcript():
  audio_file = open("prompt.mp3", "rb")
  transcript = openai.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
  )
  return transcript.text
