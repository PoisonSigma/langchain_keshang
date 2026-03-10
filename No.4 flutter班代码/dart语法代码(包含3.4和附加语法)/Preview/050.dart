abstract class Person {
  String name = "张三";
  abstract int age; //抽象属性,要求子类必须实现这个属性,
  action();

  breath() {
    print("Person 人呼吸了");
  }
}

abstract class Fighting {
  yongChun();

  wangBaQuan() {
    print("使用了王八拳,双手轮起来,是对手没见过的拳法,对手蒙圈");
  }
}
class Sleeping {
  sleep() {
    print("睡觉了");
  }
}
//extends要求,必须重重写抽象方法和抽象 属性,普通方法breath不用重写. extends继承,可以使用super关键字调用父类的普通方法
class Student extends Person {
  //抽象属性必须实现
  @override
  int age = 18;

  @override
  action() {
    // TODO: implement action
    print("学生学习");
    // super.action();//注意,抽象方法是不能被调用的
  }

  @override
  breath() {
    // TODO: implement breath
    super.breath();
    print("学生自己也会呼吸");
  }
}

// implements在其他语言中叫做 遵守协议,或者继承接口.作用是可以同时继承多个父类
// implements 可以同时继承多个父类,要求实现父类所有方法,不管是不是抽象的,不能使用super.关键字调用父类方法,因为所有方法都会被当做抽象方法
class Worker implements Person, Fighting,Sleeping {
  @override
  int age = 30;

  //父类的非抽象属性也被当做抽象属性,必须实现
  @override
  String name = "工人老李";

  @override
  action() {
    // TODO: implement action
    print("工人工作");
  }

  @override
  breath() {
    // TODO: implement breath
    print("工人呼吸");
  }

  @override
  wangBaQuan() {
    // TODO: implement wangBaQuan
    // 不能使用super.关键字调用父类方法,因为所有方法都会被当做抽象方法
    // super.wangBaQuan();//错误The method 'wangBaQuan' is always abstract in the supertype,方法wangBaQuan总是抽象的
    print("工人使用了中国王八拳,左右手轮流旋转攻击,是外国选手没见过的拳法,对手一脸懵逼");
  }

  @override
  yongChun() {
    // TODO: implement yongChun
    print("大吼一声咏春叶问,然后直接切了对手中路,把对手打到");
  }

  @override
  sleep() {
    // TODO: implement sleep
    print("工人睡觉了");
  }
}



main() {
// var s1 = Student();
// s1.breath();
// s1.action();

  var w1 = Worker();
  w1.action();
  w1.breath();
  w1.yongChun();
  w1.wangBaQuan();
}
