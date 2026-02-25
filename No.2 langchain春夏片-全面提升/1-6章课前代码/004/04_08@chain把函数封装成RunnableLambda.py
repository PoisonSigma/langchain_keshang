from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain, RunnableLambda
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop = "好",
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
@chain
def chain1(dic1:dict):
    text1 = dic1["text1"]
    text2 = dic1["text2"]
    print("传入的text1=",text1)
    print("传入的text2=", text2)
    text = text1 + text2
    print("组合后的text=", text)

    prmpt = ChatPromptTemplate.from_template("{str1}").partial(str1=text)
    print("prmpt=", prmpt)
    ai_msg = (prmpt | llm | StrOutputParser()).invoke({})
    #这里invoke里面只穿了{}一个空字典,因为上面提示词模板已经没有需要占位的了
    return ai_msg
# print(chain1)
# print(type(chain1))
# output = chain1.invoke({"text1":"你","text2":"好"})
#
#

# def add(a, b):
#     result = a + b
#     print("add",result)
#     return result
# async def sub(a,b):
#     result = a - b
#     print("sub", result)
#     return result
# # add(1,1)
# # asyncio.run( sub(2,1)) #直接调用异步方法,把协程放入事件循环,并且运行
# # runnable1 = RunnableLambda(lambda x :add(x[0],x[1]))
# runnable2 = RunnableLambda( lambda x :add(x[0],x[1]))#afunc参数可以传入 异步方法
# runnable3 = RunnableLambda( lambda x :chain1(x[0],x[1]))
chain1.invoke({"text1":1,"text2":2})