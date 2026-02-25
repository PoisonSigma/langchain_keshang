# interpreter中 package中添加langchain 和 langchain-openai
import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv("../../assets/openai.env")#注意../回退一个路径
# print(os.getenv("NAME"))
from dotenv import load_dotenv

# llm = ChatOpenAI(
#     # openai_api_base="https://api.hunyuan.cloud.tencent.com/v1", # 混元 endpoint
#     # openai_api_key="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO",
#     # model_name="hunyuan-turbo",
# openai_api_base=os.getenv("OPENAI_API_BASE"), # 混元 endpoint
#     openai_api_key=os.getenv("OPENAI_API_KEY"),
#     model_name=os.getenv("MODEL_NAME")
# )
llm = ChatOpenAI(
    # openai_api_base="https://api.hunyuan.cloud.tencent.com/v1", # 混元 endpoint
    # openai_api_key="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO",
    # model_name="hunyuan-turbo",
openai_api_base=os.getenv("OPENAI_API_BASE"), # 混元 endpoint
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name=os.getenv("MODEL_NAME")

)
response = llm.invoke("你好")
print(response)
print(">====)====(====>")
print(response.content)
