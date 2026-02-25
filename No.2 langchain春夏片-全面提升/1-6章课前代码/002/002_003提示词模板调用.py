"""
prompts是提示的意思
Template模板
PromptTemplate提示词模板
"""
import os

from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import PromptTemplate
"""
PromptTemplate.from_template类方法接收一个字符串模板作为输入，
该模板中可以包含使用花括号 {} 包裹的变量占位符，
这些占位符将在后续使用模板生成提示时被具体的值替换。其基本调用格式如下：

"""
load_dotenv("../assets/openai.env")
print(os.getenv("OPENAI_API_BASE"))
prompt_template = PromptTemplate.from_template("你是一个天气预报系统告诉我{city}{data}的天气预报")
template_format = prompt_template.format(city="哈尔滨", data="明天")
print(template_format)
llm = ChatOpenAI(model = os.getenv("MODEL_NAME"))
response = llm.invoke(template_format)
print(response.content)

