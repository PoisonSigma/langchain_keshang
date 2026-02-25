# interpreter中 package中添加langchain 和 langchain-openai
import os
from tkinter.font import names
from typing import Optional # 使用Optionnal

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_openai.chat_models.base import BaseChatOpenAI

load_dotenv("../../assets/openai.env")#注意../回退一个路径
# print(os.getenv("NAME"))
from dotenv import load_dotenv
#self.openai_api_base = self.openai_api_base or os.getenv("OPENAI_API_BASE")
#
llm = ChatOpenAI(
    # openai_api_base="https://api.hunyuan.cloud.tencent.com/v1", # 混元 endpoint
    # openai_api_key="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO",
    # model_name="hunyuan-turbo",
# openai_api_base=os.getenv("OPENAI_API_BASE"), # 混元 endpoint
#     openai_api_key=os.getenv("OPENAI_API_KEY"),
#     model_name=os.getenv("MODEL_NAME")
# openai_api_base=os.getenv("OPENAI_API_BASE"), # 混元 endpoint
    # openai_api_key=os.getenv("OPENAI_API_KEY"),
openai_api_base="https://api.hunyuan.cloud.tencent.com/v1", # 混元 endpoint
    openai_api_key="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO",
    model=os.getenv("MODEL_NAME")

)
#
# response = llm.invoke("你好")
# print(response)
# print(">====)====(====>")
# print(response.content)

# 使用 or 运算符实现类似 ?? 的效果
age : Optional[int] = None
age2 = age or 99
print(age2)
value = None
default_value = 10

def add(a:int,b:Optional[int] = None):
    print(a + (b or 99))#如果b的值是None就让 a + 99
add(3)#可以不传值,因为有默认值=None