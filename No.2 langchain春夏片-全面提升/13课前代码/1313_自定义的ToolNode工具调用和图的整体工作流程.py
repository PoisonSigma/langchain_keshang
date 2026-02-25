#安装包:langchain-tavily
#本课中自定义函数代替ToolNode
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
class BasicToolNode:
    """A node that runs the tools requested in the last AIMessage."""

    def __init__(self, tools: list) -> None:
        self.tools_by_name = {tool.name: tool for tool in tools}#这里是for循环遍历tools然后放到字典里面
        #等价于这个self.tools_by_name = {}  # 初始化空字典
        # for tool in tools:
        #     self.tools_by_name[tool.name] = tool  # 键是工具名称，值是工具对象
        #如果有2个tool,一个名字叫:langSearch,一个叫:TavilySearch ,那么这里结果就是:
        #假设工具里面存的2个对象如下:
        # [langSearch_tool,tavilySearch_tool]
        #这2个对象里面的名字.name属性分别是langSearch和TavilySearch
        #{"langSearch":langSearch_tool,"tavily_search":tavilySearch_tool}


    #这段代码的核心逻辑是处理大模型生成的最后一条信息,遍历里面的工具,再让里面的参数args传给要调用的工具,通过工具名字的字典遍历
    def __call__(self, inputs: dict):#__call__作用是对象可以直接传入参数当函数用
        #例如对象是obj,那么可以obj({字典})当函数调用
        print("BasicToolNode __call__: inputs=",inputs)
        #messages 列表存在且不为空，取最后一条消息（
        if messages := inputs.get("messages", []):
            message = messages[-1]#-1是list里面的最后一个元素,每次
        else:
            raise ValueError("No message found in input")
        #处理工具调用请求通过工具名称快速查找对应的工具对象
        outputs = []#保存输出
        #处理所有工具调用，我们例子里面只有一个工具,所以就调用一个工具
        for tool_call in message.tool_calls:
            #获取工具：self.tools_by_name是一个字典，通过工具名称（如"tavily_search"）查找对应的工具实例。
            #这里右边相当于是遍历[tools里面的对象,tools_by_name字典的key是名字从messages传入,value是工具的对象]
            tool_result = self.tools_by_name[tool_call["name"]].invoke(
                tool_call["args"]#传入的参数,传给工具
            )
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),#序列化为 JSON 字符串
                    name=tool_call["name"],#tool_call是for 遍历的子工具
                    tool_call_id=tool_call["id"],
                )
            )
        return {"messages": outputs}
# tool_node = BasicToolNode(tools=[tool])
# graph_builder.add_node("tools",tool_node)#,参数tools=[tool]表示该节点关联的工具列表,ToolNode是 LangGraph 中用于处理工具调用的节点类,这个可以自己写,但是代码太多用框架写好的就行
# #add_conditional_edges增加条件判断的边
# #创建带条件判断的边,参数1,是起始点,参数二框架自带的条件,
# # 如果llm不需要调用工具就走到end,如果需要调用工具就走到工具节点
#
# #tools_condition框架创建的工具判断条件
# graph_builder.add_conditional_edges("chat_node",tools_condition)
#
# graph_builder.add_edge("tools","chat_node")
# graph = graph_builder.compile()
# #可视化图
# try:
#     #display(Image(graph.get_graph().draw_mermaid_png()))
#     # 生成图片二进制数据
#     png_data = graph.get_graph().draw_mermaid_png()
#     with open("openai_graph.png", "wb") as f:
#         f.write(png_data)
#         print("工作流图已保存为：langgraph_workflow.png")  # 提示保存路径
# except Exception as e:
#     # This requires some extra dependencies and is optional
#     print("e=",e)
# graph_result = graph.invoke({"messages":["今天几号?请查一下工具再回答吧,求你了"]})
# print("result=",graph_result)#这个是整个工作流结束的汇总信息
# messages = graph_result["messages"]
# for message in messages:
#     print(type(message),"content=",message.content)
#  # {'messages':
#  #      [
#  #          HumanMessage(content='今天几号?请查一下工具再回答吧,求你了', additional_kwargs={}, response_metadata={}, id='59765d7f-b709-4ac0-b377-3e35271a2492'),
#  #          AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_0_c2f0e112-e3e2-4af3-8e78-3d231e6daa14', 'function': {'arguments': '{"query":"今天日期"}', 'name': 'tavily_search'}, 'type': 'function', 'index': 0}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 1956, 'total_tokens': 1977, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 1920}, 'prompt_cache_hit_tokens': 1920, 'prompt_cache_miss_tokens': 36}, 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_8802369eaa_prod0623_fp8_kvcache', 'id': 'ae047a14-54a7-4c15-87f1-6f129a113f61', 'service_tier': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run--67f5741d-a2a5-4349-b829-93a328f2fb83-0',
#  #                    tool_calls=[{'name': 'tavily_search', 'args': {'query': '今天日期'}, 'id': 'call_0_c2f0e112-e3e2-4af3-8e78-3d231e6daa14', 'type': 'tool_call'}], usage_metadata={'input_tokens': 1956, 'output_tokens': 21, 'total_tokens': 1977, 'input_token_details': {'cache_read': 1920}, 'output_token_details': {}}),
#  #          ToolMessage(content='{"query": "\\u4eca\\u5929\\u65e5\\u671f", "follow_up_questions": null, "answer": null, "images": [], "results": [{"url": "http://zh.todaysdate365.com/", "title": "\\u65e5\\u671f\\u4eca\\u5929Today\'sDate365", "content": "\\u4eca\\u5929\\u7684\\u65e5\\u671f \\u00b7 \\u661f\\u671f\\u56db \\u00b7 2025 \\u4e03\\u670817 \\u00b7 2025/07/17. Today\'sDate365\\uff0c\\u6f14\\u793a. Today\'sDate365\\uff0c\\u6f14\\u793a. \\u4eca\\u5929\\u662f\\u51e0\\u53f7\\uff1f \\u5f88\\u591a\\u4eba", "score": 0.7420672, "raw_content": null}, {"url": "https://www.jyshare.com/front-end/5672/", "title": "\\u4eca\\u65e5\\u65e5\\u671f - \\u83dc\\u9e1f\\u5de5\\u5177", "content": "\\u4eca\\u65e5\\u65e5\\u671f | \\u83dc\\u9e1f\\u5de5\\u5177 Image 1: \\u83dc\\u9e1f\\u5de5\\u5177 \\u4eca\\u65e5\\u65e5\\u671f \\uff5c 2025 \\u5e74 07 \\u6708 08 \\u65e5 03:44:04  8 \\u5341\\u56db Image 2Calendar Remark \\u5173\\u95ed \\u4fdd\\u5b58\\u56fe\\u7247 2025\\u5e74 1900\\u5e74 1901\\u5e74 1902\\u5e74 1903\\u5e74 1904\\u5e74 1905\\u5e74 1906\\u5e74 1907\\u5e74 1908\\u5e74 1909\\u5e74 1910\\u5e74 1911\\u5e74 1912\\u5e74 1913\\u5e74 1914\\u5e74 1915\\u5e74 1916\\u5e74 1917\\u5e74 1918\\u5e74 1919\\u5e74 1920\\u5e74 1921\\u5e74 1922\\u5e74 1923\\u5e74 1924\\u5e74 1925\\u5e74 1926\\u5e74 1927\\u5e74 1928\\u5e74 1929\\u5e74 1930\\u5e74 1931\\u5e74 1932\\u5e74 1933\\u5e74 1934\\u5e74 1935\\u5e74 1936\\u5e74 1937\\u5e74 1938\\u5e74 1939\\u5e74 1940\\u5e74 1941\\u5e74 1942\\u5e74 1943\\u5e74 1944\\u5e74 1945\\u5e74 1946\\u5e74 1947\\u5e74 1948\\u5e74 1949\\u5e74 1950\\u5e74 1951\\u5e74 1952\\u5e74 1953\\u5e74 1954\\u5e74 1955\\u5e74 1956\\u5e74 1957\\u5e74 1958\\u5e74 1959\\u5e74 1960\\u5e74 1961\\u5e74 1962\\u5e74 1963\\u5e74 1964\\u5e74 1965\\u5e74 1966\\u5e74 1967\\u5e74 1968\\u5e74 1969\\u5e74 1970\\u5e74 1971\\u5e74 1972\\u5e74 1973\\u5e74 1974\\u5e74 1975\\u5e74 1976\\u5e74 1977\\u5e74 1978\\u5e74 1979\\u5e74 1980\\u5e74 1981\\u5e74 1982\\u5e74 1983\\u5e74 1984\\u5e74 1985\\u5e74 1986\\u5e74 1987\\u5e74 1988\\u5e74 1989\\u5e74 1990\\u5e74 1991\\u5e74 1992\\u5e74 1993\\u5e74 1994\\u5e74 1995\\u5e74 1996\\u5e74 1997\\u5e74 1998\\u5e74 1999\\u5e74 2000\\u5e74 2001\\u5e74 2002\\u5e74 2003\\u5e74 2004\\u5e74 2005\\u5e74 2006\\u5e74 2007\\u5e74 2008\\u5e74 2009\\u5e74 2010\\u5e74 2011\\u5e74 2012\\u5e74 2013\\u5e74 2014\\u5e74 2015\\u5e74 2016\\u5e74 2017\\u5e74 2018\\u5e74 2019\\u5e74 2020\\u5e74 2021\\u5e74 2022\\u5e74 2023\\u5e74 2024\\u5e74 2025\\u5e74 2026\\u5e74 2027\\u5e74 2028\\u5e74 2029\\u5e74 2030\\u5e74 2031\\u5e74 2032\\u5e74 2033\\u5e74 2034\\u5e74 2035\\u5e74 2036\\u5e74 2037\\u5e74 2038\\u5e74 2039\\u5e74 2040\\u5e74 2041\\u5e74 2042\\u5e74 2043\\u5e74 2044\\u5e74 2045\\u5e74 2046\\u5e74 2047\\u5e74 2048\\u5e74 2049\\u5e74 2050\\u5e74 7\\u6708 1\\u6708 2\\u6708 3\\u6708 4\\u6708 5\\u6708 6\\u6708 7\\u6708 8\\u6708 9\\u6708 10\\u6708 11\\u6708 12\\u6708 8 \\u5341\\u56db \\u4eca Image 3 \\u5173\\u95ed", "score": 0.6420965, "raw_content": null}], "response_time": 1.45}', name='tavily_search', id='4482e082-2bbd-4a82-b0a5-84dd75def56e', tool_call_id='call_0_c2f0e112-e3e2-4af3-8e78-3d231e6daa14'),
#  #          AIMessage(content='今天是2025年7月17日，星期四。', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 3587, 'total_tokens': 3598, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 1920}, 'prompt_cache_hit_tokens': 1920, 'prompt_cache_miss_tokens': 1667}, 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_8802369eaa_prod0623_fp8_kvcache', 'id': '60d8f9d3-e121-4e5c-9b0f-7550d6871c5a', 'service_tier': None, 'finish_reason': 'stop', 'logprobs': None}, id='run--bc46441d-fa49-4960-85cb-36349253f3d5-0', usage_metadata={'input_tokens': 3587, 'output_tokens': 11, 'total_tokens': 3598, 'input_token_details': {'cache_read': 1920}, 'output_token_details': {}})]}
#