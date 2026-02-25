inputs = {}
res = inputs.get("messages", [])
print("res=",res)
if  messages := inputs.get("messages", []): #这里第一件事是先把右边复制给messages,再判断messages
    message = messages[-1]  # -1是list里面的最后一个元素,每次
# 在 Python 中，空列表[]在布尔上下文中被视为假值（False）#
if []:#如果if 判断条件是[]空列表,那么就是假
    print("非空list")
else:
    print("[]1")
# else:
#     raise ValueError("No message found in input")
print("messages=",messages)
# print(message)