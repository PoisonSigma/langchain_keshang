from pprint import pprint

from langchain.agents import create_agent
import os

from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
from nltk import toolbox
checkpointer = InMemorySaver() #BaseCheckpointSaver的子类
load_dotenv("../openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
from langchain.tools import tool
@tool
def dongbei_convbert(text: str):
    """把传入字符串转化成东北话"""
    print("工具被调用")
    result =text.replace("没", "妹").replace("我", "俺").replace("什么", "啥")
    print("东北口音结果是:",result)
    if result == text:
        print("没有转换,自己加上一个前缀:")
        result += "干哈呢?"
    return result#注意这个返回结果是给 大模型用的

@tool
def london_accent_converter(text: str):
    """说话的时候变成伦敦口音"""
    result = "此时传来一口地道的伦敦味:may I help you sir然后再说:" + text
    print("工具被调用")
    print(f"result={result}")
    print("伦敦口音结果是:", result)
    return result#注意这个返回结果是给 大模型用的



tools = [
dongbei_convbert,
london_accent_converter
]
angent = create_agent(llm, tools, system_prompt="你一个帮助转换口音的助手",checkpointer=checkpointer)
# config: RunnableConfig
#config 类型是TypedDict子类型,代表字典的key是有明确名字的,逗号total=false是给父类的参数附上默认值
ai_msg = angent.invoke({"messages": [HumanMessage(content="请把这句话变成东北口音:hello world")]},
                       {"configurable": {"thread_id": "1"}},
                       )

print("type(ai_msg)=",type(ai_msg))
for msg in ai_msg.get("messages"): #get比普通的[""]增加了默认值,如果没找到对应key不会报错
    pprint(msg)

ai_msg = angent.invoke({"messages": [HumanMessage(content="我之前问的内容是什么?")]},
{"configurable": {"thread_id": "1"}},
)
for msg in ai_msg.get("messages"): #get比普通的[""]增加了默认值,如果没找到对应key不会报错
    pprint(msg)