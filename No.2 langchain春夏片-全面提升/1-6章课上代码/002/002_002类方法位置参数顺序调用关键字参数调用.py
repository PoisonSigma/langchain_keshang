class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # @classmethod是类方法的关键字，代表这个方法不用创建对象，可以被类名直接调用,第一个参数是类本身
    @classmethod
    def from_name(cls):
        print("这是一个类方法")
        pass#pass 是一个空语句，它不执行任何操作，主要起到占位的作用，这里代表函数结束了

    @classmethod
    def template(cls,city:str,date:str):
        result:str = "城市" + city + date + "的天气是"
        print(result)
        return result

    @classmethod
    def template2(cls,city:str,date:str,road:str):
        result:str = "城市" + city + road + date + "的天气是"
        print(result)
        return result
# p1 = Person("张三", 18)
# Person.from_name()
# Person.template("哈尔滨","今天")
#函数调用方式，按照顺序调用可以省略参数名，
#  函数中的关键字参数（Keyword Arguments）(命名参数)
# 在函数调用时，关键字参数允许你通过参数名来指定传递的值，而不必按照函数定义中参数的顺序传递。
#如果不按照顺序调用，可以用=等号+参数名，顺序可以改变，
# 可以混用，但是如果不写=，顺序必须正确
#
Person.template(date="明天",city="义乌")
# Person.template2( Person,"哈尔滨",road="南岗区大呲花",date="后天")
Person.template2("Harbin",road="南岗区大呲花",date="后天")