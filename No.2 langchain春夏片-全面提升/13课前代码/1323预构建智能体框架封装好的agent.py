from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv("openai.env")

tool = TavilySearch(max_results=1)
tools = [tool]
# 这个相当于是封装后的操作,只简单的调用tool,没有其他复杂操作
from langgraph.prebuilt import create_react_agent
import os
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
# checkpointer = InMemorySaver()#创建内存检查点记忆
import sqlite3
# pip install langgraph-checkpoint-sqlite
from langgraph.checkpoint.sqlite import SqliteSaver# 需要安装包langgraph-checkpoint-sqlite
conn = sqlite3.connect("abc.db",check_same_thread=False)#创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
checkpointer = SqliteSaver(conn)#创建一个sqlite保存器

from pydantic import BaseModel
class JoJo(BaseModel):
    name: str
agent = create_react_agent(
    llm,
    tools,
    prompt="你是一个有用的代理",#提示词
checkpointer=checkpointer,
response_format=JoJo #用来结构化输出,这样大模型返回可以直接是JoJo类型


)
config = {"configurable": {"thread_id": "1"}}
# result = agent.invoke({"messages":[HumanMessage(content="我叫jojo")]},
# config
#                       )
# print(result)
# print(result["structured_response"])#解构化输出
result = agent.invoke({"messages":[HumanMessage(content="我叫什么?")]},
config
                      )
# print(result)
print("最终结果:",result["structured_response"])#解构化输出

for msg in result["messages"]:
    print(type(msg),msg.content)

#agent是封装好的固定的工作流,但是也能通过把graph改成agent打印图片
try:
    #display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = agent.get_graph().draw_mermaid_png()
    with open("agent.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：agent.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)