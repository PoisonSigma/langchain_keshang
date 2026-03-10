//下面是不能使用const 创建对象的场景,因为构造函数不是const常量构造函数
/*
class Person{
  String name;
  int age;
  Person(this.name,this.age);
}
main(){
   var p1 = const Person("张三", 18); // 错误
  //The constructor being called isn't a const constructor. (Documentation)
  // Try removing 'const' from the constructor invocation.
  //构造函数被调用的不是const构造函数,尝试删 const 从构造函数调用中
}
 */

//常量构造函数 需要在构造函数左边加 const,同时,所有成员变量都是final类型,这样赋值一次以后参数就不会改变,或者是static const
class Person {
  // String name;
  // int age;
  final String name;

  // int age =  18;  //需要所有成员都是 final, Error: Constructor is marked 'const' so all fields must be final.
  // Field isn't final, but constructor is 'const'.
  //   int age =  18;
  final int age;
  final id = 10000; //是final ,因为有默认值,可以不用放在构造函数里
  static int a = 100; // static不属于某一个对象,所以也可以
  static const int b = 200; //static 成员也可以,但是const必须是static
  const Person(this.name, this.age);

  /*
  Can't define a const constructor for a class with non-final fields. (Documentation)
    Try making all of the fields final, or removing the keyword 'const' from the constructor.
    里面的字段不是final的时候,不能定义一个构造函数,把name和 age改成final,这样初始化赋值一次以后就不会改变了
   */

//常量命名构造函数,跟常量构造函数一样,左边有const,右边是命名构造函数 类名.方法名+(参数),要求所有成员都是final
  const Person.setNameAge(this.name, this.age);
}

main() {
  //复习final
  final int a = 100;
  // a = 101;//错误,final类型只能被复制一次
  final int b;
  b = 101; //可以,赋值了1次
  // b = 102;//错误,赋值了2次
  var p1 = const Person("张三", 18);
  // p1.name = "abc";//'name' can't be used as a setter because it's final. 错误name不能赋值,因为他是final
  var p2 = const Person.setNameAge("张三", 18);
  Person.a; //静态成员,类名.变量名

  print(p1.hashCode);
  print(p2.hashCode);
}
