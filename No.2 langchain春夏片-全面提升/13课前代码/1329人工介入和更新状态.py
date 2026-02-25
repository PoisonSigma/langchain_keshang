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


# 2. 定义人机交互工具
@tool
def human_assistance(
        answer: str,
        tool_call_id: Annotated[str, InjectedToolCallId]#这个是自动设置id,非自定义的node
) -> str:

    """请求人类审核信息"""
    # 中断流程，等待人类输入
    print("human_assistance 人类审核节点执行:tool_call_id=", tool_call_id)
    human_response = interrupt(
        {
            "question": "这个对吗?",
            "answer": answer,
        },
    )

    # 根据人类反馈更新状态
    final_answer = ""#最终答案
    response = ""
    if human_response == "对":
        final_answer = answer #如果正确,那么最终答案就是入参answer,不改变值
        response = "正确"
    else:#如果键盘输入人类审核不是"对",就把最终答案变成键盘输入
        final_answer = human_response
        response = f"人类修改: {human_response}"

    # 构建状态更新指令
    state_update = {
        "answer": final_answer,
        "messages": [ToolMessage(content=response, tool_call_id=tool_call_id)],
    }
    # 工具需要返回Command对象更新状态
    return Command(update=state_update)
@tool
def abc(
        answer: str,
        tool_call_id: Annotated[str, InjectedToolCallId]#这个是自动设置id,非自定义的node
) -> str:

    """请求人类审核信息"""
    # 中断流程，等待人类输入
    print("abc 人类审核节点执行:tool_call_id=", tool_call_id)
    human_response = interrupt(
        {
            "question": "这个对吗?",
            "answer": answer,
        },
    )

    # 根据人类反馈更新状态
    final_answer = ""#最终答案
    response = ""
    if human_response == "对":
        final_answer = answer #如果正确,那么最终答案就是入参answer,不改变值
        response = "正确"
    else:#如果键盘输入人类审核不是"对",就把最终答案变成键盘输入
        final_answer = human_response
        response = f"人类修改: {human_response}"

    # 构建状态更新指令
    state_update = {
        "answer": final_answer,
        "messages": [ToolMessage(content=response, tool_call_id=tool_call_id)],
    }
    # 工具需要返回Command对象更新状态
    return Command(update=state_update)
from dotenv import load_dotenv
load_dotenv("openai.env")
# 3. 配置工具和LLM
search_tool = TavilySearch(max_results=2)  # 搜索工具
tools = [search_tool, human_assistance,abc]  # 注册工具列表
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
llm_with_tools = llm.bind_tools(tools)  # 将工具绑定到LLM


# 4. 定义聊天机器人节点
def chatbot(state: State):
    print("chatbot执行 state=",state)
    """处理消息并生成响应"""
    message = llm_with_tools.invoke(state["messages"])
    assert len(message.tool_calls) <= 1  # 限制单次调用一个工具
    return {"messages": [message]}


# 5. 构建流程图
graph_builder = StateGraph(State)

# 添加节点
graph_builder.add_node("chatbot", chatbot)  # 聊天机器人节点
tool_node = ToolNode(tools=tools)

graph_builder.add_node("tools", tool_node)  # 工具调用节点

# 添加边
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,  # 根据是否调用工具决定流向
)
graph_builder.add_edge("tools", "chatbot")  # 工具调用后返回聊天机器人
graph_builder.add_edge(START, "chatbot")  # 起始点连接聊天机器人

# 编译图（启用内存检查点以保存状态）
memory = InMemorySaver()
graph = graph_builder.compile(checkpointer=memory)

# 6. 运行示例
if __name__ == "__main__":
    # 配置线程ID（用于多轮对话追踪）


    # 用户输入：查询LangGraph发布日期并请求人类审核
    user_input = (
        """你能查一下langgraph最新版本吗？
        当有答案时，使用abc工具进行审查。"""
    )#注意这里让大模型调用的工具名就算没有匹配上,但是前面tools里面只有2个工具,大模型也会找到人类审核工具并且调用

    # 流式运行图
    print("=== 对话流程 ===")
    config = {"configurable": {"thread_id": "1"}}
    result = graph.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config
    )
    print("result=",result)
    #打印整个流程调用过程:
    for msg in result["messages"]:
        print(type(msg),msg.content)
        # if hasattr(msg,
        #            "tool_calls") and msg.tool_calls:
        #     print("调用工具了")
        #     print("msg.tool_calls=",msg.tool_calls)

    # 模拟人类审核（修正错误信息）
    print("\n=== 人类审核输入 ===")
    user_input = input("人类审核输入:\n")
    human_command = Command(
        resume=user_input
    )
    result = graph.invoke(human_command, config)
    for event in result["messages"]:
            event.pretty_print()
