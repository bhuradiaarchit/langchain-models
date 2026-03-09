from langchain_openai import OpenAIEmbeddings  # OpenAI's embedding model
from dotenv import load_dotenv  # Load environment variables
from sklearn.metrics.pairwise import cosine_similarity  # Calculate similarity between embeddings
import numpy as np  # Numerical operations

# Load API key from .env file
load_dotenv()

# Initialize OpenAI embedding model with 300 dimensions
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# List of documents about Indian cricketers
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# User query to find similar documents
query = 'tell me about bumrah'

# Convert all documents to embedding vectors
doc_embeddings = embedding.embed_documents(documents)

# Convert query to embedding vector
query_embedding = embedding.embed_query(query)

# Calculate cosine similarity between query embedding and all document embeddings
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find document with highest similarity score
# Step-by-step explanation:
# 1. enumerate(scores) - creates pairs: (0, score0), (1, score1), (2, score2), etc.
# 2. list() - converts to a list of tuples
# 3. sorted(..., key=lambda x: x[1]) - sorts tuples by score (x[1]) in ascending order
#    key=lambda x: x[1] means "sort by the second element of each tuple"
# 4. [-1] - gets the LAST element (highest score after sorting)
# 5. index, score = ... - unpacks the tuple into two variables
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

# Print results
print(query)
print(documents[index])
print("similarity score is:", score)