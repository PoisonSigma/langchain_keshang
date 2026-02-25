from typing import TypedDict
import uuid
from langgraph.graph import StateGraph
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import START, END


# 1. 定义图状态结构
class State(TypedDict):
    content: str #内容
    approved: bool #是否批准


# 2. 定义节点函数
def user_input_node(state: State) -> State:
    """生成初始内容"""
    user_input = input("请输入内容:\n")
    #请联系有8块腹肌长相帅气的健身教练,就说吴彦祖要联系他
    return {"content": user_input}


def human_review_node(state: State) -> State:
    """人类审查节点（包含中断）"""
    # 暂停图执行，等待人类输入
    content = state["content"]
    #interrupt是暂停,之后会通过执行 graph.invoke(Command)恢复
    print("interrupt 开始")
    interrupt_result = interrupt(f"请人类审核如下内容:{content}")#执行这句就会暂停,然后我们后续通过input输入
    #当恢复运行的时候再次进入这个节点,但是不会再次中断,而是把后面的Comand(resume)的结果返回给interrupt左边
    print("interrupt_result=",interrupt_result)
    print("interrupt 结束")
    # 根据人类输入更新状态
    if interrupt_result == "同意":
        return {"content":content, "approved":True}
    else:
        return {"content": content, "approved": False}





def final_processing(state: State) -> State:
    print("final_processing state=",state)
    """最终处理节点"""
    if state["approved"]:
        print(f"✅ 内容已通过审核: {state['content']}")
    else:
        print(f"❌ 内容未通过审核")
    return state


# 3. 构建图
builder = StateGraph(State)

# 添加节点
builder.add_node("user_input_node", user_input_node)
builder.add_node("human_review", human_review_node)
builder.add_node("finalize", final_processing)

# 定义流程
builder.set_entry_point("user_input_node")#入口节点,相当于从start到这里的边
builder.add_edge("user_input_node", "human_review")
builder.add_edge("human_review", "finalize")
builder.add_edge("finalize", END)

# 4. 配置检查点（必须用于保存状态）
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# 5. 运行图直到中断
thread_id = "1"
config = {"configurable": {"thread_id": thread_id}}

# 首次调用：执行到中断点
initial_result = graph.invoke({}, config=config) #第一个节点不输入任何内容,但是在节点里面输入
print("initial_result=",initial_result)
print("中断信息:", initial_result["__interrupt__"])  # 显示中断提示

# 6. 人类输入并恢复执行（模拟人类编辑操作）
human_response = input("请输入同意或者不同意:\n")
# human_response = "同意"
# human_response = {
#     "action": "edit",
#     "edited_content": "经过人类编辑后的最终内容"
# }
#执行完下面后会再次进入中断之前所在的节点human_review_node,而不是在interrupt调用的后面执行
final_result = graph.invoke(Command(resume=human_response), config=config)

# 输出最终结果
print("最终状态:", final_result)
try:
    #display(Image(graph.get_graph().draw_mermaid_png()))
    # 生成图片二进制数据
    png_data = graph.get_graph().draw_mermaid_png()
    with open("人工审核.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：人工审核.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)