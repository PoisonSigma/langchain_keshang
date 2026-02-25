# interpreter中 package中添加langchain 和 langchain-openai
import os

from langchain.chat_models import init_chat_model
from ps_chat_models import init_chat_model as ps_chat_model
# print(ps_chat_model())
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv("../../assets/openai.env")
print(os.getenv("MODEL_NAME"))
print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("OPENAI_API_BASE"))
#
llm = ChatOpenAI(
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name=os.getenv("MODEL_NAME"),
    temperature=2  # 温度越低，精度越高，智能客服一般选择0，这样回答问题准确
    # openai_api_base="https://api.hunyuan.cloud.tencent.com/v1",
    # openai_api_key="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO",
    # model_name = "hunyuan-turbo"
)
print(llm)
response = llm.invoke("你好")
print(response)
print(response.content)
