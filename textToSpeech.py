
import openai
from config import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY
openai.organization = "org-Zv09lXMbqC7TqcJFmH96zF6k"
openai.models.list()



def text_to_speech():
  file = open("response.txt",'r')
  lines = file.read()

  speech_file_path = "response.mp3"
  response = openai.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=lines
  )
  response.stream_to_file(speech_file_path)
  

