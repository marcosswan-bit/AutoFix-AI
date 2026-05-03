from openai import OpenAI

client = OpenAI()

def analyze_file(path):
    with open(path, "r") as f:
        code = f.read()

    prompt = f"""
    Find bugs and bad practices in this code.
    Suggest fixes AND output the fixed version.

    Code:
    {code}
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print("🤖 AI Suggestions:\n")
    print(response.choices[0].message.content)
