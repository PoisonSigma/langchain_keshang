from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage
from langchain_core.prompts import MessagesPlaceholder

# HumanMessage(content="我叫绯村剑心")
# AIMessage(content="啊,那你很帅气啊(你真能吹啊,我信你个鬼)")
# SystemMessage(content="你是一个运动专家")
prompt = MessagesPlaceholder(
    # variable_name="chat_history",
    variable_name="GasSpeedUpSystem",
    optional=True  # 默认是False,是不能可空的,就是必须得填写,如果是True才是可空的
)
print("prompt=", prompt)  # 蛋清屁

result = prompt.format_messages(GasSpeedUpSystem=[
    HumanMessage(content="多吃鸡蛋,但是不咀嚼"),
    AIMessage(content="你很厉害啊"),
    HumanMessage(content="但是我想减速怎么办?")
])
print(result)
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    model=os.getenv("MODEL_NAME"),
     temperature=0.8)
ai_msg = llm.invoke(result)
print("ai_msg",ai_msg)