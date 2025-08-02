# 🎬 Entertainment Chatbot AI

Một chatbot AI giới thiệu phim / nội dung giải trí, sử dụng các công nghệ hiện đại:

- 🧠 **OpenAI GPT-4o**: sinh phản hồi hội thoại thông minh  
- 📚 **ChromaDB**: lưu trữ kiến thức dạng vector embedding  
- 🔊 **HuggingFace VITS (Tiếng Việt)**: chuyển văn bản thành giọng nói  

---

## 🚀 Tính năng

- Trả lời câu hỏi về phim hoặc chương trình giải trí  
- Trích xuất kiến thức nền từ ChromaDB  
- Phản hồi bằng văn bản + phát âm bằng giọng nói tiếng Việt  
- Giao diện CLI và Web UI bằng Streamlit  

---

## 📦 Cài đặt & Yêu cầu

1. Clone repository

2. Cài thư viện cần thiết

pip install openai chromadb transformers torch soundfile streamlit simpleaudio

🔑 Cấu hình OpenAI API
Tạo file .env

OPENAI_API_KEY=sk-GlKxsGKVhd4ftqS1L33gZw
TEXT_EMBEDDING_KEY=sk-HAfeizWMtwFhxlJUb_UC7A
OPENAI_BASE_URL=https://aiportalapi.stu-platform.live/jpe

📁 Khởi tạo dữ liệu
Chạy đoạn mã để nạp dữ liệu mock vào ChromaDB:
python chromadb_client.py

💬 Chạy ứng dụng CLI
python app.py

Bạn có thể nhập câu hỏi, xem phản hồi văn bản và nghe phát âm từ file output.wav.

🌐 Chạy giao diện Web bằng Streamlit
streamlit run web_app.py
or
python -m streamlit run web_app.py

Truy cập http://localhost:8501 để tương tác với chatbot.

🔁 Tính năng Web UI
- Phát giọng nói khi phản hồi được tạo
- Truy vấn kiến thức từ ChromaDB và hiển thị nguồn thông tin
- Dễ dàng tuỳ chỉnh giao diện bằng Streamlit

👨‍💻 Tác giả
- AI Beginner — AI Application Engineer tại Elevate 👨‍🔬
- Hỗ trợ bởi Microsoft Copilot 🤖

📜 License
MIT License
