import os

from dotenv import load_dotenv
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

examples = [
    {"game": "拳皇97", "skill": "八稚女", "sound": "犀利魔力多"},
    {"game": "拳皇97", "skill": "凤凰斩", "sound": "洗地的鸭子"},
    {"game": "守望先锋", "skill": "死亡绽放", "sound": "带带带"},
    {"game": "北斗神拳", "skill": "死亡一指", "sound": "o wa e wa mou xin dei yi lv"},
]
fspt = FewShotPromptTemplate(
    examples = examples,
    example_prompt= PromptTemplate.from_template("游戏的名称是{game}人物的超必杀是{skill},发出的空耳发音是{sound}"),
    prefix = "请根据下面给出的例子,游戏名,游戏的技能,和技能的空耳发音进行推理",
    suffix = "请告诉我,游戏{g}中的技能{k}的空耳发音是什么"
)
msg = fspt.format(g="拳皇97",k="大蛇薙")
print(msg)
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)

