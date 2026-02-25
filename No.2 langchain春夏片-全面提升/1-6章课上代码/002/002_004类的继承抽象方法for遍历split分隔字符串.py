from abc import abstractmethod #导入 abc  abstractmethod 装饰器。

from typing_extensions import override

"""
     Python 里，抽象方法是一种在抽象基类中定义但没有具体实现的方法，
     它只是声明了方法的签名（包括方法名、参数列表等），
     具体的实现要由继承该抽象基类的子类来完成。
     抽象方法主要用于定义接口规范，确保子类实现特定的方法，从而提高代码的可维护性和可扩展性。下面从多个方面详细介绍 Python 中的抽象方法。
    """
class Person:
    def __init__(self):
        pass

    def talk(self):
        print("我是人类")
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def paser(self,text:str):
        pass

"""
#定义子类，在类名后的括号中指定要继承的父类名称
Student是后面括号中Person的子类
"""

"""
#定义子类，在类名后的括号中指定要继承的父类名称
Student是后面括号中Person的子类
"""
class Student(Person):
    def paser(self,text:str):
        result = "学生的输出分析器是" + text;
        # print(result)
        return result

    def walk(self):
        print("学生蹦蹦跳跳")

    # def walk(self):
    #     pass

    # 重写父类方法
    # @override #可以省略
     # @override
    def talk(self):
         print("我是学生")


# Person().talk()


Student().talk()
l1:list[Person] = [Person(),Person()]
print(l1)
l2:list[int] = [1,2,3,4,5]
print(l2)
#for in 遍历List
for item  in l2:
    print("item=" + str(item))
str1 = "abc,bcd,cdefg"
l3 = str1.split(",")#字符串.split()把后面括号里面用逗号分隔成List列表
print(l3)
for item in l3:
    print(item)

result1 = Student().paser("白金之星")
print(result1)