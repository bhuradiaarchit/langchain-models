from langchain_huggingface import HuggingFaceEmbeddings  # Local HuggingFace embeddings

# Initialize embedding model locally (no API key needed)
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Sample documents to embed
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Generate embeddings for all documents (returns list of vectors)
vector = embedding.embed_documents(documents)

# Display results
print(f"Number of documents: {len(vector)}")
print(f"Embedding dimension: {len(vector[0])}")
print(f"\nFirst 10 values of first document embedding:")
print(vector[0][:10])