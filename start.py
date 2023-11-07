import openai
import os
from config import OPENAI_API_KEY
import textToSpeech
import playAudio
import recordSpeech
import speechToText


openai.api_key = OPENAI_API_KEY

openai.organization = "org-Zv09lXMbqC7TqcJFmH96zF6k"
openai.models.list()

def get_response(prompt):
    role_description = "assistant"
    response = openai.chat.completions.create(
        model = 'gpt-4',
        messages = [
            {"role": "system", "content": role_description}, 
            {"role": "user", "content": prompt},
        ],
    )
    with open("response.txt","w") as file:
        file.write(response.choices[0].message.content)

    textToSpeech.text_to_speech()
    playAudio.playSpeech()

    ans = str(input("Continue..   （y/n）"))
    if ans ==('y'):
        get_prompt()
    else: 
        print("--end--")
    return


def get_prompt():
    recordSpeech.get_audio()
    prompt = speechToText.get_transcript()
    print(prompt)
    get_response(prompt) 
    return

if __name__ == "__main__":
    get_prompt()

