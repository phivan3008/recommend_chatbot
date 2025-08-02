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

def ask_llm(context, user_input):
    system_prompt = (             
        "You are a helpful assistant specializing in laptop recommendations. "
        "Use the provided context to recommend the best laptop(s) for the user needs. "
        "Be specific about why each laptop matches their requirements. "
        "Format your response in a friendly, conversational manner."        
    )

    user_prompt = (             
        f"User requirements: {user_input}\n\n"
        f"Context (top relevant laptops):\n{context}\n\n"
        "Dựa vào danh sách top relevant movies, bổ sung các thông tin liên quan đến bộ phim đó như: "
        "Nội dung tóm tắt"
        "Diễn viên chính"
        "Năm sản xuất"
        "Điểm đánh giá IMDB"      
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model="GPT-4o-mini",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content


def build_context(results, n_context=3):
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    context_str = ""
    for doc, meta in zip(docs, metas):
        context_str += (
            f"Name: {meta['name']}\n"
            f"Genre: {meta['genre']}\n"
            f"Summary: {doc}\n"
        )
    return context_str.strip()
