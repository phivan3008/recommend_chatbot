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
    documents = [item["tom_tat"] for item in data_list]
    metadatas = [{"name": item["ten_phim"], "genre": item["the_loai"]} for item in data_list]
    ids = [f"doc_{i}" for i in range(len(data_list))]

    collection.add(documents=documents, metadatas=metadatas, ids=ids)

def search_knowledge(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results

data_list = [
  {
    "ten_phim": "The Shawshank Redemption (1994)",
    "the_loai": "Chính kịch, Tội phạm",
    "tom_tat": "Câu chuyện về Andy Dufresne, một nhân viên ngân hàng bị kết án oan và hành trình tìm lại tự do, hy vọng và tình bạn trong nhà tù Shawshank."
  },
  {
    "ten_phim": "The Godfather (1972)",
    "the_loai": "Tội phạm, Chính kịch",
    "tom_tat": "Tập trung vào gia đình mafia Corleone và quá trình chuyển giao quyền lực từ người cha Vito sang con trai út Michael, người ban đầu không muốn dính líu đến thế giới ngầm."
  },
  {
    "ten_phim": "The Dark Knight (2008)",
    "the_loai": "Hành động, Tội phạm, Giật gân",
    "tom_tat": "Batman đối mặt với kẻ thù lớn nhất của mình, Joker, một tên tội phạm tâm thần gieo rắc hỗn loạn và thách thức giới hạn đạo đức của Người Dơi."
  },
  {
    "ten_phim": "Pulp Fiction (1994)",
    "the_loai": "Tội phạm, Chính kịch",
    "tom_tat": "Những câu chuyện đan xen của các nhân vật trong thế giới ngầm ở Los Angeles, bao gồm hai sát thủ, vợ của một ông trùm và một võ sĩ quyền Anh."
  },
  {
    "ten_phim": "Forrest Gump (1994)",
    "the_loai": "Chính kịch, Lãng mạn",
    "tom_tat": "Cuộc đời phi thường của Forrest Gump, một người đàn ông có IQ thấp nhưng trái tim nhân hậu, vô tình trở thành nhân chứng và người tham gia vào các sự kiện lịch sử quan trọng của Mỹ."
  },
  {
    "ten_phim": "Inception (2010)",
    "the_loai": "Hành động, Khoa học viễn tưởng, Giật gân",
    "tom_tat": "Một nhóm chuyên gia xâm nhập vào giấc mơ của người khác để đánh cắp thông tin, nay nhận nhiệm vụ thực hiện điều ngược lại: cấy một ý tưởng vào tiềm thức."
  },
  {
    "ten_phim": "The Matrix (1999)",
    "the_loai": "Hành động, Khoa học viễn tưởng",
    "tom_tat": "Một hacker tên Neo phát hiện ra rằng thế giới anh đang sống thực chất là một chương trình giả lập, và anh được chọn để giải phóng nhân loại."
  },
  {
    "ten_phim": "The Lord of the Rings: The Fellowship of the Ring (2001)",
    "the_loai": "Phiêu lưu, Giả tưởng, Hành động",
    "tom_tat": "Chàng hobbit Frodo Baggins bắt đầu hành trình nguy hiểm đến núi Doom để phá hủy chiếc Nhẫn Chúa, một vũ khí quyền năng có thể hủy diệt thế giới."
  }
]


if __name__ == "__main__":
    add_data_to_chroma(data_list)
