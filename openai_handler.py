from dotenv import load_dotenv
import openai
import os

load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_BASE_URL")
)

def generate_response(user_input):
    messages = [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model="GPT-4o-mini",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content
