#ChatOpenAI
import os

from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI

# https://python.langchain.com/v0.1/docs/integrations/chat/
# https://python.langchain.com/docs/integrations/chat/
# Chat models are language models that use a sequence of messages as inputs and
# return messages as outputs (as opposed to using plain text). These are generally newer models.
# 聊天模型是一种语言模型，它使用一系列消息作为输入，
# 并返回消息作为输出（与使用纯文本不同）。这些通常都是较新的型号。
#腾讯混元:https://python.langchain.com/v0.1/docs/integrations/chat/tencent_hunyuan/

#OpenAI
# https://python.langchain.com/v0.1/docs/integrations/llms/
# https://python.langchain.com/docs/integrations/llms/
# LLMs are language models that take a string as input and return a string as output.
# llm是一种语言模型，它接受一个字符串作为输入，并返回一个字符串作为输出。
msg = "你好"
load_dotenv("../assets/openai.env")
# llm = OpenAI(model=os.getenv("MODEL_NAME"), temperature=0.8)

llm = ChatOpenAI(model=os.getenv("MODEL_NAME"),
                 #如果是混元模型加上下面的enable_enhancement": True
                 extra_body={
                     "enable_enhancement": True #自定义参数
                 }
                 )
res = llm.invoke(msg)
print(res)
# print(res.content)