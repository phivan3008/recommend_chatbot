import chromadb
from dotenv import load_dotenv
import os
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

load_dotenv()

# Khởi tạo ChromaDB
embedding_function = OpenAIEmbeddingFunction(
    api_key=os.getenv("TEXT_EMBEDDING_KEY"),
    model_name="text-embedding-3-small",
    api_base=os.getenv("OPENAI_BASE_URL")
)

client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection(
    name="knowledge_base",
    embedding_function=embedding_function
)

def add_data_to_chroma(data_list):
    documents = [item["text"] for item in data_list]
    metadatas = [{"topic": item["topic"]} for item in data_list]
    ids = [f"doc_{i}" for i in range(len(data_list))]

    collection.add(documents=documents, metadatas=metadatas, ids=ids)

def search_knowledge(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results["documents"]

data_list = [
    {
        "topic": "Giới thiệu phim",
        "text": "Stranger Things: Một nhóm trẻ em thám hiểm những hiện tượng siêu nhiên ở thị trấn Hawkins và đối đầu với thí nghiệm bí mật của chính phủ."
    },
    {
        "topic": "Giới thiệu phim",
        "text": "The Witcher: Geralt, thợ săn quái vật lạnh lùng, rong ruổi qua thế giới huyền bí đầy chính trị và âm mưu để thực hiện số phận của mình."
    },
    {
        "topic": "Giới thiệu phim",
        "text": "Money Heist: Một nhóm tội phạm kỳ tài thực hiện vụ cướp táo bạo tại Xưởng in tiền Hoàng gia Tây Ban Nha, dưới sự chỉ huy của Giáo sư."
    },
    {
        "topic": "Giới thiệu phim",
        "text": "Breaking Bad: Giáo viên hóa học Walter White chuyển sang sản xuất ma túy để đảm bảo tương lai cho gia đình khi phát hiện mắc bệnh ung thư."
    },
    {
        "topic": "Giới thiệu phim",
        "text": "The Queen's Gambit: Bé gái mồ côi Beth Harmon trở thành thiên tài cờ vua trong hành trình vượt qua nghiện ngập và đấu trí với thế giới nam giới."
    },
]

if __name__ == "__main__":
    add_data_to_chroma(data_list)
