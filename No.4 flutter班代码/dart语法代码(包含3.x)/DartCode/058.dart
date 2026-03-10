//常量构造函数 需要在构造函数左边加 const,同时,所有成员变量都是final类型,这样赋值一次以后参数就不会改变,或者是static,static const
class Person {
  final String name;
  final int age;
  static int a = 100; //静态变量
  static const int b = 300;
  const Person(this.name, this.age);
  // Person(this.name,this.age);
/*
  Can't define a const constructor for a class with non-final fields. (Documentation)
    Try making all of the fields final, or removing the keyword 'const' from the constructor.
    里面的字段不是final的时候,不能定义一个构造函数,把name和 age改成final,这样初始化赋值一次以后就不会改变了
   */
  const Person.setNameAge(this.name, this.age);
}

main() {
  var p1 = const Person("张三", 18);
  var p2 = const Person("张三", 19);
  // var p1 =  Person("张三", 18);
  // var p2 =  Person("张三", 18);
  // print("p1.hashCode = ${p1.hashCode}");
  // print("p2.hashCode = ${p2.hashCode}");

  //identical 返回2个对象是否相同
  var result = identical(p1, p2);
  // print("result = $result");

  // final a;
  // a = 100;
  // // a = 101;
  //  const b =101;
  //  // b = 101;
  // Person.a = 101;
  // Person.a = 102;

  print(Person.b);
}
