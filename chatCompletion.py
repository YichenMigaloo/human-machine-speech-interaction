
import os
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
openai.organization = "org-Zv09lXMbqC7TqcJFmH96zF6k"
openai.models.list()

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)
