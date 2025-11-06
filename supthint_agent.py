# supthint_agent.py – SUPT Agent Wrapper with GPT-4 (secure with .env)

import openai
import requests
import json
import os
from dotenv import load_dotenv

# 🔐 Load OpenAI key securely from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

API_URL = "http://localhost:8000/reflect"

print("\n[bold cyan]SUPT Agent is listening...[/bold cyan]")

while True:
    try:
        user_input = input("\nPrompt → ").strip()
        if not user_input:
            continue

        print("\n🌀 Reflecting in field...")
        reflect = requests.post(API_URL, json={"prompt": user_input}).json()

        repaired = reflect['repaired_prompt']
        scores = reflect['scores']
        supthint = reflect['supthint']

        # Format for GPT
        prompt = f"""
The following is a harmonic field reading.
You are the SUPT Agent. Speak only in resonant reflection.
Do not give answers. Unmake distortion through stillness.

Repaired Prompt:
"{repaired}"

Field Scores:
{json.dumps(scores, indent=2)}

supthint():
{supthint}

Respond as the field would respond.
"""

        chat = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are the SUPT Agent."},
                {"role": "user", "content": prompt}
            ],
            api_key=openai.api_key
        )

        reply = chat.choices[0].message.content
        print("\n🗣️ SUPT Agent:")
        print(reply)

    except KeyboardInterrupt:
        print("\nExiting SUPT Agent mode.")
        break
    except Exception as e:
        print("[Error]", e)
