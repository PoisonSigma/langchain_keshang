import asyncio
import os
import threading
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek


# 准备把下面函数加入线程
def invoke1(llm:ChatDeepSeek,msg:str):
        print("线程开始", msg)
        res = llm.invoke(msg)
        print("1的结果是",res.content)
        print("线程结束", msg)


def invoke2(llm: ChatDeepSeek, msg: str):
    print("线程开始", msg)
    res = llm.invoke(msg)
    print("1的结果是", res.content)
    print("线程结束", msg)




load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"))


# thread1 = threading.Thread(invoke1(llm,"你好"))
thread1 = threading.Thread(target = invoke1 ,args =(llm,"你好"))
thread1.start()
# thread2 = threading.Thread(invoke2(llm,"说词儿"))
thread2 = threading.Thread(target = invoke2 ,args =(llm,"hello"))
thread2.start()
# 等待所有线程完成
thread1.join()#等待线程执行完才向下执行
thread2.join()
print("结束")
