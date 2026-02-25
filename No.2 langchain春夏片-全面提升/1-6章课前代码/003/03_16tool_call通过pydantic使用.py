#官网文档:https://python.langchain.com/docs/how_to/tool_calling/#langchain-tool

#定义一个 BaseModel的子类,作用是定义一个可以被大模型识别的语言描述
#也可以继承 TypedDict 类,但是我们掌握一个BAseModel就好了,后面再用@tool
from pydantic import BaseModel, Field
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
#加法工具
class add(BaseModel):
    """Add two integers."""

    a: int = Field(..., description="第1个数字")
    b: int = Field(..., description="第2个数字")
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
class whichBigger(BaseModel):
    """那个数字大"""
    a:int = Field()
    b: int = Field()
tools = [add,whichBigger]

def add_fun(a,b):
    result = a+b
    print("调用add_fun",a,"+",b ,"=",result)
    return result
def whichBigger_fun(a,b):
    print("调用whichBigger_fun")
    if a>b:
        print(a,"大")
    else:
        print(b,"大")

tools = [add,whichBigger]#定义了一个工具列表，这里只包含了之前定义的 add 工具。
llm_bind_tools = llm.bind_tools(tools)#将工具列表绑定到 llm 实例上，得到一个新的实例
# llm_bind_tools = llm.bind_tools(tools,tool_choice="auto")#auto是自动选择
# llm_bind_tools = llm.bind_tools(tools,tool_choice="add")#强制使用add,这样大模型发现虽然是乘法,但是还是调用假发
# "auto"自动选择一个工具（包括不选择工具）。
# "none"``：不调用任何工具。

msg= "9.1和9.08哪个大？"
res = llm_bind_tools.invoke(msg)
print("res = ",res)
res_tools =  res.tool_calls
print("res_tools=",res_tools)
for tool in res_tools:
    if tool["name"] == "add":
        add_fun(args["a"],args["b"])
    if tool["name"] == "whichBigger":
        args = tool["args"]
        whichBigger_fun(args["a"],args["b"])


# print("res.content=",res.content)