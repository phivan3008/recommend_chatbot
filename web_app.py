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
        query_result = search_knowledge(user_input)

        # Tạo context cho mô hình LLM
        context = build_context(query_result)

        # Lấy phản hồi văn bản từ mô hình
        response = ask_llm(context, user_input)

        # Tạo nút phát giọng nói
        if st.button("🔊 Phát giọng nói"):
            # Gọi hàm chuyển văn bản thành giọng nói
            audio_path = text_to_speech(response)

            # Đọc file âm thanh và mã hoá base64
            with open(audio_path, "rb") as f:
                audio_bytes = f.read()
                audio_base64 = base64.b64encode(audio_bytes).decode()

            # Chèn player vào giao diện (không autoplay)
            st.markdown(f"""
                <audio controls>
                    <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
                </audio>
            """, unsafe_allow_html=True)

        # Hiển thị câu trả lời của bot
        st.write(f"🤖 Bot trả lời: {response}")
