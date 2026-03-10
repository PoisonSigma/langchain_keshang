/*
类型推断Type inference
分析器可以为fields:字段成员变量属性,
方法methods、
局部变量local variables
泛型类型参数推断类型。(上节课讲过List<>的类型推断)
当分析器没有足够的信息推断出特定类型时，它会使用动态类型dynamic。

 */

/*
main(){
//1. 当分析器没有足够的信息推断出特定类型时，它会使用动态类型dynamic
//1.1泛型中,自己明确了类型注释,就不推断了,例如下面的dynamic
Map<String,dynamic> m1 = {"name":"张三","age":18};
var m2 = {"name":"张三","age":18};//String和 int的 共同父类是Object ,所以推断出类型是  Map<String, Object>
}

 */
/*
//2.没有声明或继承类型但有初始值的字段，将根据初始值推断出一个类型。
class Animal{
   var str = "abc";//没有声明或继承类型但有初始值的字段，将根据初始值推断出一个类型。
//String str2;//这个是field ,字段,属性,成员变量

}
class Cat extends Animal{
  //下面是继承父类的类型
  @override
  set str(String _str) {
    // TODO: implement str
    super.str = _str;
  }
  @override
  // TODO: implement str
  String get str => super.str;
}
 */
/*
//3.override覆盖重写了父类的方法,将继承超类方法或字段的类型。
class Animal {
  Animal getObj(){
    return Animal();
  }
  into(Animal obj){//试验入参
  }
}
class Cat extends Animal{
  @override
  //函数返回类型,可以是父类或者子类
  /*
  Animal getObj() {
    return Animal();//可以返回父类
  }
   */
  Cat getObj() {
    return Cat();//可以返回子类
  }
  @override
  //重写方法入参可以是父类或者超类
  // into(Animal obj) {
  // }
  into(Object obj) {
  }
}

 */
/*
// 4.静态字段推断
// 静态字段和变量的类型由其初始值推断出来。如果遇到循环（即推断变量的类型取决于知道该变量的类型），推断会失败。
class A{
  static var str;
  static var str2 = "abc123";
  // static var str3 = str4 ; //不能循环初始化值
  // static var str4 = str3;
}
main(){
    print(A.str);
    print(A.str2);

}


 */
/*
// 5.局部变量推断
// 局部变量的类型从它们的初始化器推断，后续的赋值不会被考虑进去。
main(){
  // 静态分析：失败
  //   var x = 3; // 局部变量的类型从它们的初始化器推断,x 被推断为 int 类型。
  //   x = 3.14;//后续的赋值不会被考虑进去。
  /*
  //区别:动态类型可以赋值任意类型
  dynamic x = 3;
  x = 3.14; //右边是生产者 左边保存值的是消费者 ,也可以认为,左边是指针, 右边是创建的对象
  x = "abc";
  print(x);
   */
  //正确用法:用共同父类去保存不同子类的对象
  num x = 3;// num 可以是 double 或 int。
  x = 3.14;




}

 */
// 6.构造函数调用和泛型方法调用的类型参数,根据上下文组合向上推断
main() {
  List list1 = []; //推不出来类型,就是dynamic
  list1.add("abc");
  list1.add(123);
  var list2 = [3, 4, 5, 3.14]; //推断出int double共同的父类是num
  var i1 = 3.14.toInt();
  // print(i1);
  var result1 = list2
      .map((e) => e.toInt())
      .toList(); // Dart 在推断 map() 方法的类型参数时将这个返回类型作为向上的信息：
  var result2 = list2.map((e) => e + 0.1).toList(); //返回类型是 double
  var result3 = list2.map((e) => print(e)).toList(); //返回类型是 double
}
