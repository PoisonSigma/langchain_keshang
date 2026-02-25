# 推理模型的思维链和 多轮对话的机制原理:
from openai import OpenAI
#下面api_key改成自己的
client = OpenAI(api_key="sk-c7cedb71b580441089441795780ac272", base_url="https://api.deepseek.com")
# 为什么要有 tools 调用呢?
# 1.因为大模型处理自然语言比较强,但是数学运算,或者其他的比较弱,
# 2.open ai的设计,里面带着tools 的调用,
# 3.这样利于结构化输入输出
# # Round 1 if(a  - b)>0:
#    a 大
# else:
#     b 大
# messages = [
#     {"role": "system",
#      "content": "你是一个会说话但是,但是除了会说好听的,一个对象也较少不了的媒婆,不要说难听的,只说好听的"},
#     {"role": "user", "content": "我没对象"},  # 第一轮的提问
# ]
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
# client.chat.completions.create 这个是openai的方法,
response = client.chat.completions.create(
    model="deepseek-chat",  # 这里要改成推理模型
    messages=messages
)

print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print(response)
content = response.choices[0].message.content
print("content=", content)  # content是最终结果
reasoning_content = response.choices[0].message.reasoning_content
print("reasoning_content=", reasoning_content)  # reasoning_content是推理过程的内容
# 推理过程是个用户看的,最终结果content才是多轮对话,放在下一次的上下文中的

# 开始第二轮对话:在system 后面要先有 user 第一轮提问 ,再 assistant 回答历史,再 user提问
# messages.append({"role": "assistant", "content": content})
# messages.append({"role": "assistant", "content": "我没对象,如果我说我全家都没对象,阁下又该如何应对呢?"})
messages.append({'role': 'assistant', 'content': content})
messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
# messages = [
#     {"role": "system",
#      "content": "你是一个会说话但是,但是除了会说好听的,一个对象也介绍不了的媒婆,不要说难听的,只说好听的"},
#     {"role": "user", "content": "我没对象"},  # 第一轮的提问
#     {"role": "assistant", "content": content},  # 第一轮的回答
#     {"role": "user", "content": "我没对象,如果我说我全家都没对象,阁下又该如何应对呢?"},  # 第二轮的提问
# ]
response = client.chat.completions.create(
    model="deepseek-reasoner",  # 这里要改成推理模型
    messages=messages
)
print("messages=",messages)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
print("第二轮对话=====>")#为了试验硬盘缓存机制,需要再第二轮对话的时候,把第一轮的 sytem和user提问什么的都变成一样的
print(response)
content = response.choices[0].message.content
print("content=", content)  # content是最终结果
reasoning_content = response.choices[0].message.reasoning_content
print("reasoning_content=", reasoning_content)  # reasoning_content是推理过程的内容

# fewshow,多轮对话也会有重复的,算是命中缓存,硬盘缓存机制
# template1
# [
#     香蕉  水果
#     苹果  水果
# ]
