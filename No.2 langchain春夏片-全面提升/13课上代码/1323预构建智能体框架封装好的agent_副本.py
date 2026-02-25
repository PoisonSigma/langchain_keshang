
import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")


#langgraph里面不在处理agent,只负责节点流程,所有agent代理转移到每个langgraph节点里使用langchain调用agent
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv("openai.env")
tool = TavilySearch(max_results=1)
tools = [tool]
import os
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8)
from langgraph.checkpoint.memory import MemorySaver
# checkpointer = MemorySaver()#创建一个内存保存器
import sqlite3
# pip install langgraph-checkpoint-sqlite
from langgraph.checkpoint.sqlite import SqliteSaver  # 需要安装包langgraph-checkpoint-sqlite
from langgraph.graph import StateGraph

conn = sqlite3.connect("langgraph.db", check_same_thread=False)  # 创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
checkpointer = SqliteSaver(conn)  # 创建一个内存保存器
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel
# 统一使用Pydantic v2的组件
from pydantic import BaseModel, Field  # 关键：v2的BaseModel和Field


class JoJo(BaseModel):
    name: str = Field(default="无名氏", description="姓名")
    age: int = Field(default=0, description="年龄")


from langchain.agents import create_agent

# agent = create_react_agent(
agent = create_agent(
    llm,
    tools,
    system_prompt="你是一个有用的代理",
    # prompt="你是一个有用的代理",
    checkpointer=checkpointer,
    response_format=JoJo
)
config = {"configurable": {"thread_id": 3}}
result = agent.invoke({"messages": [HumanMessage(content="我叫jojo我18岁")]}, config)
print("result=", result)
for msg in result["messages"]:
    print(type(msg), msg.content)
print(result["structured_response"])

try:
    # display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = agent.get_graph().draw_mermaid_png()
    with open("agent.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：agent.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=", e)
