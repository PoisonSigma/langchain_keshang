# 执行 p = Person("张三", 18) 时，Python 会创建一个 Person 类的实例对象，
# 并将这个对象作为 self 参数传递给 __init__ 方法。在 __init__ 方法内部，
# 通过 self.name = name 和 self.age = age 为这个实例对象设置了 name 和 age 属性。
import os
import sys
from typing import Optional

from dotenv import load_dotenv

load_dotenv("../../assets/openai.env")#注意../回退一个路径

class Person:
    money: int = 20  # 类属性，在init方法外面定义的属性

    def __init__(self, name: str, age: int ,api:Optional[str] ="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO") -> None:
        self.name = name  # 实例属性属于类的每个实例，在实例创建时通过 __init__ 方法进行初始化。每个实例都有自己独立的实例属性副本，其生命周期与实例相同。
        self.age = age
        self.api = api
    def show(self):
        print(self.name, self.age, self.money,self.api)


p1 = Person("张三", 18)
print(sys.getsizeof(p1))
p1.show()
p1.age = 30
# 注意不要有多余空格缩进
Person.money = 9999


p1.show()
print(sys.getsizeof(p1))

p2 = Person("李四", 20)
p2.show()
address1 = id(Person.money)
print(id(Person.money))
print(id(p1.money))
print(id(p2.money))
p1.money =11111
p2.money =22222
Person.money = 33333

print(p1.money)
print(p2.money)
print(Person.money)
print(id(Person.money))
print(id(p1.money))
print(id(p2.money))
str1 = "123"