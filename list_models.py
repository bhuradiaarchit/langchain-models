from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.genai as genai
import os

load_dotenv()

# Configure the API key
client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

# List available models
models = client.models.list()
print("Available models:")
for model in models:
    print(f"- {model.name}: {model.description}")
    if hasattr(model, 'supported_generation_methods'):
        print(f"  Supported methods: {model.supported_generation_methods}")