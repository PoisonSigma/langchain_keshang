# 在 LangChain 里，ToolMessage 一般用来表示工具调用后返回的消息。
# 定义 ToolMessage 所需参数
# content：此为工具调用返回的具体内容，一般是工具执行后的结果。
# name：指的是工具的名称，要和工具定义时的名称保持一致。
# tool_call_id：是工具调用的唯一标识符，要和大模型返回的 tool_call 里的 id 相匹配。

from langchain_core.tools import tool
from langchain_core.messages.tool import ToolMessage

# 自定义 ToolMessage
tool_message = ToolMessage(
    content="这是工具执行的结果",
    name="my_custom_tool",
    tool_call_id="call_1_abcdef"
)
#@tool方法定义的对象, .invoke(传入 大模型返回的tool_calls中的一个元素) ,可以生成ToolMessage
@tool
def add(a,b):
    """加法 a+b"""
    print("调用add")
    result = a + b
    return result
#大模型返回的tool_calls是个字典,包括,name args id type
# tool_call1 ={'name': 'muti', 'args': {'a': 3, 'b': 4}, 'id': 'call_1_de6fb1fc-4512-4365-bf34-f50094c8848b', 'type': 'tool_call'}
#注意 ,下面的args,参数key要对上
tool_call1 ={'name': '测试函数名', 'args': {'a': 3, 'b': 4}, 'id': '1', 'type': 'tool_call'}

tool_msg1 = add.invoke(tool_call1)
print("tool_msg1=",tool_msg1)
print("type(tool_msg1)=",type(tool_msg1))


