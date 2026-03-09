from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

#made object of ChatOpenAI class and passed the model name as gpt-4, temperature as 1.5 and max_completion_tokens as 10
model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

#invoke method is used to call the model and pass the prompt as an argument
result = model.invoke("Write a 5 line poem on cricket")

print(result.content)