# 是指模型通过少量的示例来学习并完成特定任务。
import os
from sys import prefix

from dotenv import load_dotenv
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

fspt = FewShotPromptTemplate(
    #例子模板example_prompt
    example_prompt = PromptTemplate.from_template("你输入了一个{i}给出的输出是{o}"),
    #examples例子的队列,但是字典
    examples= [
    {"i": "橘子", "o": "水果"},
    {"i": "香蕉", "o": "水果"},
    {"i": "西瓜", "o": "水果"},
    {"i": "黄瓜", "o": "蔬菜"},
    {"i": "豆角", "o": "蔬菜"},

],
    #前缀prefix
    prefix = "请根据我提供的下列例子,进行推理",
    #后缀,suffix 放在整个提示词模板的结尾
    suffix = "请告诉我{name}对应的推理出来的词是什么"
)
msg = fspt.format(name="马铃薯")
print(msg)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)

