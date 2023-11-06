from pathlib import Path
import openai
from config import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY
openai.organization = "org-Zv09lXMbqC7TqcJFmH96zF6k"
openai.models.list()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="啊！我和我的祖国，一刻也不能分割. 那味道……让我想起小琛宝。"
)
response.stream_to_file(speech_file_path)
