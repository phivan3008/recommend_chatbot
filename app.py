from openai_handler import generate_response
from chromadb_client import search_knowledge
from tts_engine import text_to_speech

def run_chatbot():
    print("Chào mừng đến với Chatbot AI! Gõ 'exit' để thoát.")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        docs = search_knowledge(user_input)
        print(f"💡 Kiến thức liên quan: {docs}")
        
        response = generate_response(user_input)
        print(f"🤖 Bot: {response}")

        audio_path = text_to_speech(response)
        print(f"🔊 Âm thanh đã được tạo: {audio_path}")

if __name__ == "__main__":
    run_chatbot()
