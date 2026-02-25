from langchain_core.prompts import PromptTemplate


class Person:
    def __init__(self ,age,name):
        self.age = age
        self.name = name
        #@classmethod是类方法的关键字，代表这个方法不用创建对象，可以被类名直接调用,第一个参数是类本身
    @classmethod
    def template(cls, city:str, date:str, template_format:str = "123", **kwargs) -> PromptTemplate:
        result:str = "城市:" + city + date + "天气是"
        print(result)
        pass #pass 是一个空语句，它不执行任何操作，主要起到占位的作用，这里代表函数结束了
#函数调用方式，按照顺序调用可以省略参数名，
#  函数中的关键字参数（Keyword Arguments）(命名参数)
# 在函数调用时，关键字参数允许你通过参数名来指定传递的值，而不必按照函数定义中参数的顺序传递。
#如果不按照顺序调用，可以用=等号+参数名，顺序可以改变，
# 可以混用，但是如果不写=，顺序必须正确
#
Person.template("哈尔滨", template_format="456", date="道里区")

# def add(a:int , b:int,c:Optional[int] = 0 ) -> int :
#     result = a + b + (c or 0)
#     print(result)
#     return result
# add(1,b = 2)

def add2(a:int , b:int,c:int = 0 ) -> int :
    result = a + b +c
    print(result)
    return result
add2(1,b = 2)