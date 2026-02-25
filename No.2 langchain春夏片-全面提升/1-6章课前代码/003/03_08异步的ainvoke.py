import asyncio
import os
import time

from langchain_community.tools.steamship_image_generation.tool import ModelName
from langchain_deepseek import ChatDeepSeek

#
# async def fun1():
#     print("开始↑")
#     # await time.sleep(1)#注意,普通的sleep不会交出控制权
#     await asyncio.sleep(1)
#     print("结束↑")
#     return "嘎斯罐1放完了"
#
# async def fun2():
#     print("开始↓")
#     time.sleep(1)
#     print("结束↓")
#     return "嘎斯罐2放完了"
# async def start():
#     (r1,r2) = await asyncio.gather(fun1(), fun2())
#     print(r1)
#     print(r2)
#
# asyncio.run(start())

from dotenv import load_dotenv


async def invoke1(llm:ChatDeepSeek,msg:str):
    print("开始↑")
    # await time.sleep(1)#注意,普通的sleep不会交出控制权
    res = await llm.ainvoke(msg)
    print(res.content)
    print("1的执行结果:",res)
    print("结束↑")
    return "嘎斯罐1放完了"
async def invoke2(llm:ChatDeepSeek,msg:str):
    print("开始↓")
    # await time.sleep(1)#注意,普通的sleep不会交出控制权
    res = await llm.ainvoke(msg)
    print(res.content)
    print("2的执行结果:",res)
    print("结束↓")
    return "嘎斯罐2放完了"
async def runAinvoke():
    load_dotenv("../assets/openai.env")
    llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"))
    await asyncio.gather(invoke1(llm,"你好"),invoke2(llm,"哈喽啊"))
asyncio.run(runAinvoke())