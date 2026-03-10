class Person {
  String name;
  int age;

  Person(this.name, this.age);

// Person(String name, int age):this.name = name ,this.age = age; //老式的语法,构造函数参数列表
  action() {
    print("Person: action");
  }

  showInfo() {
    print("Person:showInfo() name = $name , age = $age");
  }
}

class Worker extends Person {
  int workId = 0;
  Worker(this.workId,super.name, super.age) {
    // print("Worker的构造函数");
  }
  // override:翻译过来叫重写,意思是子类把父类的同名方法覆盖了,@override这个关键字可以省略,
  @override
  action() {
    // TODO: implement action
    // super.action();
    // super.showInfo();
    print("Worker action执行了");
    // return super.action();
  }
  // @override //如果使用@override 发现,方法没有在父类中出现,有会警告,提示,重写的方法,不是从父类继承来的
  work(){
    print("work() 工人工作了");
    super.action();
    // this.action();
    action();//this可以省略
  }
  @override
  showInfo() {
    print(" Worker: showInfo() workId = $workId  name = $name , age = $age");
  }
}

main() {
  var w1 = Worker(10000,"张三", 30);
  // w1.action();
  w1.showInfo();
  // w1.work();
}
