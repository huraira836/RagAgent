import streamlit as st
import asyncio
from rag import chatbot, create_vector_database, load_json_data, setup_retrieval_qa

st.set_page_config(page_title="RAG Agent", page_icon="🏏", layout="wide")

st.markdown("Ask anything about ThoughfulAI")
paragraphs = load_json_data()
vector_db = create_vector_database(paragraphs)
qa_chain = setup_retrieval_qa(vector_db)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("⏳ Thinking...")
        
        async def get_response(query):
            return await chatbot(qa_chain, query)

        response = asyncio.run(get_response(prompt))

        message_placeholder.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

