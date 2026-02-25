# 使用 @tool 装饰器简化了将自定义函数转换为 LangChain 工具的过程

from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek
from langchain_core.tools import tool
#@tool定义的方法的类型是StructuredTool
@tool
def add(a: int, b: int) -> int:
    """Adds a and b.""" #这个3双引号的文档字符串要有,否则报错:error_on_invalid_docstring
    return a + b
print(type(add))

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b

# value1 = {"add": add, "multiply": multiply}["add"]#这个是左边是字典,右边是字典的key,最终就是在这个字典里面选出value
# print(value1)
# print(type(value1))

tools = [add, multiply]
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
llm_with_tools = llm.bind_tools(tools)

query = "3 * 12 = 多少? 11 + 49 = 多少?"

messages = [HumanMessage(query)]#先把要发的人类提问放前面,

ai_msg = llm_with_tools.invoke(messages)#把绑定的工具调用人类的提问,获取到大模型返回的选择工具

print("ai_msg.tool_calls=",ai_msg.tool_calls) #这里大模型返回了需要调用的工具,是一个字典列表[dict]

messages.append(ai_msg)#把大模型返回的ai结果添加到提示词中,

for tool_call in ai_msg.tool_calls:
    # {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    #这句话作用:lower它的作用是将字符串转换为小写形式。
    selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    print("tool_call=",tool_call)
    print("type(tool_call)=", type(tool_call))
    print("selected_tool=",selected_tool)
    print("type(selected_tool)=",type(selected_tool))
    tool_msg = selected_tool.invoke(tool_call)#生成
    messages.append(tool_msg)
print("messages=",messages)
final_ai_msg = llm_with_tools.invoke(messages)
print("final_ai_msg=",final_ai_msg)

