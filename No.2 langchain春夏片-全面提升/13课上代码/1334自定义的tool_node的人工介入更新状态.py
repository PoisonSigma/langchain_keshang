import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")

# 安装依赖
# pip install -U "langchain[openai]" langchain-tavily
import json
import os
from typing import Annotated, List, Dict, Any
from typing_extensions import TypedDict
from langchain_tavily import TavilySearch
from langchain_core.messages import ToolMessage, HumanMessage, AIMessage, BaseMessage
from langchain_core.tools import BaseTool, tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import tools_condition
from langgraph.types import Command, interrupt


# 1. 定义自定义状态
class State(TypedDict):
    messages: Annotated[list, add_messages]  # 消息列表（带自动追加功能）
    answer: str  # 最终答案


# 2. 定义人机交互工具
@tool
def human_assistance(
        answer: str,
        tool_call_id: str  # 移除了InjectedToolCallId注解
) -> str:

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
        tool_call_id: str# 移除了InjectedToolCallId注解
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

# 环境设置
from dotenv import load_dotenv

load_dotenv("openai.env")

# 3. 配置工具和LLM
import os
from langchain_deepseek import ChatDeepSeek

# 初始化LLM
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
    temperature=0.8
)

# 初始化工具
tool = TavilySearch(max_results=2)  # 搜索工具
tools = [tool, human_assistance, abc]  # 注册工具列表
llm_with_tools = llm.bind_tools(tools)  # 将工具绑定到LLM


# 4. 定义聊天机器人节点
def chatbot(state:State):
    print("chatbot=state",state)
    result = llm.bind_tools(tools).invoke(state["messages"])
    return {"messages": [result]}  # 返回的结果通过add_messages追加的list的结尾


# 5. 构建流程图
graph_builder = StateGraph(State)

# 添加节点
graph_builder.add_node("chatbot", chatbot)  # 聊天机器人节点


# 修复工具节点
class BasicToolNode:
    """自定义工具节点，正确处理工具调用"""

    def __init__(self, tools: List[BaseTool]) -> None:
        self.tools = {tool.name: tool for tool in tools}

    def __call__(self, state: State) -> Dict[str, Any]:
        print("BasicToolNode __call__ 执行")
        messages = state["messages"]
        last_message = messages[-1]

        if not hasattr(last_message, "tool_calls") or not last_message.tool_calls:
            return {"messages": []}

        tool_messages = []
        for tool_call in last_message.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tool_id = tool_call["id"]

            print(f"调用工具: {tool_name}({tool_args})")

            if tool_name in self.tools:
                # 特殊处理human_assistance 和 abc 工具
                if tool_name == "human_assistance":
                    # 直接调用函数，不再使用invoke方法
                    result = human_assistance.func(
                        answer=tool_args["answer"],  # 传递 answer
                        tool_call_id=tool_id
                    )
                if tool_name == "abc":
                    #.func()是langchian框架直接调用函数，不再使用invoke方法
                    result = abc.func(
                        answer=tool_args["answer"],  # 传递 answer
                        tool_call_id=tool_id
                    )
                else:
                    # 其他工具正常调用
                    result = self.tools[tool_name].invoke(tool_args)

                # 如果result是Command对象，需要特殊处理
                if isinstance(result, Command):
                    # 更新状态
                    #Command.update 是一个字典，包含要更新的状态字段（例如 messages 和 answer）。
                    state_update = result.update
                    state["answer"] = state_update["answer"]#把State的字段更新
                    # 添加ToolMessage到消息列表
                    tool_messages.append(state_update["messages"][0])
                else:
                    # 普通工具结果
                    tool_messages.append(
                        ToolMessage(
                            content=str(result),
                            name=tool_name,
                            tool_call_id=tool_id
                        )
                    )
            else:
                tool_messages.append(
                    ToolMessage(
                        content=f"未知工具: {tool_name}",
                        name="system",
                        tool_call_id=tool_id
                    )
                )

        return {"messages": tool_messages}


tool_node = BasicToolNode(tools)
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
