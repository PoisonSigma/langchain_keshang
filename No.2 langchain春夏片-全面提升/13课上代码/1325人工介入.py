import warnings
# 过滤Tavily的属性覆盖警告TavilyResearch 类（TavilySearch 的底层实现类）中的 output_schema 和 stream 字段名称，与父类 BaseTool 的同名属性重复；
warnings.filterwarnings("ignore", message="Field name .* shadows an attribute in parent")

import sqlite3

from langgraph.graph import StateGraph

#workflow工作流
#StateGraph状态图
#中断,invoke 执行的时候,遇到interrupt 会中断,一旦中断,编译好的图就停止,直到遇到Comman(resume)才恢复到中断所在的结点的开头开始执行
#恢复
from typing import TypedDict
class State(TypedDict):
    content:str #内容
    approved:bool #是否批准

#  定义节点函数
def user_input_node(state:State)->State:
    user_input = input("请输入要输入的信息:\n")
    return  {"content":user_input}
# 添加人工介入函数
from langgraph.types import interrupt, Command
def human_review_node(state:State)->State:
    print("进入函数human_review_node state=",state)
    # interrupt是暂停,之后会通过执行 graph.invoke(Command)恢复
    result_interrupt = interrupt(f"请人工审核{state['content']}")#这个是中断工作流
    # 当恢复运行的时候再次进入这个节点,但是不会再次中断,而是把后面的Command(resume="返回的值")的结果返回给interrupt左边
    print("result_interrupt=",result_interrupt)
    print("interrupt执行完毕=============")
    if result_interrupt == "同意":
        approved = True
    else:
        approved = False
    return {"content":state["content"],"approved":approved}

def final_node (state:State)->State:
    if state["approved"]:
        print("✅ 审核通过了,内容是:",state["content"])
    else:
        print("❌ 审核未通过,内容是:", state["content"])
    return state


graph_builder = StateGraph(State)
graph_builder.add_node("user_input_node", user_input_node)
graph_builder.add_node("human_review_node", human_review_node)
graph_builder.add_node("final_node", final_node)

graph_builder.set_entry_point("user_input_node")#等价于添加边,从START到当前的字符串的key
graph_builder.add_edge("user_input_node","human_review_node")
graph_builder.add_edge("human_review_node","final_node")
from langgraph.checkpoint.sqlite import SqliteSaver  # 需要安装包langgraph-checkpoint-sqlite
from langgraph.graph import StateGraph

conn = sqlite3.connect("langgraph.db", check_same_thread=False)  # 创建链接,关闭检查相同线程,langgraph是多线程,默认sqlite是单线程
checkpointer = SqliteSaver(conn)  # 创建一个内存保存器
graph = graph_builder.compile(checkpointer)
config = {"configurable": {"thread_id": 1}}
result = graph.invoke({},config)

print("result['__interrupt__']=",result['__interrupt__'])
user_input = input("请输入同意还是不同意:\n")
#执行完下面后会再次进入中断之前所在的节点human_review_node,而不是在interrupt调用的后面执行
result = graph.invoke(Command(resume=user_input),config)
print("result=",result)
#可视化图
try:
    #display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = graph.get_graph().draw_mermaid_png()
    with open("人工介入.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：人工介入.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)