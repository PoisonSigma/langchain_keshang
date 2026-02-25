result = {"name":"张三"}.get('name1')#get 是 字典里面取一个value
print("result=", result)
result = {"name":"张三"}.get('name2',"1")#get 是 字典里面取一个value,逗号后面是默认值,如果取不到,就返回默认值
print("result=", result)
# result = not False #not 是取反
# print("result=", result)

fun1 =  lambda x: not x.get('chat_history', False)#如果发现有聊天历史,就返回,如果没有,反返回false,再not取反,等于返回Ture
result1 = fun1({"chat_history":"abc"})#能取到,就返回"abc",再取反就是false
print("result1=", result1)
result = not "abc" #右边的字符串取反还是False,字符串被判断的时候,只要不空就是Ture
if "abc":
    print("真")
else:
    print("假")
print("not abc result=", result)
#
result2 = fun1({"chat_history":"abc"})
print("result2=", result2)
