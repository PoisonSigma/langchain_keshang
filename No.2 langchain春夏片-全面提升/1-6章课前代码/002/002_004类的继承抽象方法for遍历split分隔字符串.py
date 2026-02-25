from abc import abstractmethod #导入 abc  abstractmethod 装饰器。
from os.path import split

from typing_extensions import override


class Person:
    def __init__(self):
        pass
    def talk(self):
        print("我是人类")

    """
     Python 里，抽象方法是一种在抽象基类中定义但没有具体实现的方法，
     它只是声明了方法的签名（包括方法名、参数列表等），
     具体的实现要由继承该抽象基类的子类来完成。
     抽象方法主要用于定义接口规范，确保子类实现特定的方法，从而提高代码的可维护性和可扩展性。下面从多个方面详细介绍 Python 中的抽象方法。
    """
    @abstractmethod
    def parser(self,text:str):
        pass

#定义子类，在类名后的括号中指定要继承的父类名称Student是后面括号中Person的子类
class Student(Person):
    def parser(self,text:str):
        print("学生的分析器" + text)
    #重写父类方法
    # @override #可以省略
    def talk(self):
        print("我是学生")
Student().talk();
Student().parser("123")
names = "白金之星,绿色法皇,愚者"
list1 = names.split(",")#字符串.split()把后面括号里面用逗号分隔成List列表
print(list)
for item in list1:  #遍历列表
    print(item)

list2 = [1,2,3]
for item in list2: print(item)
