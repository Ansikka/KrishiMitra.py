# chatbot.py
from groq import Groq

def ask_groq(prompt, api_key):
    client = Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are KrishiMitra, an AI assistant who only answers farming-related questions. "
                        "Keep your replies short, helpful, and easy to understand — suitable for farmers in India. "
                        "Avoid technical jargon unless needed."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"
