from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
# Graph state
class State(TypedDict):
    topic: str #主题
    story: str #故事
    seconed_story_str: str # 第二个剧本当中包含了视觉嗅觉等,可能产生不雅之物,要进行去屎尿化
    third_story_str: str

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)

def first_story(state: State):
    """大模型调用生成第一轮幽默的文案"""
    msg = llm.invoke(f"写一段幽默的文案大概50字关于话题 {state['topic']}的")
    return {"story": msg.content}



def second_story(state: State):
    """第二次LLM调用来改进笑话"""

    msg = llm.invoke(f"让文字能够让人的感官例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道,要突出肩膀上硕大的针眼,和后背的痤疮,嘴里的口臭难闻,夸大文字效果: {state['story']}")
    return {"seconed_story_str": msg.content}

def no_shit_condition(state: State):#当第二个story运行完毕的时候进入这个函数判断
    """如果文字里面包含屎尿,就要去掉"""
    if "屎" in state["seconed_story_str"] or "尿" in state["seconed_story_str"]:
        return "have_shit"
    return "no_shit"
def no_shit_story(state: State):#当第二个story运行完毕的时候进入这个函数判断
    """如果文字里面包含屎尿,就要去掉"""
    msg = llm.invoke(f"去掉文字中的屎尿屁文字: {state['seconed_story_str']}")
    print("去掉屎尿以后:",msg.content)
    return {"seconed_story_str": msg.content}
def third_story(state: State):
    """第三，LLM要求最后的润色"""

    msg = llm.invoke(f"让文字押韵有文采,在每行文字最后一个字上的韵母尽量相同,124句相同,第三局可以是别的韵母: {state['seconed_story_str']}")
    return {"third_story_str": msg.content}


# Build workflow
stateGraph = StateGraph(State)

# Add nodes
stateGraph.add_node("first_story", first_story)
stateGraph.add_node("second_story", second_story)
stateGraph.add_node("no_shit_story", no_shit_story)
stateGraph.add_node("third_story", third_story)

# Add edges to connect nodes
stateGraph.add_edge(START, "first_story")
stateGraph.add_edge("first_story", "second_story")
stateGraph.add_edge("second_story", "third_story")
stateGraph.add_conditional_edges(
    #判断,包含屎尿,就进入no_shit函数重新请求大模型,如果不包含就执行第三个story的节点
    "second_story",no_shit_condition, {"have_shit": "no_shit_story", "no_shit": "third_story"}
)
stateGraph.add_edge("no_shit_story", "third_story")
stateGraph.add_edge("third_story", END)

# Compile
graph = stateGraph.compile()

# Show workflow
try:
    png_data = graph.get_graph().draw_mermaid_png()
    with open("喜表酷尔曼.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：喜表酷尔曼.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)

# Invoke
ai_msg = graph.invoke({"topic": "拉屎"})
print("第一轮文案:")
print(ai_msg["story"])
print("\n--- --- ---\n")
if "seconed_story_str" in ai_msg:
    print("第二轮文案:")
    print(ai_msg["seconed_story_str"])
    print("\n--- --- ---\n")

    print("第三轮文案:")
    print(ai_msg["third_story_str"])
else:
    print("story failed quality gate - no punchline detected!")