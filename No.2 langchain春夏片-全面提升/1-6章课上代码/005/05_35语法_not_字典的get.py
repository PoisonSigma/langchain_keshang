# fun1 = lambda x: not x.get('chat_history', False)
# result = fun1({"chat_history": "abc124"})
# print(result)
#get可以取到字典里面的key的对应的value
dic1 = {"name":"张三"}
value1 = dic1.get("name")
print("value1=", value1)
value2 = dic1["name"]
print("value2=", value2)
value3 = dic1.get("name2")
print("value3=", value3)
value4 = dic1.get("name2","王二麻子")#get可以指定默认值,如果没写,就是None
print("value4=", value4)
fun1 = lambda x: x.get('chat_history', False)
result = fun1({"chat_history": "abc124"})
print(result)
result5 = {"chat_history": "abc124"}.get('chat_history', False)
print("result5=", result5)
result6 = not False #not是取反,真取反就是假
print("result6=", result6)
result7 = not "abc123" #not是取反,真取反就是假
print("result7=", result7)
if not "abc123": #所有的字符串判断都是真,除非是空
    print("真")
else:
    print("假")
