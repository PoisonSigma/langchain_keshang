import os
import threading
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

def invoke1(llm:ChatDeepSeek,msg:str):
    print("线程开始了,提示词是:",msg)
    res = llm.invoke(msg)
    print(res.content)


load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
# thread1 = threading.Thread(invoke1(llm,"说词儿"))#错误,直接在主线程中完成方法
# thread2 = threading.Thread(invoke1(llm,"没感觉"))#错误,直接在主线程中完成方法
thread1 = threading.Thread(target=invoke1,args=(llm,"说词儿"))
thread2 = threading.Thread(target=invoke1,args=(llm,"没感觉"))
thread1.start()#开始线程
thread2.start()

thread1.join()#等线程执行完以后向下执行
thread2.join()
print("终于都执行完了,到我发挥用处")