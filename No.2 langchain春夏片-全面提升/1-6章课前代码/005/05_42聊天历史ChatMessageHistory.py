#ChatMessageHistory 通过 add_ai_message 添加ai mseesge
#add_user_message 添加user message

from langchain_community.chat_message_histories import ChatMessageHistory
chat_history = ChatMessageHistory()#ChatMessageHistory按照添加顺序保存信息
#添加用户信息
chat_history.add_user_message(
    "如何一秒钟变男神?"
)
#添加ai聊天历史
chat_history.add_ai_message("首先要一秒钟睡着觉")
chat_history.add_ai_message("3333333")
chat_history.add_user_message(
    "如何10秒钟变男神?"
)
print(chat_history)
print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")

chat_history.messages
# print("33333333333")
print(chat_history.messages)

