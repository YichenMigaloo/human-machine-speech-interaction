import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
openai.organization = "org-Zv09lXMbqC7TqcJFmH96zF6k"
openai.models.list()

audio_file = open("/Users/yichen/Documents/GitHub/human-machine-interaction/human-machine-speech-interaction/test.wav", "rb")
transcript = openai.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)


print(transcript)