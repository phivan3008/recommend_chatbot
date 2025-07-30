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
```bash
git clone https://github.com/<your-repo-name>.git
cd chatbot_project

2. Cài thư viện cần thiết
pip install -r requirements.txt


Nếu chưa có file requirements.txt, bạn có thể cài thủ công:

pip install openai chromadb transformers torch soundfile streamlit simpleaudio



🔑 Cấu hình OpenAI API
Đặt API Key vào biến môi trường:
Windows:
set OPENAI_API_KEY=sk-xxxxx


Mac/Linux:
export OPENAI_API_KEY=sk-xxxxx



📁 Khởi tạo dữ liệu
Chạy đoạn mã để nạp dữ liệu mock vào ChromaDB:
python chromadb_client.py



💬 Chạy ứng dụng CLI
python app.py


Bạn có thể nhập câu hỏi, xem phản hồi văn bản và nghe phát âm từ file output.wav.


🌐 Chạy giao diện Web bằng Streamlit
streamlit run web_app.py


Truy cập http://localhost:8501 để tương tác với chatbot.


🔁 Tính năng Web UI
- Tự động phát giọng nói khi phản hồi mới được tạo
- Nút 🔁 Phát lại giúp nghe lại phản hồi
- Truy vấn kiến thức từ ChromaDB và hiển thị nguồn thông tin
- Dễ dàng tuỳ chỉnh giao diện bằng Streamlit

👨‍💻 Tác giả
- Phi Van — AI Application Engineer tại Elevate 👨‍🔬
- Hỗ trợ bởi Microsoft Copilot 🤖

📜 License
MIT License
