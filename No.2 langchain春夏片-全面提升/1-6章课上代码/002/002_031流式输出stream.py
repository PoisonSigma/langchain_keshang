import os
from typing import Iterator
from dotenv import load_dotenv
from langchain_core.messages import BaseMessageChunk, AIMessageChunk
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# msg = PromptTemplate.from_template("你好").format()
# print(msg)
msg = "你好"
load_dotenv("../assets/openai.env")
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.8)
# res = llm.invoke(msg)
# print(res.content)
# it1:Iterator[BaseMessageChunk]  = llm.stream(msg)
# for item in it1:
#     print(item.content, end="====>")
# print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
it2 = llm.stream(msg)
for item in it2:
    # AIMessageChunk
    # BaseMessageChunk
    newResult = item.__add__(
        AIMessageChunk(content=">===阿诺说: ") + AIMessageChunk(content=" 那我问你") + AIMessageChunk(
            content=" 那我问你2==>\n"))
    # print(item.content,end="")
    print(newResult.content, end="")
    # next(it2)
