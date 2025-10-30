🧠 RAG Agent 
This project is a Retrieval-Augmented Generation (RAG)-based chatbot built with Streamlit and LangChain.
It allows users to ask questions about Thoughtful AI and receive context-aware answers powered by OpenAI embeddings and models.

🚀 Features

Interactive Streamlit chat interface
LangChain-based retrieval and QA pipeline
FAISS vector database for efficient semantic search
Context-aware responses using OpenAI GPT-4
Local JSON-based knowledge base (data.txt)

🗂️ Project Structure
.
├── app.py          # Streamlit UI and chat logic
├── rag.py          # RAG setup (embeddings, retriever, QA chain)
├── data.txt        # Knowledge base in JSON format
└── README.md       # Project documentation

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/huraira836/RagAgent
cd rag-agent

2️⃣ Install dependencies
pip install -r requirements.txt

Then modify rag.py to read:

▶️ Run the App
streamlit run app.py

Launch the Streamlit interface:

streamlit run app.py
