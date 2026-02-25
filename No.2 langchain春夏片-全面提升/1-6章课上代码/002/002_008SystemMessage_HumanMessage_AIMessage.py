"""
SystemMessage
出现次数：通常建议 SystemMessage 出现 0 到 1 次。
原因：SystemMessage 主要用于给 AI 提供一些全局的、背景性的信息，帮助 AI 理解它所处的角色和任务环境。例如在你的代码中，通过 SystemMessage 告知 AI 它是一个奇幻小说家且正在创作的小说名字。一般来说，这种全局的背景信息只需要提供一次就足够了，多次使用可能会让 AI 产生混淆或者导致信息冗余。
2. HumanMessage
出现次数：可以出现 0 次或多次。
原因：HumanMessage 模拟的是人类用户与 AI 的交互，在实际的对话场景中，用户可以多次向 AI 提问、发出指令或者提供新的信息。在你的代码里，有多个 HumanMessage 用于模拟不同阶段的用户提问，比如询问小说名字、询问小说内容、提出创作需求等，因此可以根据实际的对话流程灵活使用多个 HumanMessage。
3. AIMessage
出现次数：可以出现 0 次或多次。
原因：AIMessage 模拟的是 AI 对用户的回复。在一个完整的对话模拟中，当用户多次提问时，AI 也会相应地给出多次回复，所以 AIMessage 的数量通常与 HumanMessage 相呼应，以构建一个完整的对话历史。例如在你的代码中，针对用户询问小说名字和内容的问题，分别有对应的 AIMessage 给出回复。
"""
import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# sy = SystemMessage(
#     content="你是一个普通的上班族",additional_kwargs = {"你的名字是":"吉恶吉懂事"}
# )
# print(sy.additional_kwargs)
# hm = HumanMessage(content="你好,请告诉我你的名字")
# print(sy.additional_kwargs)
aiTemplate = "某个20岁少年{name},每顿饭吃100个鸡蛋,每天3万大卡热量摄入,深蹲时靠香草味的蛋白屁做蛋气加速,他的蛋白屁是真蛋白,就是未完全消化的蛋清混合气体,与地面反作用力,产生跳跃式加速深蹲,有时候蛋白屁里混合着小虾仁,会让速度加快,当速度接近光速的时候,因为爱因斯坦的狭义相对论,使时间静止,这时候{name}大喊一声:砸瓦鲁多,会让时间静止10秒,"
aiContent = aiTemplate.format(name = "脚脚")
print(aiContent)
template = ChatPromptTemplate.from_messages([
    # sy, hm,
    SystemMessage(content="你是奇幻小说家"),
    HumanMessage(
        content="你好,小说家,请问你的小说内容是什么样的"),
    AIMessage(
        content=aiContent),
    HumanMessage(content="我想要创作一部这样的小说,内容有文采一点优雅绅士一点,大概200字")
])
msg = template.format()
print()
#
load_dotenv("../assets/openai.env")
print(os.getenv("MODEL_NAME"))
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=1)
res = llm.invoke(msg)
print(res.content)
