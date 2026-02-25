from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, trim_messages
from langchain_core.output_parsers import StrOutputParser


# 简单的 token 计数函数，这里简单按空格分割来近似 token 数量
def simple_token_counter(messages):
    total_tokens = 0
    for msg in messages:
        print("msg.content=", msg.content)
        print(len(msg.content))
        total_tokens += len(msg.content)
    return total_tokens


result = "我是一个钛合金钢铁直男,48k纯爷们,碳纤维的,但是我是软饭男".split()

msg = [
    SystemMessage("你是一个漂亮年轻的李阿姨,实际年龄比我小"),
    HumanMessage("我是一个钛合金钢铁直男,48k纯爷们,碳纤维的,但是我是软饭男"),
    AIMessage("我给你我的附属金卡"),
    HumanMessage("你在教我做事啊?"),
]
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

trimmed_messages = trim_messages(
    msg,
    max_tokens=2,  # 这个数字,不会让信息从中间断开
    strategy="last",#last从后截取
    # strategy="first",  # first从前截取
    # token_counter=simple_token_counter,  # 设置自己的计算token个数的函数
    token_counter=len, #只用len的话就是按对话条数来算
    # include_system=True, #要求包含system,强制包含,其他剩余的取个数,例如max_tokens数字很小,那么就只有系统信息
    # start_on="human",  # 第一条信息从human开始不包括系统,并且只显示人类对话
    # allow_partial=True,
)

print("trimmed_messages=", trimmed_messages)

# trimer = trim_messages(
#     max_tokens=2,  # 这个数字,不会让信息从中间断开
#     strategy="last",  # first从前截取
#     # token_counter=simple_token_counter,  # 设置自己的计算token个数的函数
#     token_counter=len,  #直接把系统函数取长度len设置成计算tokens的方法
# )
# result = trimer.invoke(msg) #可以直接通过invoke调用,代表直接可以在链里使用invoke
# print("result=",result)
# import os
# from langchain_deepseek import ChatDeepSeek
# from dotenv import load_dotenv
# load_dotenv("../assets/openai.env")
# llm = ChatDeepSeek(
#     model=os.getenv("MODEL_NAME"),
#      temperature=0.8)
# chain = trimer | llm | StrOutputParser()
# ai_msg = chain.invoke(msg)
#
# print("ai_msg=",ai_msg)