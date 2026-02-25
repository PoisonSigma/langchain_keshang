import asyncio
import os

from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
async def invoke1(llm:ChatDeepSeek,msg:str)->str:
    print("嘎斯罐1开始了↑")
    res = await llm.ainvoke(msg)#出现 await等待,就把控制权给其他协程
    print(res)
    print("1的结果",res.content)
    print("嘎斯罐1结束了了↑")
    return res.content

async def invoke2(llm:ChatDeepSeek,msg:str)->str:
    print("嘎斯罐2开始了↓")
    res = await llm.ainvoke()#出现 await等待,就把控制权给其他协程
    print(res)
    print("1的结果",res.content)
    print("嘎斯罐1结束了了↓")
    return res.content



load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
asyncio.run(invoke1(llm,"你好"))