//构造函数中的[]和{} 跟普通函数一样,   [] 可选参数列表和 {} 命名参数列表,里面的参数都是 可选类型,或者是有默认值的非可选类型,
// {}大括号多了一个required 必填项
// 子类继承父类中的[]和{}的时候,也要加上括号
//{}大括号里面调用的时候要有 变量名:, {}里面定义的时候变量要有默认值,或者是必填项required,或者是可选类型的参数
/*
class Person {
  /*
  String name;//非可选类型

  // Person({this.name = "张三"});
Person({required this.name});
   */
/*
  int? age;
  // Person({ this.age });
  // Person({ required this.age });
  Person({ this.age = 18});
 */
  String name;
  int? age;

  Person({required this.name , this.age});

  showInfo() {
    print("name= $name  age =$age");
  }
}

class Worker extends Person {
  Worker({required super.name,super.age});
}
 */
class Person {

  String name;
  int? age;

  Person([ this.name = "老六" , this.age]);

  showInfo() {
    print("name= $name  age =$age");
  }
}

class Worker extends Person {
      Worker([super.name,super.age]);
}


main() {
  // var p1 = Person(name: '李四',age: 18);
  // p1.showInfo();
  // var w1 = Worker(name: '老五',age:18);
  // w1.showInfo();

  //下面开始是 []的表演
  // var p1 = Person("老七",30);
  // p1.showInfo();
  var w1 = Worker("老七",30);
  w1.showInfo();

}
