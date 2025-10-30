from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document
import json


OPENAI_API_KEY = 'OPENAI_API_KEY'

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
chat_model = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY)



audio_cache = {}

def get_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)


def load_json_data():
    data = get_data("data.txt")
    return data

def create_vector_database(paragraphs):
    documents = [Document(page_content=paragraph["answer"], metadata={"question": paragraph["question"]}) for paragraph in paragraphs]
    vector_db = FAISS.from_documents(documents, embeddings)
    return vector_db

def setup_retrieval_qa(vector_db):
    retriever = vector_db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=chat_model,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )
    return qa_chain

async def chatbot(qa_chain, query):
    response = qa_chain({"query": query})
    answer = response["result"]
    
    return answer
