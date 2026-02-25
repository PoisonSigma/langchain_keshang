import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv("../assets/openai.env")  # 注意../回退一个路径


# print( os.getenv("OPENAI_API_KEY"))
class Person:
    bike: int

    # def __init__(self, name, age,api:Optional[str] = "192.168.1.100"):
    # def __init__(self, name, age, api: Optional[str] = None ):
    def __init__(self, name, age, api: Optional[str] = os.getenv("OPENAI_API_KEY")):
        self.name = name  # 成员变量
        self.age = age  # 成员变量
        self.api = api
        self.abc = "前年老妖"
        # self.api = api or os.getenv("OPENAI_API_KEY") #or如果左边没有值就是None就认为是false，
        # 那么就执行右边  ， 其他语言的??合并运算符

    def show(self):
        print(self.name, self.age, self.api, self.abc)


'''
# p1 = Person("John", 22,"192.168.1.1")
p1 = Person("John", 22,)
p3 = Person("wang5 ", 30,)
p2 = Person("李四 ", 30,)
p1.show()
p2.show()
p1.name = "aaaa"
p2.name = "bbbb"
p1.age = 1111
p2.age = 2222
p1.show()
p2.show()
num1:Optional[int] = None
print(num1)
num2 = num1 or 999
print(num2)


name2:Optional[str] = None
name3 =  name2 or "abc"
print(name3)

print(id(p1))#id是查看是否是一个对象
print(id(p2))
print(id(Person))
'''
# 类成员变量
Person.bike = 200

pb1 = Person("aaa", 22, "192.168.1.1")
pb2 = Person("bbb", 22, "192.168.1.1")
print(Person.bike)
print(pb1.bike)
print(pb2.bike)
print(id(Person.bike))
print(id(pb1.bike))
print(id(pb2.bike))
pb1.bike = 22222
pb2.bike = 33333
print("戟把离手越进义父离你越远>-------------)三(--> ")
print("戟把离手越进义父离你越远>-阿祖の剑---阿祖の盾---------)三(--> ")
# 单独给类成员对象赋值以后，内存地址就不一样了，就是分别每个对象下的成员变量了
print(Person.bike)
print(pb1.bike)
print(pb2.bike)
print(id(Person.bike))
print(id(pb1.bike))
print(id(pb2.bike))
print("戟把离手越进义父离你越远>-------------)三(--> ")
print("戟把离手越进义父离你越远>-阿祖の剑---阿祖の盾---------)三(--> ")

print("大宝剑广东地区吴彦祖阿祖の剑佛山分祖阿祖の盾")

Person("xxxxx", 999).show()

print("戟把离手越进义父离你越远>-------------)三(--> ")
print("大宝剑广东地区吴彦祖阿祖の剑佛山分祖阿祖の盾")
print("戟把离手越进义父离你越远>---红字增幅+25----------)三(--> ")

def add(a, b):
    print(a + b)
    return a + b
add(1,2)
#
# {
#     {
#
#     }
# }