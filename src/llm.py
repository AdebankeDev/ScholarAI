from openai import OpenAI
from src.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    MODEL_NAME,
)


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
)


def ask_llm(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"LLM request failed: {error}"