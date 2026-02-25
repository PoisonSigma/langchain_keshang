import os

from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     # stop = "三",#下面的bind相当于这里填入
     # stop = "很",
     temperature=0.8)
###卡卡一顿运行
#bind会绑定一个参数给大模型,返回一个新的Ranable
llm2 = llm.bind(stop = "好")#这里的stop参数必须在上面的rannable对象里面真能使用
# ai_msg = llm.invoke("你好")#不invoke执行的时候 上面绑定的参数即使不存在,也不会报错,运行invoke才会真的检查
chain = llm2 | StrOutputParser()
ai_msg = chain.invoke("你好")
print(ai_msg)



