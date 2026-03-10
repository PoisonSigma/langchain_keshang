//extends继承和子类执行父类构造函数
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
  int workId;

  Worker(this.workId, super.name, super.age);

}

main() {
  var w1 = Worker(1000, "张三", 18);
  // w1.showInfo();//父类的方法,自动就有
  // w1.action();


}
