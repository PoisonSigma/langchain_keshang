
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")#注意../回退一个路径
from dotenv import load_dotenv

llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME")
)
response = llm.invoke("你好")
print(response)
print(">====)====(====>")
print(response.content)
