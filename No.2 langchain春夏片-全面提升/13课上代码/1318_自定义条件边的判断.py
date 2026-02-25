import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")

#安装包:langchain-tavily
import json
from typing import TypedDict
from langchain_core.messages import HumanMessage, ToolMessage
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
    messages: Annotated[list,add_messages]  #Annotated []是泛型,list是类型,逗号后面add_messages是框架告诉处理数据的规则是添加合并


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
# tool_node = ToolNode(tools)#框架生成的创建节点的类
# name: str = "tavily_search"
# [tool1,tool2]

#自定义的可以修改字典里面的非标准key
class BasicToolNode:
    def __init__(self,tools:list):
        # for tool in tools:
        #     self.tool_dic[tool.name] = tool
        self.tool_dic = {  tool.name:tool for tool in tools}
            # 如果有2个tool,一个名字叫:langSearch,一个叫:TavilySearch ,那么这里结果就是:
            # {"tavily_search":tool,"lang_search":tool2}
        # 这段代码的核心逻辑是处理大模型生成的最后一条信息,遍历里面的工具,再让里面的参数args传给要调用的工具,通过工具名字的字典遍历
    def __call__(self, inputs:dict) :#__call__作用是对象可以直接传入参数当函数用
        print("BasicToolNode __call__: inputs=", inputs)
        if messages := inputs.get("messages", []):
            message = messages[-1]#-1是list里面的最后一个元素,每次
        else:
            raise ValueError("message为空")
        finalresult = []
        for tool_call in message.tool_calls:
            tool_result =self.tool_dic[tool_call["name"]] .invoke(tool_call["args"])
            finalresult.append(ToolMessage(
                content=json.dumps(tool_result),  # 序列化为 JSON 字符串
                name=tool_call["name"],  # tool_call是for 遍历的子工具
                tool_call_id=tool_call["id"],
            ))
        return {"messages":finalresult}
tool_node = BasicToolNode(tools)
# tool_node({"messages":[tool,tool2]})

graph_builder.add_node("tools",tool_node)#,参数tools=[tool]表示该节点关联的工具列表,ToolNode是 LangGraph 中用于处理工具调用的节点类,这个可以自己写,但是代码太多用框架写好的就行
#add_conditional_edges增加条件判断的边
#创建带条件判断的边,参数1,是起始点,参数二框架自带的条件,
# 如果llm不需要调用工具就走到end,如果需要调用工具就走到工具节点

#tools_condition框架创建的工具判断条件
def route_tools(
        state:State# 接收当前图的状态（包含对话历史等信息）
):
    print("route_tools=state", state)  # 先打印state
    print("state类型是:", type(state))
    # 第一步：从状态中提取最新的AI消息

    if messages := state.get("messages", []):
        # 这里是判断如果state是字典类型,就取里面的messages的最后一个元素,把他当做ai_message
        # 先把state里面的"messages" 的值赋值给messages,如果没有这个key value,那么就赋值成[]空列表,再判断messages,如果是空列表就走到下面的else,抛出异常
        ai_message = messages[-1]
    else:
        # 若状态中无消息，抛出异常（避免流程中断）
        raise ValueError("route_tools state中没有找到messages")

    # 第二步：判断是否需要调用工具
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        # 若最新消息包含工具调用指令且调用列表非空，返回"tools"（指向工具节点）
        return "ducks"
    # 若无需工具调用，返回END（流程终止）
    # return END
    return "ende"
graph_builder.add_conditional_edges("chat_node",
                                    route_tools,#这个是我们自定义的工具路由函数,通过返回值来决定走到哪个节点,
                                    # 返回值不用非要是真实节点名,通过参数3映射到真实节点名
                                    {"ducks":"tools","ende":END})

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
graph_result = graph.invoke({"messages":["今天几号?查一下工具吧,三分钟我要调用这个工具的全部信息"]})
print("graph_result=",graph_result)
for message in graph_result["messages"]:
    print(type(message), message.content)
# {'messages':
 #      [HumanMessage(content='今天几号?查一下工具吧,求求了,我还没吃晚饭,录完课还得去撸铁呢', additional_kwargs={}, response_metadata={}, id='92397d5a-f5e9-482a-9314-8885e444491a'),
 #       AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_0_cbed64bd-99d5-4b14-ade8-da2e9aef4f77', 'function': {'arguments': '{"query":"今天几号","search_depth":"basic"}', 'name': 'tavily_search'}, 'type': 'function', 'index': 0}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 28, 'prompt_tokens': 1968, 'total_tokens': 1996, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 1920}, 'prompt_cache_hit_tokens': 1920, 'prompt_cache_miss_tokens': 48}, 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_8802369eaa_prod0623_fp8_kvcache', 'id': 'c8d407f4-d14c-4b5e-95ff-7f6485b48323', 'service_tier': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run--b64c2bc3-52b1-4a9b-934d-51f3944f5c18-0',
 #                 tool_calls=[{'name': 'tavily_search', 'args': {'query': '今天几号', 'search_depth': 'basic'}, 'id': 'call_0_cbed64bd-99d5-4b14-ade8-da2e9aef4f77', 'type': 'tool_call'}],
 #                 usage_metadata={'input_tokens': 1968, 'output_tokens': 28, 'total_tokens': 1996, 'input_token_details': {'cache_read': 1920}, 'output_token_details': {}})
 #       ]
 #  }

