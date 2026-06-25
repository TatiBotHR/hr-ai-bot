import os
import requests

API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_text(text: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "Ты HR эксперт. Анализируй резюме строго и структурировано."
            },
            {
                "role": "user",
                "content": f"""
Проанализируй резюме:

Процент соответствия:
Сильные стороны:
Слабые стороны:
Уточнить:
Рекомендация:

{text}
"""
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()["choices"][0]["message"]["content"]
