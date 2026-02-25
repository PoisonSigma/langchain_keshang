from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages.tool import tool_call, ToolMessage
from langchain_core.tools import tool
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
#让大模型调用工具的顺序
#[HumanMessage , 人类提出问题
 # AIMessage ,这个是第一轮使用bind_tools以后调用的人类提出问题,再返回的结果
 # ToolMessage,这是第一轮返回的AIMessage,里面的tool_calls的元素
 # ToolMessage,这是第一轮返回的AIMessage,里面的tool_calls的元素
 #]
 #把这个message的List用绑定了工具的llm调用
@tool
def add(a,b):
    """这是加法运算a+b"""
    result = a + b
    print(a,"+",b ,"=",result)
    return result
@tool
def multi(a, b):
    """这是乘法运算a*b"""
    result = a * b
    print(a,"*",b ,"=",result)
    return result
# msg1= add.invoke({"a":1,"b":2})
# print(msg1)
# print(type(msg1))
# msg2 = muti.invoke({"a":3,"b":4})
# print(msg2)
# print(type(msg2))

#把llm返回的tool_calls中的一个元素,直接传入到@tool里面.invoke,可以得到ToolMessage
#例如下面tool_call1是llm返回的,这里直接复制过来
# tool_call1 ={'name': 'muti', 'args': {'a': 3, 'b': 4}, 'id': 'call_1_de6fb1fc-4512-4365-bf34-f50094c8848b', 'type': 'tool_call'}
# toolMsg1 = muti.invoke(tool_call1)
# print("toolMsg1=",toolMsg1)
# print("type(toolMsg1)",type(toolMsg1))

#
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(model=os.getenv("MODEL_NAME"), temperature=0.8)
tools = [add, multi]
llm_with_toolls = llm.bind_tools(tools)
msg = [HumanMessage("1+2=? 3*4=?")]
ai_msg = llm_with_toolls.invoke(msg)



print("ai_msg=",ai_msg)
tool_calls = ai_msg.tool_calls
print("tool_calls=",tool_calls)
msg.append(ai_msg)
print("msg=",msg)
for tool in tool_calls:
    fun = {"add":add,"multi":multi}[tool["name"].lower()]
    print("tool=",tool)
    tool_msg = fun.invoke(tool)#@tool 类型的对象.invoke(里面传入大模型返回的tool_calls的元素),会生成tool_msg
    print("tool_msg=",tool_msg)
    print(" type(tool_msg)=", type(tool_msg))
    msg.append(tool_msg)
    print("msg=",msg)

#上面组合完最终的Message List :
# [
#     HumanMessage,
#     AIMessage,
#     ToolMessage,
# ToolMessage
# ]
print("msg=",msg)

ai_msg = llm_with_toolls.invoke(msg)
print("ai_msg=",ai_msg)

[HumanMessage(content='1+2=? 3*4=?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_0_cc48cab8-ba79-444d-ba00-bf86802283c2', 'function': {'arguments': '{"a": 1, "b": 2}', 'name': 'add'}, 'type': 'function', 'index': 0}, {'id': 'call_1_98635989-cdef-46fb-997a-452b6120864c', 'function': {'arguments': '{"a": 3, "b": 4}', 'name': 'multi'}, 'type': 'function', 'index': 1}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 47, 'prompt_tokens': 181, 'total_tokens': 228, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 128}, 'prompt_cache_hit_tokens': 128, 'prompt_cache_miss_tokens': 53}, 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_3d5141a69a_prod0225', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-85a08fbd-5832-43c1-a9d3-e8fe8ced6088-0',
           tool_calls=[{'name': 'add', 'args': {'a': 1, 'b': 2}, 'id': 'call_0_cc48cab8-ba79-444d-ba00-bf86802283c2', 'type': 'tool_call'},
                       {'name': 'multi', 'args': {'a': 3, 'b': 4}, 'id': 'call_1_98635989-cdef-46fb-997a-452b6120864c', 'type': 'tool_call'}], usage_metadata={'input_tokens': 181, 'output_tokens': 47, 'total_tokens': 228, 'input_token_details': {'cache_read': 128}, 'output_token_details': {}}),
 ToolMessage(content='3', name='add', tool_call_id='call_0_cc48cab8-ba79-444d-ba00-bf86802283c2'),
 ToolMessage(content='7', name='multi', tool_call_id='call_1_98635989-cdef-46fb-997a-452b6120864c')]

