import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")

#时间回溯的主要方法:通过graph.get_state_history 获取状态快照的list,
# 遍历里面的状态快照,保存想要回溯的状态快照,再用graph.invode( 状态快照.config)去从某个检查点开始执行
#这样可以不用重复输入之前的上下文,就是不需要前2轮的对话

import os
from typing import Annotated
from typing_extensions import TypedDict

# 导入LangChain相关模块
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


# 1. 初始化LLM（需替换为自己的API密钥）
from dotenv import load_dotenv
load_dotenv("openai.env")
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)

# 2. 定义图的状态（存储对话消息）
class State(TypedDict):
    # 用add_messages注解自动处理消息列表的追加
    messages: Annotated[list[BaseMessage], add_messages]


# 3. 构建图
graph_builder = StateGraph(State)

# 定义工具（Tavily搜索）
tool = TavilySearch(max_results=2)
tools = [tool]
llm_with_tools = llm.bind_tools(tools)  # 将工具绑定到LLM


# 4. 定义节点：聊天机器人节点（生成响应或调用工具）
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)  # 添加聊天机器人节点




# 5. 定义工具节点（执行工具调用）
tool_node = ToolNode(tools=[tool])
graph_builder.add_node("tools", tool_node)  # 添加工具节点


# 6. 定义边（控制节点间的流转）
# 从chatbot节点根据工具调用情况跳转（有工具调用则去tools节点，否则结束）
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,  # 内置条件：判断是否需要调用工具
)
# 工具调用完成后返回chatbot节点继续处理
graph_builder.add_edge("tools", "chatbot")
# 从起始节点进入chatbot节点
graph_builder.add_edge(START, "chatbot")


# 7. 编译图（启用检查点以支持时间回溯）
memory = InMemorySaver()  # 用内存存储检查点（生产环境可替换为持久化存储）
graph = graph_builder.compile(checkpointer=memory)


# 8. 与图交互（添加对话步骤，生成检查点）
config = {"configurable": {"thread_id": "1"}}  # 用thread_id区分不同对话线程
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
user_input = "如何刷脂?20字以内回答"
result = graph.invoke({"messages": [HumanMessage(content=user_input)]},config)
user_input = "如何2小时之内刷脂的同时再增肌?20字以内回答"
result = graph.invoke({"messages": [HumanMessage(content=user_input)]},config)
for msg in result["messages"]:
    msg.pretty_print()

print("\n===== 时间回溯 =====")
replay_snapshot = None #保存状态快照的
for snapshot in graph.get_state_history(config):
    print(f"消息个数{len(snapshot.values["messages"])},下一个节点是:{snapshot.next}")
    if len(snapshot.values["messages"]) == 3:
        replay_snapshot = snapshot #保存,消息总是是2的状态快照

print("\n===== 从回溯点恢复执行 =====")
print("replay_snapshot.config=",replay_snapshot.config)
# result = graph.invoke(None,replay_snapshot.config)#None是不添加新的,用之前检查点保存 的聊天记录
user_input = "如何快速增肥变成大囗袋?20字之内回答"
result = graph.invoke({"messages": [HumanMessage(content=user_input)]},replay_snapshot.config)
for msg in result["messages"]:
    msg.pretty_print()


try:
    #display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = graph.get_graph().draw_mermaid_png()
    with open("时光回溯.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：时光回溯.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)