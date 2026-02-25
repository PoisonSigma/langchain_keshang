"""
prompts是提示的意思
Template模板
PromptTemplate提示词模板
"""
import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

"""
PromptTemplate.from_template类方法接收一个字符串模板作为输入，
该模板中可以包含使用花括号 {} 包裹的变量占位符，
这些占位符将在后续使用模板生成提示时被具体的值替换。其基本调用格式如下：
提示词模板作用:提升代码复用性,每次运行只需要把变量修改就行了,其他不变的不用改
format是将模板中的占位变量替换为实际的值
"""
prompt_template = PromptTemplate.from_template("你是一个天气预报系统请告诉我{city}{data}的天气预报")

msg = prompt_template.format(city="哈尔滨", data="明天")
print(msg)
# load_dotenv("../assets/openai.env")
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
# llm = ChatOpenAI(model=os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"),
                 #混元模型加上下面的
                 extra_body={
                     "enable_enhancement": True #自定义参数
                 }
                 )
response = llm.invoke(msg)
print(response.content)
