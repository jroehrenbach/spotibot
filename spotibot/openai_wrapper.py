
import openai
import os


API_KEY = os.environ.get('OPENAI_API_KEY')
MODEL = "gpt-3.5-turbo"


class OpenAIWrapper:
    def __init__(self, api_key=None):
        openai.api_key = api_key or API_KEY

    def generate_text(self, messages, model=MODEL, max_tokens=2000):
        completion = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens
        )
        return completion['choices'][0]['message']['content']
