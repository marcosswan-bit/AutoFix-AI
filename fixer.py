from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_file(path):
    with open(path, "r") as f:
        code = f.read()

    prompt = f"""
You are a senior software engineer.

1. Find bugs and bad practices
2. Explain them simply
3. Then output a FIXED version of the code

CODE:
{code}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        print("\n🤖 AI Review:\n")
        print(response.choices[0].message.content)
        print("\n" + "="*50 + "\n")

    except Exception as e:
        print("❌ Error:", e)
