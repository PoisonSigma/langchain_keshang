import json
import os
from ctypes.wintypes import PSIZE

from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from langgraph.graph import StateGraph
from typing_extensions import TypedDict, Annotated

load_dotenv("openai.env")
from langchain_tavily import TavilySearch
tool = TavilySearch(max_results=2)
tools = [tool]
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)

from langgraph.graph.message import add_messages
class State(TypedDict):
    messages:Annotated[list,add_messages]
#创建节点函数
def chat_node (state:State):
        result = llm.bind_tools(tools).invoke(state["messages"])#这个是用大模型执行绑定的工具
        print("result=",result)
        if hasattr(result, "tool_calls" )  and result.tool_calls: #1.and 左边先判断对象result是否包含tool_calls属性或者方法 ,2and 右边如果左边有这个属性,再判断是否为空值null
            print("调用工具了")

        return  {"messages":[result]}#返回的结果通过add_messages追加的list的结尾
graph_builder = StateGraph(State)
graph_builder.add_node("chat_node",chat_node)
from langgraph.prebuilt import ToolNode, tools_condition
#ToolNode创建工具节点
tool_node = ToolNode(tools=[tool])#,参数tools=[tool]表示该节点关联的工具列表,ToolNode是 LangGraph 中用于处理工具调用的节点类,这个可以自己写,但是代码太多用框架写好的就行
#自定义工具节点
# class PsToolNode(ToolNode):
#     def __call__(self, inputs: dict):
#         # 打印工具调用的触发信息
#         print("\n===== 工具开始调用 =====")
#         # 调用父类的工具执行逻辑（获取结果）
#         result = super().__call__(inputs)
#         # 打印工具返回的原始结果
#         print("工具调用结果（ToolMessage）：", result["messages"])
#         # 解析 ToolMessage 的内容（工具返回的原始数据，如搜索结果）
#         for msg in result["messages"]:
#             print(f"工具 {msg.name} 返回的数据：{json.loads(msg.content)}")
#         print("===== 工具调用结束 =====\n")
#         return result
# tool_node = PsToolNode(tools=[tool])#使用自定义的工具节点
graph_builder.add_node("tools",tool_node)#添加工具节点
#add_conditional_edges创建带条件判断的边,参数1,是起始点,参数二框架自带的条件,如果llm不需要调用工具就走到end,如果需要调用工具就走到工具节点

#自定义的条件判断函数:
# 自定义条件函数，替代框架的 tools_condition
def custom_tools_condition(state: State):
    messages = state["messages"]
    if not messages:
        return END  # 无消息时结束
    last_msg = messages[-1]#-1是messsage中最后一个元素
    # 检查最后一条消息是否包含工具调用指令
    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        return "tools"  # 有工具调用，跳转到工具节点
    else:
        return END  # 无工具调用，结束流程
graph_builder.add_conditional_edges(
    "chat_node",#条件边的起点
    tools_condition,#框架定义好的条件,需要包含头文件:如果模型生成了最终答案就跳转到END,如果生成了调用工具指令tool_calls,则跳转到调用工具
# custom_tools_condition,#自定义的判断条件
)
graph_builder.add_edge(START,"chat_node")
graph_builder.add_edge("tools", "chat_node")#增加一个从tools返回到大模型的边
#“工具调用→结果处理→llm最终回答” 闭环逻辑的核心设计
#工具返回的是 “原始数据例如json”，需要大模型 “翻译” 成自然语言回答

graph = graph_builder.compile()

#生成图片
try:
    #display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = graph.get_graph().draw_mermaid_png()
    with open("openai_graph.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：langgraph_workflow.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)
ai_msg = graph.invoke({"messages":[HumanMessage(content="今天几号?查一下工具")]})

print(ai_msg)
