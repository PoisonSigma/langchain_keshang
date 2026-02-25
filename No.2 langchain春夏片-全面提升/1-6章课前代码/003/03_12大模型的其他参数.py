#deepseek不限速:
# https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit
import json
import os
from datetime import datetime

from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
t1 = ChatPromptTemplate.from_template("你好,我叫{name},现在是{date},在这一分钟你会永远记住我")
print("t1类型",type(t1))
t2 = t1.partial(date= datetime.now().strftime("%Y年%m月%d日%H:%M:%S"))
print(t2)
# msg = t2.format(name = "哈尔滨吴彦祖")
# print(msg)
#注意下面的prompt传入的是BasePromptTemplate 提示词模板的子类,所以我们的t2:ChatPromptTemplate(BaseChatPromptTemplate),BaseChatPromptTemplate(BasePromptTemplate
# LLMChain(llm=llm,prompt=t2)#这种方法被废弃,使用RunnableSequence代替
"""Compose this Runnable with another object to create a RunnableSequence."""
#Runnable 可运行的
#Serializable序列化,串行
chain1:RunnableSerializable =  t2 | llm
print("chain1=",chain1)
dic = chain1.model_dump_json()#转为json字符串
print("dic=",dic)
json2 = {"a":123,"b":"abc"}
# first：这代表 RunnableSequence 序列里的首个可运行对象。
# last：它代表 RunnableSequence 序列里的最后一个可运行对象。
# middle：中间的对象,如果没有就是空,如果很多就是多个
# chain1.invoke()
print(chain1.model_dump_json())
# msg = chain1.format(name = "哈尔滨吴彦祖")#错误 RunnableSequence 没有format
res = chain1.invoke({"name":"哈尔滨吴彦祖"})
print("res=",res)











