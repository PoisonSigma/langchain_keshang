import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessageChunk
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI

# t1 = PromptTemplate.from_template("当我玩{game}的时候,碰到一个人过来用{player}用{skill}磨我血,把我当电脑打,"
#                              "然后被我一挑三以后赖摇杆不好使,我要如何优雅的安抚他?")
# msg = t1.format(game = "拳皇97",player ="二阶堂红丸",skill="跳起来下重脚,再近身反半圆C")
# print(msg)
msg  = PromptTemplate.from_template("你好").format()
print(msg)
load_dotenv("../assets/openai.env")
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.8)
print("开始了吗?")
it1 = llm.stream(msg)
for item in it1:
    #print 方法的  end='\n 默认就是换行,这里面 end="" 是设置结尾是 空字符串
    # print(item.content , end="")
    ai1 = item.__add__(AIMessageChunk(content="面壁人常熟阿诺说:") + AIMessageChunk(content=" 那我问你:===>\n"))
    # print("ai1.content=",  ai1.content)
    print(ai1.content,end="")
    # print(item.content, end="")



print("\n第一次响应已经结束了")

# 逐步获取数据：每次调用 next(iterator) 时，迭代器会向 OpenAI 的 API 发送请求，获取一部分响应数据并返回。例如，模型可能会先返回一个词，然后再返回下一个词，这样就实现了逐步接收数据。
# 不立即结束循环：只要 OpenAI 的 API 还有数据可以返回，__next__ 方法就会持续返回新的元素，for 循环就会继续执行。只有当 API 没有更多数据，__next__ 方法抛出 StopIteration 异常时，for 循环才会结束。

