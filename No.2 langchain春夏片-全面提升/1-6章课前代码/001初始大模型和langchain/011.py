"""
invoke 方法是 ChatOpenAI 类提供的一个用于与 OpenAI 模型进行交互的方法。
当你调用 invoke 方法并传入一个字符串（例如 "你好"）时，
该方法会将这个字符串作为输入发送给 OpenAI 的聊天模型，
模型会根据输入生成相应的回复，然后将回复返回。
"""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI


def hello_langchain():
    load_dotenv("../assets/openai.env")  # 注意../回退一个路径
    print(os.getenv("MODEL_NAME"))
    llm2 = ChatOpenAI(
        model=os.getenv("MODEL_NAME")
    )
    invoke = llm2.invoke("你好")
    print(invoke.content)


hello_langchain()
"""
{
    {
        # cmd+option+= - 进行代码折叠使用
    }
}

"""
