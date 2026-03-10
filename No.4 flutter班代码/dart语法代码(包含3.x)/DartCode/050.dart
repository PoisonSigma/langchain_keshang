abstract class Person{
  String name = "张三";
  abstract int age;
  action();
  breath() {
    print("Person 人呼吸了");
  }
}
abstract class Fighting{
  yongChun();
  wangBaQuan(){
    print("使用了王八拳,双手轮起来,是对手没见过的拳法,对手蒙圈");
  }
}
//extends要求,必须重重写抽象方法和抽象 属性,普通方法breath不用重写. extends继承,可以使用super关键字调用父类的普通方法
class Student extends Person{
  String name = "学生甲";
  @override
  int age = 18;

  @override
  action() {
    // TODO: implement action
    //抽象方法,在子类中重写的时候不能用super关键字去调用父类的方法,因为父类的方法是抽象方法,没有方法体.
    // super.action();
    print("学习学习了");
  }
  @override
  breath() {
    // TODO: implement breath
    super.breath();
    print("学生呼吸了");
  }
}

class Sleeping {
  sleep(){
    print("睡觉了");
  }
}

// implements在其他语言中叫做 遵守协议,或者继承接口.interface 作用是可以同时继承多个父类
// implements 可以同时继承多个父类,要求实现父类所有方法,不管是不是抽象的,不能使用super.关键字调用父类方法,因为所有方法都会被当做抽象方法

class Worker implements Person ,Fighting,Sleeping{
  @override
  int age = 30;

  @override
  String name = "工人甲";

  @override
  action() {
    // TODO: implement action
    print("工人工作了");
  }

  @override
  breath() {
    // TODO: implement breath
    // implements 不能使用super.关键字调用父类方法,因为所有方法都会被当做抽象方法
    //The method 'breath' is always abstract in the supertype.
    //super.breath();//报错了
    print("工人呼吸了");
  }

  @override
  sleep() {
    // TODO: implement sleep
    print("工人睡觉了");
  }

  @override
  wangBaQuan() {
    // TODO: implement wangBaQuan
    print("工人使用了中国王八拳,左右手轮流旋转攻击,是外国选手没见过的拳法,对手一脸懵逼");
  }

  @override
  yongChun() {
    // TODO: implement yongChun
    print("大吼一声咏春叶问,然后直接切了对手中路,把对手打到");
  }

}
main(){
    // var s1 = Student();
    // print(s1.name);
    // s1.action();
    // print(s1.age);
    // s1.breath();
  var w1 = Worker();
  w1.action();
  w1.breath();
  w1.yongChun();
  w1.wangBaQuan();
}