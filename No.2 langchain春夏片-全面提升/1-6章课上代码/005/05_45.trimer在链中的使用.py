from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, trim_messages, BaseMessage
from langchain_core.output_parsers import StrOutputParser

msg = [
    SystemMessage("你是一个漂亮年轻的李阿姨,实际年龄比我小"),
    HumanMessage("我是一个钛合金钢铁直男,48k纯爷们,碳纤维的,但是我是软饭男"),
    AIMessage("我给你我的附属金卡"),
    HumanMessage("你在教我做事啊?"),
]

#自定义的一个token计数器
def azu_token_counter(messages):
    total = 0
    for msg in messages:
        # print("msg.content=", msg.content)
        total += len(msg.content)
    # print("total=", total)
    return total  # 返回总共的token数


trimmer = trim_messages(
    max_tokens=30,
    token_counter=azu_token_counter,
    # strategy="last",  # strategy="last",#last从后截取
    strategy="last",  # strategy="last",#last从后截取
    # allow_partial = False,# first从前截取
    # "first", "last"
)
# result = trimmer.invoke(msg)#可以直接invoke调用
# print("result=",result)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
chain = trimmer | llm | StrOutputParser()
result = chain.invoke(msg)
print("result=",result)

