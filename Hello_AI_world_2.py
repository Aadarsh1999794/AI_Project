import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# point the SAME client at Groq instead of OpenAI 👇
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
    ],
)
print(response.choices[0].message.content)