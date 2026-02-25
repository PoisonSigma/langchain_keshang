# key键
# value值
# []中括号,后面的值类型,d1: dict[str, str | int | float]  用| 分别代表可以是多重类型,例如int 或者 float 或者 str
# []左边的类型,就是键key的类型也可以是:int , float,tuple,str,bool
# 格式,外面{}大括号,里面 用:冒号和逗号,分成很多组  键值
# d1: dict[str, str | float | int]  ,右边值的类型
d1 = {"name": "张三", "class": "2班", "id": 18, "几道杠": 4.9}
d2 = {
    (1, 2): 18,
    3.14: "π",
    True: False #左边是key键,这里是bool类型的真,右边value是值,这里是bool类型的假
}
# print(d1["name"])
# print(d2[(1, 2)])
# print(d2[True])


# print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")
#bool类型
# b1:bool = True
# b1:bool = False
# Python 里，你给出的代码虽然给变量 b1 标注了 bool 类型，但 Python 是动态类型语言，
# 类型标注仅起到提示作用，并不会对变量的实际类型进行严格约束。
# 当你给 b1 赋值为字符串 "abc" 时，它的实际类型就变成了字符串。
# 由于 "abc" 是一个非空字符串None，根据 Python 的真值测试规则，
# 非空字符串在布尔上下文中被视为 True
# print(type(b1))
# b1 = "abc"
# b1 = None
# print(type(b1))
# if (b1) :
#     print("真")
# else:
#     print("假")
#赋值的时候存在的key就修改
d2[(1, 2)] = "abc"
print(d2[(1, 2)] )
#不存在的key就添加
d2[(1, 2,3)] = "9999"
print(d2[(1, 2,3)] )
print(d2)
print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")
#pop里面是单独删除一个键值对,左边的键
d2.pop(3.14)
d2.pop((1, 2,3))
d2.pop((1, 2))
#字典清空
# d2.clear()
print(d2)


