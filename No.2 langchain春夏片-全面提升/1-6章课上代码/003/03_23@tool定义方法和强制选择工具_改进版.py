#也可以继承 TypedDict 类,但是我们掌握一个BaseModel就好了,后面再用@tool
#@tool直接修饰一个方法,节省我们的大脑健康细胞
from langchain_core.tools import tool
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
@tool
def add(a,b): #后面要调用的时候,要.invoke(字典)调用
    """加法a+b"""#错误,必须有文档描述字符串,报错:error_on_invalid_docstring
    result = a + b
    print("调用了add_function(),结果是", result)
    return result

@tool
def whichBigger(a,b):
    """哪个大"""
    print("调用了whichBigger_function()")
    if (a > b):
        print(a, "大")
    else:
        print(b, "大")
# add.invoke({"a":3,"b":4})#这个是调用@tool的方法,.invoke(字典)
load_dotenv("../assets/openai.env")
print(add)
print(type(add))
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
tools = [add,whichBigger]
print(type(tools))
llm_with_tools = llm.bind_tools(tools )#默认自动选
# llm_bind_tools = llm.bind_tools(tools,tool_choice="auto")#auto是自动选择
# llm_with_tools = llm.bind_tools(tools ,tool_choice="add")#让大模型强制选择一个工具,#auto是自动选择
ai_msg = llm_with_tools.invoke("1-2=? 9.8和9.12哪个大?")
print("ai_msg",ai_msg)
print("ai_msg.tool_calls",ai_msg.tool_calls)#拿到llm帮我们选择的tool
for tool_call in ai_msg.tool_calls:
    fun = {"add": add,"whichBigger":whichBigger}[tool_call["name"]]
    fun.invoke(tool_call)  # .invoke(tool_calls里的遍历元素)是调用方法,并且生成ToolMessage