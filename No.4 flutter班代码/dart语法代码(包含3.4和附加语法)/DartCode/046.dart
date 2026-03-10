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
// extends关键字,继承父类,右边是父类,左边是子类,默认情况下,什么都不写,子类拥有父类全部的方法和成员变量,但是必须初始化父类的构造函数
// extends关键字只能继承1个父类,如果要继承多个父类,需要使用implements,后续讲
// class Worker extends Person{
//   //The superclass 'Person' doesn't have a zero argument constructor. 超类 Person没有0参数的构造函数
// }
class Worker extends Person{
  //子类可以有自己的属性
  int workId;//工作id

  // 子类的构造函数必须把父类的构造函数也初始化了,这里指的初始化是指调用父类构造函数,同时给构造函数参数赋值
  // 不只是dart语言,其他一些语言,调用子类构造函数的时候,也要求调用父类的构造函数
  // 例如swift:中super.init()是调用父类的构造函数.super.viewDidLoad()调用父类的viewDidLoad

  // 初始化父类构造函数可以在冒号后面的初始化列表里面写super(参数列表)
  // Worker(String name,int age):super(name,age);//这个是构造函数参数列表的语法

// Worker( String name, int age) :Person(name, age);//错误,不能写成父类Person
//简写方法
Worker(this.workId, super.name,super.age);
// Worker()
}
main(){
      var w1 = Worker(10000,"张三", 30);
      w1.age = 99;
      w1.showInfo();


}