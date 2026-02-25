#多重继承一般都是通过接口抽象类,里面每个抽象类都是抽象方法,子类继承的时候需要强制实现抽象方法
#但是mixin这种思想,其他语言是有明确关键字语法 with混入抽象类的,
# 优点是也能像implement这种实现的关键字被子类多重继承,而且mixin不用强制重写方法,
# 里面定义的方法可以直接被子类直接使用
#python中没有直接定义mixin的关键字,但是可以用普通的类来当做mixin的思想使用,
# 普通类就能被多重继承
#例如dart语言可以使用: mixin class 来定义一个混入的类, 子类通过with进行多重继承
from abc import abstractmethod, ABC


class PersonMixin(ABC): #继承ABC,可以让子类强制实现抽象方法EggWhiteGasSystem
    def deepSquat(self):
        print("人深蹲了")
        # 定义一个抽象方法@abstractmethod ,
        # 需要继承ABC类 导入from abc import ABC, abstractmethod
    @abstractmethod
    def EggWhiteGasSystem(self):#蛋清气体系统
        pass


class eggMixin:
    def makeEggWhite(self):
        print("产生出蛋清")

class zhouzhou(PersonMixin,eggMixin):
    def EggWhiteGasSystem(self):
        print("巧克力味的蛋清加速系统才是天下第一,香草味的蛋清屁也很难忘记")


z1 = zhouzhou()
z1.deepSquat()
z1.makeEggWhite()
z1.EggWhiteGasSystem()