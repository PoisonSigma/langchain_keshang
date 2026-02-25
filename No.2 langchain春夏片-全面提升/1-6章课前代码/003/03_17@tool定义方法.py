from langchain_core.tools import tool

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
@tool
def add(a: int, b: int) -> int:
    """加法a+b"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """乘法a*b"""
    return a * b


tools = [add, multiply]

llm_bind_tools = llm.bind_tools(tools)
res = llm_bind_tools.invoke("3*2=?")
print(res)
res_tools = res.tool_calls
print("res_tools=",res_tools)