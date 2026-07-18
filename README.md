# 📚 Retrieval-Augmented Generation (RAG) Pipeline for PDF Question Answering

An end-to-end Retrieval-Augmented Generation (RAG) pipeline that answers user queries from PDF documents using semantic search and Large Language Models (LLMs).

The project extracts text from PDF documents, splits them into manageable chunks, converts each chunk into dense vector embeddings using Sentence Transformers, stores the embeddings in ChromaDB, retrieves the most relevant information through semantic similarity search, and generates context-aware responses using the Groq LLM.

---

# 🚀 Features

- 📄 Load PDF documents
- ✂️ Split documents into semantic chunks
- 🧠 Generate embeddings using Sentence Transformers
- 💾 Store embeddings in ChromaDB vector database
- 🔍 Retrieve relevant document chunks using semantic similarity search
- 📑 Top-K document retrieval
- 🤖 Context-aware answer generation using Groq LLM
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
        SentenceTransformer Embedding Model
                           │
                           ▼
                   Dense Vector Embeddings
                           │
                           ▼
                ChromaDB Vector Database
                           ▲
                           │
                    User Question
                           │
                           ▼
             Query Embedding Generation
                           │
                           ▼
            Semantic Similarity Search
                           │
                           ▼
               Top-K Relevant Chunks
                           │
                           ▼
                 Prompt Construction
                           │
                           ▼
                 Groq Large Language Model
                           │
                           ▼
                   Generated Response
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB |
| LLM | Groq (Llama-3.1-8B-Instant) |
| PDF Processing | PyMuPDF |
| Numerical Computing | NumPy |
| Environment Variables | python-dotenv |

---

# 📂 Project Structure

```text
RAG-Based-Chatbot/
│
├── notebook/
│   └── document.ipynb
│
├── data/
│   ├── pdfs/
│   └── vector_store/
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
└── main.py
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Navya-nigam/RAG-Based-Chatbot.git

cd RAG-Based-Chatbot
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5. Run the project

Open

```
notebook/document.ipynb
```

and execute the notebook cells sequentially.

---

# 🔄 RAG Pipeline Workflow

### Step 1 — Load PDF

The PDF document is loaded using **PyMuPDF**.

---

### Step 2 — Text Chunking

The extracted text is divided into smaller chunks to improve retrieval accuracy and fit within the LLM context window.

---

### Step 3 — Generate Embeddings

Each text chunk is converted into a dense vector representation using the **SentenceTransformer all-MiniLM-L6-v2** model.

---

### Step 4 — Store in ChromaDB

The embeddings, document text, and metadata are stored in a persistent ChromaDB vector database.

---

### Step 5 — User Query

When a user asks a question, the query is converted into an embedding using the same embedding model.

---

### Step 6 — Semantic Retrieval

The query embedding is compared against stored document embeddings using cosine similarity.

The top-K most relevant document chunks are retrieved.

---

### Step 7 — Prompt Construction

The retrieved document chunks are combined with the user's question to create a prompt.

---

### Step 8 — Response Generation

The prompt is passed to the Groq-hosted Llama model, which generates the final context-aware answer.

---

# 📦 Main Components

### PDF Processing

- PDF Loading
- Text Extraction

---

### Embedding Module

- SentenceTransformer
- all-MiniLM-L6-v2

---

### Vector Store

- ChromaDB
- Persistent Storage
- Document Metadata

---

### Retrieval Module

- Query Embedding
- Semantic Similarity Search
- Top-K Retrieval

---

### LLM Module

- Groq API
- Llama-3.1-8B-Instant
- Prompt-based Response Generation

---

# 💬 Example Queries

```
What is self-attention?

Explain the attention mechanism.

What is Unified Multi-task Learning Framework?

Summarize the uploaded paper.

What are Hard Negative Mining techniques?

Explain transformer architecture.
```

---

# 📦 Dependencies

- langchain
- langchain-core
- langchain-community
- langchain-groq
- chromadb
- sentence-transformers
- pymupdf
- pypdf
- numpy
- python-dotenv

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

---

# 🔮 Future Improvements

- Streamlit Web Interface
- Multiple PDF Support
- Source Citation
- Conversational Memory
- Hybrid Search (Keyword + Vector Search)
- Reranking Models
- Docker Containerization
- Cloud Deployment

---

# 👩‍💻 Author

**Navya Nigam**

B.Tech Computer Science (2022–2026)

Interested in Machine Learning, NLP, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and AI Engineering.

GitHub: https://github.com/Navya-nigam

---

## ⭐ If you found this project useful, consider giving it a star!
