import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")

#安装包:langchain-tavily
from typing import TypedDict
from langchain_core.messages import HumanMessage
from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv("openai.env")
tool = TavilySearch(max_results = 2)
tools = [tool]
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("openai.env")
import os
load_dotenv("openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
class State(TypedDict):
    # messages 可以修改,这里作用的,保存聊天历史记录
    messages: Annotated[list,add_messages]#这个字段如果改了名字,那么调用工具会报错,需要用自定义的BasicToolNode修改这个字段  #Annotated []是泛型,list是类型,逗号后面add_messages是框架告诉处理数据的规则是添加合并


graph_builder = StateGraph(State)#创建工作流状态,这里,所有工作流只能处理messages,因为上面的State,只有一个字段
#创建节点函数
def chat_node(state:State):
    print("chat_node=state",state)
    result = llm.bind_tools(tools).invoke(state["messages"])
    print("chat_node result=",result)
    if hasattr(result,"tool_calls") and result.tool_calls:
        print("发现tool_calls 大模型想要调用工具")
        print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
    return {"messages":[result]}#返回的结果通过add_messages追加的list的结尾

graph_builder.add_node("chat_node",chat_node)#添加节点

graph_builder.add_edge(START,"chat_node")
from langgraph.prebuilt import ToolNode, tools_condition
#ToolNode创建工具节点
tool_node = ToolNode(tools)#框架生成的创建节点的类
graph_builder.add_node("tools",tool_node)#,参数tools=[tool]表示该节点关联的工具列表,ToolNode是 LangGraph 中用于处理工具调用的节点类,这个可以自己写,但是代码太多用框架写好的就行
#add_conditional_edges增加条件判断的边
#创建带条件判断的边,参数1,是起始点,参数二框架自带的条件,
# 如果llm不需要调用工具就走到end,如果需要调用工具就走到工具节点

#tools_condition框架创建的工具判断条件
graph_builder.add_conditional_edges("chat_node",tools_condition)

graph_builder.add_edge("tools","chat_node")
graph = graph_builder.compile()
#可视化图
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
graph_result = graph.invoke({"messages":["今天几号?请查一下工具"]})
print("result=",graph_result)
