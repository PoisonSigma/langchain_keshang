/*
  external关键字翻译过来是外部的意思,在c++中关键字 extern 可以应用于全局变量、函数或模板的声明,就是只是告诉编译器有这个方法,需要再其他文件中寻找定义
  在dart中的使用如下
  这个例子实验external关键字,在普通类中,可以让方法只声明方法名,不实现方法体,子类继承这个方法的时候,可以重写,也可以不重写
  external使用可以让普通类里的方法像抽象类abstract那样,写出抽象方法,就是不实现方法体的方法,但是抽象类的抽象方法,子类继承必须重写
  而普通类的external方法,子类继承以后不是必须实现这些external方法
   */

import '046.dart';

class Person{
 external  breath();
}
class Worker extends  Person{
    @override
  breath() {
    // TODO: implement breath
    // return super.breath();
      print("工人呼吸了");
  }
}
main(){
      var w1 = Worker();
      w1.breath();
}