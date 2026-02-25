import asyncio
import os

from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv


async def invoke1(llm: ChatDeepSeek, msg: str) -> str:
    print("嘎斯罐1开始了↑")
    # res = await llm.ainvoke(msg)#出现 await等待,就把控制权给其他协程
    # print(res)
    # print("1的结果",res.content)
    # print("嘎斯罐1结束了了↑")
    # return res.content
    # res = llm.stream(msg)
    # for item in res:
    #     print(item.content, end="")
    #语法async  for in,专门迭代异步的
    result:str =""
    async  for item in llm.astream(msg):
        print(item.content, end="")
        result+= item.content
    print("结果是:",result)
    return result
async def invoke2(llm: ChatDeepSeek, msg: str) -> str:
    print("嘎斯罐2开始了↓")
    res = await llm.ainvoke(msg)  # 出现 await等待,就把控制权给其他协程
    print(res)
    print("2的结果", res.content)
    print("嘎斯罐1结束了了↓")
    return res.content


async def start():
    load_dotenv("../assets/openai.env")
    llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
    (r1, r2) = await asyncio.gather(invoke1(llm, "嗯,没问题"), invoke2(llm, "实在吃不下了"))
    # (r1,r2) = res

    print(r1)
    print(r2)


asyncio.run(start())
