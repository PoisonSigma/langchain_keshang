import os
from sys import prefix

from dotenv import load_dotenv
from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

examples: list[dict[str, str]] = [
    # {"game": "kof97", "skill": "八稚女", "sound": "犀利魔力多"},
    {"game": "kof97", "skill": "凤凰斩", "sound": "洗地的鸭子"},
    {"game": "守望先锋", "skill": "死亡绽放", "sound": "带带带"},
    # {"game": "北斗神拳", "skill": "死亡一指", "sound": "o wa e wa mou xin dei yi lv"},
]
t1 = PromptTemplate.from_template("游戏名字{game}里的超必杀{skill}的空耳发音是{sound}")
# p1 = t1.format(game= "北斗神拳",skill = "死亡一指",sound = "o wa e wa mou xin dei yi lv")

# print(p1)
es1 = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=t1,
    max_length=13
)
# print(es1)
# l1 = es1.select_examples({"skill": "八酒杯"}, )
# print(l1)

# 是指模型通过少量的示例来学习并完成特定任务。

#cmd+左键点击类名FewShotPromptTemplate,找到继承的父类Mixin,_FewShotPromptTemplateMixin里面有examples和example_selector
# 并且找到如何这2个值都是None就提示,if examples is None and example_selector is None:
fspt = FewShotPromptTemplate(
    # examples=examples,  # 例子 这里是传入完整例子
    example_selector = es1,
    example_prompt=t1,  # 提示词模板
    prefix="请根据以下示例判断输入的游戏名字和技能名字的空耳发音",
    suffix="游戏名字{game}超必杀{skill}的空耳发音是:"  # 后缀,引导用户输入占位用的字符串
)
# print(fspt)
msg = fspt.format(game="kof97",skill="八稚女")
print(msg)

load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)
