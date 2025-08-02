import chromadb
from dotenv import load_dotenv
import os
import json
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
    results = collection.query(query_texts=[query])
    return results

def read_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

data_list = read_json_file("sample_data.json")

if __name__ == "__main__":
    add_data_to_chroma(data_list)
