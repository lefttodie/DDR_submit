import requests
import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def call_llm(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "arcee-ai/trinity-large-preview:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(URL, headers=headers, json=payload)

    data = response.json()

    if "choices" not in data:
        print("OPENROUTER ERROR:")
        print(data)
        raise Exception("OpenRouter API failed")

    return data["choices"][0]["message"]["content"]