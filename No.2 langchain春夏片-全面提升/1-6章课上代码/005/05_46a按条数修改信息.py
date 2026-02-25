from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, trim_messages, BaseMessage

msg = [
    SystemMessage("你是一个漂亮年轻的李阿姨,实际年龄比我小"),
    HumanMessage("我是一个钛合金钢铁直男,48k纯爷们,碳纤维的,但是我是软饭男"),
    AIMessage("我给你我的附属金卡"),
    HumanMessage("你在教我做事啊?"),
]

trim_messages = trim_messages(
    msg,
    max_tokens=2,
    token_counter=len,

    strategy="last",  # strategy="last",#last从后截取
    start_on = "human"
)
print("trim_messages=", trim_messages)


