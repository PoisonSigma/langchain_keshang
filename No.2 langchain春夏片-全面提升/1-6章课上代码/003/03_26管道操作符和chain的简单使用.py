# 任何两个可运行对象可以“链式”组合成序列。
# 前一个可运行对象的 .invoke() 调用的输出作为输入传递给下一个可运行对象。
# 这可以使用管道操作符 | 或更明确的 .pipe() 方法来完成，二者效果相同。
from langchain_classic.chains.llm import LLMChain
from langchain_core.output_parsers import StrOutputParser
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv("../assets/openai.env")
prompt = ChatPromptTemplate.from_template(
    "你好,我是{city}{name}"
)
prompt2 = prompt.partial(city="哈尔滨")
print("prompt2=", prompt2)

msg = prompt2.format(name="吴彦祖")
print("msg=", msg)


load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop="好",
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
# chain = msg | llm #字符串不能参与管道操作符的调用
chain = prompt | prompt2 | prompt2  | llm
print("类型chain=", type(chain))
oldChain:LLMChain
# chain1:RunnableSequence #练真正的类型
# json = chain.model_dump_json()
# print("json=",json)#通过json查看chain里面的顺序
# ai_msg = chain.invoke({"name":"吴彦祖"})
# prompt2.invoke({"name":"吴彦祖"})#提示词模板的invoke要的input是一个字典,所以要用{}
# print("ai_msg=",ai_msg)
# str1:str = "你好{name}"
# msg2 = str1.format(name="彭于晏")#默认python的字符串str就有格式化
# print("msg2=",msg2)
