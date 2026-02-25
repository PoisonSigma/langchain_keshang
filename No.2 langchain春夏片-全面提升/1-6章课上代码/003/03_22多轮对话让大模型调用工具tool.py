#让大模型调用工具的顺序
#[HumanMessage , 人类提出问题
 # AIMessage ,这个是第一轮使用bind_tools以后调用的人类提出问题,再返回的结果
 # ToolMessage,这是第一轮返回的AIMessage,里面的tool_calls的元素
 # ToolMessage,这是第一轮返回的AIMessage,里面的tool_calls的元素
 #]
 #把这个message的List用绑定了工具的llm调用
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages.tool import tool_call, ToolMessage
from langchain_core.tools import tool
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

@tool
def add(a,b): #后面要调用的时候,要.invoke(字典)调用
    """加法a+b"""#错误,必须有文档描述字符串,报错:error_on_invalid_docstring
    result = a + b
    print("调用了add(),结果是", result)
    return result
@tool
def sub(a,b): #后面要调用的时候,要.invoke(字典)调用
    """减法a-b"""#错误,必须有文档描述字符串,报错:error_on_invalid_docstring
    result = a - b
    print("调用了sub(),结果是", result)
    return result

# add(1,2)#去掉@tool本地调试2个方法
# sub(3,4)

load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
llm_with_tools = llm.bind_tools([add, sub])
msgs = [HumanMessage("1+2=? 3-5=?")]
ai_msg = llm_with_tools.invoke(msgs)
print("第一轮ai_msg=",ai_msg)
msgs.append(ai_msg)
tool_calls = ai_msg.tool_calls
for tool_call in tool_calls:
    fun = {"add": add, "sub": sub}[tool_call["name"]]
    print("fun=",fun)
    tool_msg = fun.invoke(tool_call)#调用@tool方法,并且生成ToolMessage
    msgs.append(tool_msg)
print("msgs=",msgs)
#打印结果:[HumanMessage,
# AIMessage,
 # ,ToolMessage
 # ,ToolMessage]
ai_msg = llm_with_tools.invoke(msgs)
print("ai_msg=",ai_msg)