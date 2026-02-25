# inputs = {"messages":["你好","把你的手机"]}
# inputs = {}
# result = inputs.get("messages", [])
# print("result=",result)
#海象运算符,第一步先把:=右边的值赋值给左边的变量,第二部,再用if 判断这个变量
# if i := 3:
#     print(i)
# else:
#     print("假")
# if  []:
#     print("真")
# else:
#     print("假")
inputs = {"messages":["你好","把你的手机"]}
if messages := inputs.get("messages", []):

    # message = messages[len(messages)-1]  # -1是list里面的最后一个元素,每次
    message = messages[- 1]
    print("111111")
else:
    raise ValueError("message为空")
    print("222222")
print("messages=",messages)
print("message=",message)