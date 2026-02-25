import os

from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

#from langgraph.checkpoint.memory import InMemorySaver
#checkpoint是包含在langgraph包里面的,我们几个月之前录制的第13章内容,里面讲解了利用检查点对langgraph进行记忆操作,现在langchain直接照搬同样操作

#uv add langgraph-checkpoint-sqlite
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
#注意,需要到uv.lock里面查看langgraph版本是否是1.0.5如果不是删除掉uv.lock文件,然后uv sync同步,版本低的langgraph包里面没有checkpoint文件夹
# BaseCheckpointSaver

import sqlite3
# pip install langgraph-checkpoint-sqlite
#需要"langgraph>=1.0.5"
conn = sqlite3.connect("langgraph.db", check_same_thread=False)


from langgraph.checkpoint.sqlite import SqliteSaver
memory = SqliteSaver(conn)
agent = create_agent(llm, [london_accent_converter],
                     system_prompt="你是个高冷的助手,只能说40字,多了就没钱坐2路汽车回家了",
                     checkpointer=memory
                     )
result = agent.invoke(
    {"messages": [HumanMessage(content="你好,我是东北土鳖,想要假装从伦敦回来的,一嘴伦敦腔,请问,说你好怎么说?")]},
     {"configurable": {"thread_id": "1"}}
)
print("result=", result)
messages = result["messages"]
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("最终答案:", messages[-1].content)
result = agent.invoke({"messages": [HumanMessage(content="我刚才问了什么?")]},
                      {"configurable": {"thread_id": "1"}})
for msg in result.get("messages"):
    print(msg.content)
conn.close()  # 关键修复：释放文件句柄，确保数据完整写入
