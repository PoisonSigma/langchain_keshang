"""
Parser分析器的意思
BaseOutputParser 英文直译:基础输出分析器
LangChain 里，BaseOutputParser 是一个基类，
主要用于对语言模型的输出进行解析处理，
将模型输出的原始文本转换为特定的数据结构或格式，方便后续程序使用
"""
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.output_parsers.base import T
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 这里我们自定义的类psOutputParser继承自BaseOutputParser类,但是必须实现里面的抽象方法parse
# 这个parse就是把你输入的字符串返回,自己可以写自定义的格式
class PsOutputParser(BaseOutputParser):
    # parse是BaseOutputParser的@abstractmethod关键字声明的抽象方法,必须实现
    # 返回类型可以不写
    def parse(self, text: str) -> T:
        # return "阿祖の章:" + text
        list1 = text.split(",")#用逗号分隔字符串,并且组成List列表
        return  list1
"""

# result = PsOutputParser().parse("白金之星")
result = PsOutputParser().parse("白金之星,愚者,绿色法皇")
print(result)
for item in result:
    print(item)
"""
template = PromptTemplate.from_template(
    "告诉我jojo里面的{count}个中文替身名字,只要替身名,不要说替身使者名字,不要多余的符号,用逗号隔开")
msg = template.format(count=5)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"))
res = llm.invoke(msg)
print(res.content)
list2 = PsOutputParser().parse(res.content)
print(list2)
for item in list2:
    print(item)