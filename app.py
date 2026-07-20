"""
Streamlit application for the RAG-based Chatbot.

This application:
1. Loads the embedding model.
2. Connects to the existing ChromaDB vector store.
3. Initializes the RAG retriever.
4. Loads the Groq Large Language Model.
5. Accepts a user query through a Streamlit interface.
6. Retrieves relevant document chunks.
7. Generates an answer using the Groq LLM.
"""

import streamlit as st
from dotenv import load_dotenv

from embedding import EmbeddingManager
from vector_store import VectorStore
from retriever import RAGRetriever
from llm import GroqLLM
from rag import rag_simple

# ---------------------------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------------------------

# Load the environment variables from the .env file.
# The .env file stores the Groq API key securely.
load_dotenv()

# ---------------------------------------------------------------------
# Initialize the RAG Components
# ---------------------------------------------------------------------

# EmbeddingManager:
# Generates embeddings for user queries.

embedding_manager = EmbeddingManager()

# VectorStore:
# Connects to the existing ChromaDB vector database
# that already contains the document embeddings.

vectorstore = VectorStore()
st.write("Documents in vector store:", vectorstore.collection.count())

# RAGRetriever:
# Retrieves the most relevant document chunks
# from the vector database.

rag_retriever = RAGRetriever(
    vectorstore,
    embedding_manager
)

# GroqLLM:
# Loads the Groq Large Language Model
# used for answer generation.

groq_llm = GroqLLM()

# ---------------------------------------------------------------------
# Streamlit User Interface
# ---------------------------------------------------------------------

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG-Based Chatbot")

st.write(
    "Ask a question related to the uploaded document."
)

question = st.text_input(
    "Enter your question"
)

# ---------------------------------------------------------------------
# Generate Response
# ---------------------------------------------------------------------

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching relevant documents..."):

            answer = rag_simple(
                query=question,
                retriever=rag_retriever,
                llm=groq_llm.llm
            )

        st.success("Answer")

        st.write(answer)