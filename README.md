# LangChain Models Learning Project

A comprehensive learning project demonstrating various LangChain models including LLMs, Chat Models, and Embeddings using both API-based and local inference approaches.

## Overview

This project explores different ways to use LangChain with various models from HuggingFace and OpenAI, covering:
- Large Language Models (LLMs)
- Chat Models
- Embedding Models
- Document Similarity Search
- Local and API-based inference

## Features

✅ **LLM Models** - Text generation using various LLM endpoints  
✅ **Chat Models** - Conversational AI using HuggingFace and OpenAI  
✅ **Embedding Models** - Local and API-based text embeddings  
✅ **Document Similarity** - Semantic search using cosine similarity  
✅ **Local Inference** - Run models locally without API costs  
✅ **API Integration** - OpenAI and HuggingFace API support  

## Project Structure

```
langchain-models/
├── LLMs/
│   └── 1_llm_demo.py              # Basic LLM demo
├── ChatModels/
│   ├── 4_chatmodel_hf_api.py      # HuggingFace API chat model
│   └── 5_chatmodel_hf_local.py    # Local HuggingFace chat model
├── EmbeddingModels/
│   ├── 3_embedding_hf_local.py    # Local HuggingFace embeddings
│   └── 4_document_similarity.py   # Semantic document search
├── requirements.txt               # Project dependencies
├── .env                           # Environment variables (not tracked)
├── .gitignore                     # Git ignore file
└── README.md                      # This file
```

## Installation

### Prerequisites
- Python 3.9+
- Virtual environment (recommended)
- Git (for cloning)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/langchain-models.git
   cd langchain-models
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or: source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file and add your API keys
   echo OPENAI_API_KEY=your_key_here > .env
   echo HUGGINGFACEHUB_API_TOKEN=your_key_here >> .env
   ```

## Usage

### Run Local Embedding Model
```bash
python EmbeddingModels/3_embedding_hf_local.py
```

### Run Document Similarity Search
```bash
python EmbeddingModels/4_document_similarity.py
```

### Run Local Chat Model
```bash
python ChatModels/5_chatmodel_hf_local.py
```

## Key Concepts

### Embeddings
Convert text into numerical vectors that capture semantic meaning. Used for:
- Similarity search
- Clustering
- Recommendation systems

### Chat Models
Conversational AI models that can handle multi-turn conversations with context.

### LLMs
Large Language Models for text generation, summarization, translation, and more.

## Dependencies

- `langchain` - Core LangChain framework
- `langchain-openai` - OpenAI integration
- `langchain-huggingface` - HuggingFace integration
- `sentence-transformers` - Local embedding models
- `scikit-learn` - Cosine similarity calculations
- `python-dotenv` - Environment variable management
- `torch` - PyTorch for local model inference
- `transformers` - HuggingFace transformers library

See `requirements.txt` for all dependencies.

## Notes

- ⚠️ **API Keys**: Keep `.env` file private and never commit it to GitHub
- 💾 **Models**: First run will download models (~100-500MB depending on model)
- 🔧 **Local Inference**: Requires significant RAM (8GB+) for larger models
- 🚀 **Free Models**: Use local models to avoid API costs

## Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [HuggingFace Models](https://huggingface.co/models)
- [OpenAI API](https://platform.openai.com/docs)
- [Sentence Transformers](https://www.sbert.net/)

## Contributing

Feel free to fork, modify, and improve this project for learning purposes.

## License

This project is open source and available under the MIT License.

---

**Last Updated:** March 2026  
**Status:** Active Learning Project
