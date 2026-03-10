class Person {
  String name;
  int age;

  Person(this.name, this.age);

  action() {
    print("Person: action");
  }

  showInfo() {
    print("Person:showInfo() name = $name , age = $age");
  }
}
class Worker extends Person {
  //子类可以有自己的属性
  int workId; //工作ID
Worker(this.workId,super.name,super.age);

  // override:翻译过来叫重写,意思是子类把父类的同名方法覆盖了,@override这个关键字可以省略,
  //
  // 重写方法以后,子类的对象调用的方法是子类自己的
  // action() {
  //   print("工人 action");
  // }

  work() {
    //子类特有的方法

    super.action(); //通过super关键字,显示调用父类的方法

    this.action();//this可以省略
    action();
    // print("工人工作");
  }
}
main(){
   var w1 = Worker(10000, "张三", 30);
   // w1.action(); //自动继承父类的方法
  w1.work();
}