from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
#made object of OpenAI class and passed the model name as gpt-3.5-turbo-instruct
llm = OpenAI(model='gpt-3.5-turbo-instruct')

#invoke method is used to call the model and pass the prompt as an argument
result = llm.invoke("What is the capital of India")

print(result)

#Just generate API KEY using OpenAI playground
#save in dotenv file as OPENAI_API_KEY=your_api_key