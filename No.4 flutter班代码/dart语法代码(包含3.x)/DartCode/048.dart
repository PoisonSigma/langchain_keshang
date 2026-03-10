/*
abstract关键字定义抽象类
抽象类里的方法如果没有写方法体,就是抽象方法,子类必须实现
抽象类中的方法如果实现了方法体,就是普通方法,extends继承 子类可以不实现
*/
abstract class Person {
  action(); //只有方法名,没有方法体,这种方法是抽象方法,子类继承,必须实现抽象方法
  breath() {
    //这个方法有方法体,是普通方法,extends继承,子类可以不重写普通方法
    print("person 人类呼吸了");
  }
}

class Worker extends Person {
  @override
  action() {
    // TODO: implement action
    // throw UnimplementedError(); //这个是编译器自动留下的代码,意思是抛出一个异常,
    // 代表这段代码还没有实现,只有在开发阶段才使用这个异常,自己写的时候删掉这行就行
    print("工人工作了");
  }
}
 class Student extends Person{
  @override
  action() {
    // TODO: implement action
    print("学生读书");
  }

}
//抽象类可以继承抽象类,抽象类可以不实现父类的抽象方法,可以定义自己的抽象方法
abstract class superMan extends Person{
      fly();
}
class womenSuperman extends superMan{
  @override
  action() {
    // TODO: implement action
    print("使用了激光眼");
  }

  @override
  fly() {
    // TODO: implement fly
    print("飞行了,但是有阻力");
  }

}
main() {
  var w1 = Worker();
  // w1.action();
  // w1.breath();

  var s1 = Student();
  // s1.action();
  // s1.breath();
  // 抽象类不能被实例化，只有继承它的子类可以
  // Person();
  // Student();

  var ws = womenSuperman();
  ws.fly();
  ws.action();
  ws.breath();
}
