# 📚 Retrieval-Augmented Generation (RAG) Pipeline for PDF Question Answering

An end-to-end **Retrieval-Augmented Generation (RAG)** application that answers user queries from PDF documents using **semantic search** and **Large Language Models (LLMs)**.

The project extracts text from PDF documents, splits it into semantic chunks, generates dense vector embeddings using **Sentence Transformers**, stores the embeddings in **ChromaDB**, retrieves the most relevant document chunks through semantic search, and generates context-aware responses using the **Groq LLM**. The application also provides an interactive **Streamlit** web interface for asking questions.

---

# 🚀 Features

- 📄 Load PDF documents
- ✂️ Split documents into semantic chunks
- 🧠 Generate embeddings using Sentence Transformers
- 💾 Store embeddings in ChromaDB vector database
- 🔍 Retrieve relevant document chunks using semantic similarity search
- 📑 Top-K document retrieval
- 🤖 Context-aware answer generation using Groq LLM
- 🌐 Interactive Streamlit web interface
- 🏗️ Modular RAG pipeline implementation

---

# 🏗️ RAG Pipeline Architecture

```text
                     PDF Documents
                           │
                           ▼
                  PDF Loader (PyMuPDF)
                           │
                           ▼
                  Text Chunking
                           │
                           ▼
             SentenceTransformer Embeddings
                           │
                           ▼
               ChromaDB Vector Store
                           │
                           ▼
              User Question (Embedding)
                           │
                           ▼
               Semantic Similarity Search
                           │
                           ▼
             Top-K Relevant Document Chunks
                           │
                           ▼
                    Groq Large Language Model
                           │
                           ▼
                    Context-Aware Answer
```

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Frameworks & Libraries

- Streamlit
- LangChain
- Sentence Transformers
- ChromaDB
- PyMuPDF
- PyPDF
- NumPy
- python-dotenv

### LLM

- Groq API
- Llama 3.1 8B Instant

---

# 📂 Project Structure

```text
RAG-Based-Chatbot/
│
├── app.py                     # Streamlit application
├── embedding.py               # Embedding generation
├── vector_store.py            # ChromaDB operations
├── retriever.py               # Semantic retrieval
├── rag.py                     # RAG pipeline
├── llm.py                     # Groq LLM integration
├── notebook/
│   └── document.ipynb         # PDF indexing notebook
├── data/
│   ├── pdf/                   # PDF documents
│   └── vector_store/          # ChromaDB database
├── requirement.txt
├── pyproject.toml
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Navya-nigam/RAG-Based-Chatbot.git

cd RAG-Based-Chatbot
```

Install the required packages

```bash
pip install -r requirement.txt
```

Create a `.env` file in the project root

```text
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Running the Project

### Step 1: Index the PDF documents

Run the notebook:

```text
notebook/document.ipynb
```

This will:

- Load PDF files
- Create text chunks
- Generate embeddings
- Store embeddings in ChromaDB

### Step 2: Start the chatbot

```bash
streamlit run app.py
```

Open the URL shown in your terminal (usually `http://localhost:8501`).

---

# 💬 Example

**Question**

> What is the HLER architecture?

**Answer**

> The HLER architecture decomposes the empirical research workflow into eight specialised agent roles coordinated by an Orchestrator that maintains the workflow state and generated artefacts.

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Dense Vector Embeddings
- Vector Databases
- Prompt Engineering
- LangChain
- Large Language Models
- Document Question Answering
- Information Retrieval
- Streamlit Application Development

---

# 🔮 Future Improvements

- Multiple PDF Support
- Source Citation
- Conversational Memory
- Hybrid Search (Keyword + Vector Search)
- Cross-Encoder Reranking
- Docker Containerization
- Cloud Deployment
- User Authentication

---

## 👩‍💻 Author

**Navya Nigam**

B.Tech Computer Science (2022–2026)

Interested in Machine Learning, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and AI Engineering.

GitHub: https://github.com/Navya-nigam

---

## ⭐ If you found this project useful, consider giving it a star!
