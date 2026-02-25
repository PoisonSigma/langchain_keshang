from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
# Graph state
class State(TypedDict):
    topic: str #主题
    story: str #故事
    seconed_story_str: str # 第二个剧本当中包含了视觉嗅觉等,可能产生不雅之物,要进行去屎尿化
    third_story_str: str#第三轮文案

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)

def first_story(state: State):
    """大模型调用生成第一轮幽默的文案"""
    prompt = ChatPromptTemplate.from_template("写一段幽默的文案大概50字关于话题{topic}")
    # msg = llm.invoke(f"写一段幽默的文案大概50字关于话题 {state['topic']}的")
    chain = prompt | llm | StrOutputParser()
    # chain = prompt | llm
    ai_msg = chain.invoke({"topic":state['topic']})
    print("first_story ai_msg = ",ai_msg)
    return {"story":ai_msg}
    # return {"story": msg.content}

def second_story(state: State):
    """第二次LLM调用来改进笑话"""
    if state["topic"] == "增肌":
        # msg = llm.invoke(f"让文字能够让人的感官得到冲击,例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道,要突出肩膀上硕大的针眼,和后背的痤疮,嘴里的口臭难闻,夸大文字效果: {state['story']}")
        prompt = ChatPromptTemplate.from_template("让文字能够让人的感官得到冲击,例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道,要突出肩膀上硕大的针眼,和后背的痤疮,嘴里的口臭难闻,夸大文字效果: {story}")

    else:
        prompt = ChatPromptTemplate.from_template(
            "让文字能够让人的感官得到冲击,例如,听觉,视觉,味觉,嗅觉,触觉等,例如人闻到气味,或者尝到味道: {story}")
    chain = prompt | llm | StrOutputParser()
    ai_msg = chain.invoke({"story":state['story']})
    print("second_story ai_msg = ",ai_msg)
    return {"seconed_story_str": ai_msg}

def no_shit_condition(state: State):#当第二个story运行完毕的时候进入这个函数判断
    """如果文字里面包含屎尿,就要去掉"""
    if "屎" in state["seconed_story_str"] or "尿" in state["seconed_story_str"]:
        return "have_shit"
    return "no_shit"
def no_shit_story(state: State):#当第二个story运行完毕的时候进入这个函数判断
    """如果文字里面包含屎尿,就要去掉"""
    prompt = ChatPromptTemplate.from_template(
        "去掉文字中的屎尿屁文字: {seconed_story_str}")
    chain = prompt | llm | StrOutputParser()
    ai_msg = chain.invoke({"seconed_story_str": state['seconed_story_str']})
    print("去掉屎尿以后:",ai_msg)
    return {"seconed_story_str": ai_msg}

def third_story(state: State):
    """第三，LLM要求最后的润色,增加文采,文字押韵"""

    msg = llm.invoke(f"让文字押韵有文采,在每行文字最后一个字上的韵母尽量相同,124句相同,第三局可以是别的韵母: {state['seconed_story_str']}")
    return {"third_story_str": msg.content}
# Build workflow
stateGraph = StateGraph(State)
stateGraph.add_node("first_story", first_story)
stateGraph.add_node("second_story", second_story)
stateGraph.add_node("no_shit_story", no_shit_story)
stateGraph.add_node("third_story", third_story)
stateGraph.add_edge(START, "first_story")
stateGraph.add_edge("first_story", "second_story")

stateGraph.add_conditional_edges(
    #判断,包含屎尿,就进入no_shit函数重新请求大模型,如果不包含就执行第三个story的节点
    "second_story",no_shit_condition, {"have_shit": "no_shit_story", "no_shit": "third_story"}
)
stateGraph.add_edge("no_shit_story", "third_story")
stateGraph.add_edge("third_story", END)
graph = stateGraph.compile()
ai_msg = graph.invoke({"topic":"增肌"})
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
try:
    png_data = graph.get_graph().draw_mermaid_png()
    with open("1341.png", "wb") as f:
        f.write(png_data)
        print("工作流图已保存为：1341.png")  # 提示保存路径
except Exception as e:
    # This requires some extra dependencies and is optional
    print("e=",e)
# state = graph.invoke({"topic": "增肌"})

#舔狗圈传来噩耗,吃不了西格玛的苦,就要吃被嘲笑的苦
# 一只被众人嘲笑的舔狗
# 看着自己肩膀上的密布的针孔头
# 曾经被欲望榨干自己的尊严和钱包
# 在未来尝够苦头猛然觉醒永不低头
