import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")

# 安装依赖
# pip install -U "langchain[openai]" langchain-tavily
import json
import os
from typing import Annotated


from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_core.messages import ToolMessage, HumanMessage
from langchain_core.tools import InjectedToolCallId, tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.types import Command, interrupt

# 1. 定义自定义状态
class State(TypedDict):
    messages: Annotated[list, add_messages]  # 消息列表（带自动追加功能）
    answer: str  # 最终答案

@tool
def human_assistance(
        answer: str,
        tool_call_id: Annotated[str, InjectedToolCallId]#这个是自动设置id,非自定义的node
)->str:

    """请求人类审核信息"""
    # 中断流程，等待人类输入
    print("human_assistance人类审核 tool_call_id=", tool_call_id)
    toolMsg_content = ""
    final_answer = ""
    human_response = interrupt(
        {"question": "这个对吗?",
            "answer": answer,}
    )
    if human_response == "对":
        toolMsg_content = f"正确{human_response}"
        final_answer = answer
    else:
        toolMsg_content = f"人类修改后{human_response}"
    state_update = {
        "messages":[ToolMessage(content=toolMsg_content,tool_call_id=tool_call_id)],
        "answer": final_answer  # 最终答案
    }
    print("abc state_update=",state_update)
    # 工具需要返回Command对象更新状态
    return Command(update=state_update)
@tool
def abc(
        answer: str,
        tool_call_id: Annotated[str, InjectedToolCallId]#这个是自动设置id,非自定义的node
)->str:

    """请求人类审核信息"""
    # 中断流程，等待人类输入
    print("abc人类审核 tool_call_id=", tool_call_id)
    toolMsg_content = ""
    final_answer = ""
    human_response = interrupt(
        {"question": "这个对吗?",
            "answer": answer,}
    )
    if human_response == "对":
        toolMsg_content = f"正确{human_response}"
        final_answer = answer
    else:
        toolMsg_content = f"人类修改后{human_response}"
    state_update = {
        "messages":[ToolMessage(content=toolMsg_content,tool_call_id=tool_call_id)],
        "answer": final_answer  # 最终答案
    }
    print("abc state_update=",state_update)
    # 工具需要返回Command对象更新状态
    return Command(update=state_update)
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv("openai.env")
tool = TavilySearch(max_results = 2)
tools = [tool,abc,human_assistance]
# 4. 定义聊天机器人节点

from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
def chatbot(state:State):
    print("chatbot=state",state)
    result = llm.bind_tools(tools).invoke(state["messages"])
    return {"messages": [result]}  # 返回的结果通过add_messages追加的list的结尾
graph_builder = StateGraph(State)#创建工作流状态,这里,所有工作流只能处理messages,因为上面的State,只有一个字段
graph_builder.add_node("chatbot", chatbot) # 聊天机器人节点
graph_builder.set_entry_point("chatbot")
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)# 工具调用节点
# 添加条件边
graph_builder.add_conditional_edges("chatbot",tools_condition)
graph_builder.add_edge("tools","chatbot")
# 编译图（启用内存检查点以保存状态）
memory = InMemorySaver()
graph = graph_builder.compile(checkpointer=memory)
user_input = "你能查一下langgraph最新版吗?当有答案时,使用工具 bcd进行审核" #如果指定工具不存在,大模型也会找一个审核工具进行审核
config = {"configurable": {"thread_id": 1}}
result = graph.invoke({"messages":[HumanMessage(content=user_input)]},config =config)#注意这里让大模型调用的工具名就算没有匹配上,但是前面tools里面只有3个工具,大模型也会找到人类审核工具并且调用
# print("result=",result)
# for msg in result["messages"]:
#     # print(type(msg),msg.content)
#     msg.pretty_print()
#可视化图
user_input = input("请人类大人审核:\n")
result = graph.invoke(Command(resume=user_input),config =config)#注意这里让大模型调用的工具名就算没有匹配上,但是前面tools里面只有3个工具,大模型也会找到人类审核工具并且调用
print("===========塞够诺塞够 最终的最终========")
for msg in result["messages"]:
    # print(type(msg),msg.content)
    msg.pretty_print()
try:
    #display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = graph.get_graph().draw_mermaid_png()
    with open("人工介入更新状态.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：人工介入更新状态.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)

