# []中括号,后面的值类型,d1: dict[str, str | int | float]  用| 分别代表可以是多重类型,例如int 或者 float 或者 str
#[]左边的类型,就是键key的类型也可以是:int , float,tuple,str,bool


d1 = {"name":"张三",
      "id":1,
      "age":18,
      "money":3.14
      }
d1["name"] = "李四" #通过[]中括号+左边的键key修改value值
print(d1["name"])
b1:bool = True
print(b1)
b1 ="abc"
# Python 里，你给出的代码虽然给变量 b1 标注了 bool 类型，但 Python 是动态类型语言，
# 类型标注仅起到提示作用，并不会对变量的实际类型进行严格约束。
# 当你给 b1 赋值为字符串 "abc" 时，它的实际类型就变成了字符串。
# 由于 "abc" 是一个非空字符串，根据 Python 的真值测试规则，
# 非空字符串在布尔上下文中被视为 True

# print(b1)
b1 = None #字符串为None才为假,只要有值就不是False
if(b1):
    print("真")
else:
    print("假")

#添加key,如果存在就修改,不存在添加
d1["abcde"] = 999
print(d1["abcde"])


t1 = (1,3)
d2 = {True:"张三",
      18:1,
      t1:18,
      (2,3):19,
      "money":3.14
      }
d2[18] = 2
print(d2[18] )
d2[(2,3)]= 20 #修改key为元组的值
print(d2[(2,3)])
# 删除键值

d2.pop((2,3))
# print(d2[(2,3)])#报错(2,3)不存在 KeyError: (2, 3)
d2.copy()# 清空

