from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke('What is the capital of India')

#print the content of the result
print(result.content)

#print(result)-> gives the whole response which includes the content and other metadata like usage, model, etc.