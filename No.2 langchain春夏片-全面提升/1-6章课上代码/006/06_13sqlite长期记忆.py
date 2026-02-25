import os

from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek
# from langgraph.checkpoint.memory import InMemorySaver

load_dotenv("../openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)


# 函数名也是工具名,但是@tool()装饰器,括号里面的字符串会覆盖工具名
# @tool
# @tool("伦敦东北人的发音")#错误,工具名不能是汉字
@tool("london_accent_speaker")
def london_accent_converter(text: str) -> str:
    """Convert text to London accent."""
    result = "张嘴一口地道的伦敦味 May I help you sir?" + text
    print(f"工具被执行{result}")
    return result  # 如果没有返回值,大模型就不用工具调用的结果,会自己想一出是一出,


print(f"工具名是:{london_accent_converter.name}")
# BaseCheckpointSaver
# checkpointer = InMemorySaver()

import sqlite3
# pip install langgraph-checkpoint-sqlite
from langgraph.checkpoint.sqlite import SqliteSaver# 需要安装包langgraph-checkpoint-sqlite
conn = sqlite3.connect("langgraph.db",check_same_thread=False)#创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
checkpointer = SqliteSaver(conn)#创建一个内存保存器
agent = create_agent(llm, [london_accent_converter],
                     system_prompt="你是个高冷的助手,只能说40字,多了就没钱坐2路汽车回家了",
                     checkpointer=checkpointer
                     )
# result = agent.invoke(
#     {"messages": [HumanMessage(content="你好,我是东北土鳖,想要假装从伦敦回来的,一嘴伦敦腔,请问,说你好怎么说?")]},
#      {"configurable": {"thread_id": "1"}}
# )
# print("result=", result)
# messages = result["messages"]
# print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
# print("最终答案:", messages[-1].content)
result = agent.invoke({"messages": [HumanMessage(content="我刚才问了什么?")]},
                      {"configurable": {"thread_id": "3"}})
for msg in result.get("messages"):
    print(msg.content)
