import os
from abc import ABC, abstractmethod

from dotenv import load_dotenv
from langchain_core.example_selectors import LengthBasedExampleSelector, BaseExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

examples = [
    {"i": "橘子", "o": "水果"},
    {"i": "香蕉", "o": "水果"},
    {"i": "西瓜", "o": "水果"},
    {"i": "黄瓜", "o": "蔬菜"},
    {"i": "∂", "o": "蔬菜"},
# {True:False}
]

#创建一个长度示例选择器,他的作用是把整个例子,按照长度截取
t1 = PromptTemplate.from_template("我输入了一个{i},推理出一个{o}")
s1 = LengthBasedExampleSelector(
example_prompt=t1,
examples = examples,
max_length= 6,
)
print(s1)

fspt = FewShotPromptTemplate(
example_selector = s1,
example_prompt = t1,
    # 前缀prefix
    prefix="请根据我提供的下列例子,进行推理",
    # 后缀,suffix 放在整个提示词模板的结尾
    suffix="请告诉我{name}对应的推理出来的词是什么"
)
msg = fspt.format(name = "西红柿")
print(msg)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)
# class Person(ABC):#继承自ABC的类,如果没有抽象方法,依然可以实例化,但是有抽象方法就不能实例化
#     @abstractmethod
#     def breath(self):
#         pass
#
# Person()