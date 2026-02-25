from langchain_community.chat_message_histories import ChatMessageHistory
history1 = ChatMessageHistory()
print(history1)
print(type(history1))#InMemoryChatMessageHistory
history1.add_user_message("你好")
history1.add_ai_message("很高兴认识你,你也好")
history1.add_ai_message("33333")
history1.add_user_message("44444")
print(history1)
print(history1.messages)