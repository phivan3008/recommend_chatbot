import base64
import streamlit as st
from openai_handler import ask_llm, build_context
from chromadb_client import search_knowledge
from tts_engine import text_to_speech

st.set_page_config(page_title="Chatbot Giải Trí", layout="centered")
st.title("🎬 Chatbot Giới Thiệu Phim")
st.write("Hãy hỏi về phim hay hoặc gợi ý giải trí. Ví dụ: *Phim hành động châu Âu*.")

# Nhập truy vấn người dùng
user_input = st.text_input("Bạn:", "", help="Nhập câu hỏi về phim")

if user_input:
    with st.spinner("🔍 Đang xử lý..."):
        # Tìm kiếm kiến thức nền từ ChromaDB
        queryRestul = search_knowledge(user_input)
        #st.write("💡 Kiến thức liên quan:")
        #for doc in docs:
        #    st.markdown(f"- {doc[0]}")

        #Build context for LLM
        context = build_context(queryRestul)

        # Tạo phản hồi văn bản
        response = ask_llm(context, user_input)
        st.write(f"🤖 Bot trả lời: {response}")

        # Tạo giọng nói
        audio_path = text_to_speech(response)

        # Tạo mã base64 từ file .wav
        with open(audio_path, "rb") as f:
            audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()

        # Hiển thị lần đầu (autoplay)
        st.markdown(f"""
            <audio autoplay>
                <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
            </audio>
        """, unsafe_allow_html=True)

        # Nút phát lại
        if st.button("🔁 Phát lại"):
            st.markdown(f"""
                <audio autoplay>
                    <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
                </audio>
            """, unsafe_allow_html=True)
