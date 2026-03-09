from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)

#logic: Here we are using the 
# HuggingFacePipeline to load a 
# local model called 'TinyLlama/TinyLlama-1.1B-Chat-v1.0'
#  for text generation. 
# We set the temperature to 0.5 and max_new_tokens to 100.
#  Then we create a ChatHuggingFace model using this 
# pipeline and invoke it with the prompt 
# "What is the capital of India". 
# Finally, we print the content of the result.