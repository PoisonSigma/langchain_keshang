/*
类型推断Type inference
分析器可以为fields:字段成员变量属性,
方法methods、
局部变量local variables
泛型类型参数推断类型。(上节课讲过List<>的类型推断)
当分析器没有足够的信息推断出特定类型时，它会使用动态类型dynamic。

 */


/*
//1. 当分析器没有足够的信息推断出特定类型时，它会使用动态类型dynamic
main(){
  //1.1泛型中,自己明确了类型注释,就不推断了,例如下面的dynamic
  Map<String, dynamic> arguments = {'argA': 'hello', 'argB': 42};//自己指定泛型的类型注释
  // 1.2 使用var或final，让Dart推断类型



  var arguments2 = {'argA': 'hello', 'argB': 42};//   String和 int的 共同父类是Object ,所以推断出类型是  Map<String, Object>
  final arguments3 = {};//<dynamic,dynamic>//没有足够信息推断出类型,所以使用dynamic动态类型
}


 */

//2.没有声明或继承类型但有初始值的字段，将根据初始值推断出一个类型。
class Animal{
  // String a ; //这个是field ,字段,属性,成员变量
  var b = "abc";//没有声明或继承类型但有初始值的字段，将根据初始值推断出一个类型。
  String Call(){
    return "动物叫";
  }
  Animal getObj( Animal obj ){
      return Animal();
  }
}

//3.override覆盖重写了父类的方法,将继承超类方法或字段的类型。
class Cat extends Animal{
@override
   Call() { //override覆盖重写了父类的方法,没有指定类型的字段或方法，将继承超类方法或字段的类型。
  return "喵喵";//如果这行注释掉,会报错,因为这个方法是覆盖了父类的,需要返回String
  }
  @override

  // Cat getObj( Animal obj ) { //传入参数只能是父类或者超类
  //   Cat getObj( Object obj ) { //传入参数只能是父类或者超类
  Animal getObj( Object obj ) {
    // TODO: implement getObj
    // return Cat(); //之前讲过返回类型可以是父类或者子类型
    return Animal(); //之前讲过返回类型可以是父类或者子类型
  }
}



// 4.静态字段推断
// 静态字段和变量的类型由其初始值推断出来。如果遇到循环（即推断变量的类型取决于知道该变量的类型），推断会失败。

class A{

  static var a = "abc";//静态字段和变量的类型由其初始值推断出来
  String b = "abc";
  // static var c = b;//The instance member 'b' can't be accessed in an initializer 实例成员b不能再初始化中被访问
  // static var d = e; //循环推断不行
  // static var e = d;
}


/*
// 5.局部变量推断
// 局部变量的类型从它们的初始化器推断，后续的赋值不会被考虑进去。



main(){
  // 静态分析：失败
  var x = 3; // 局部变量的类型从它们的初始化器推断,x 被推断为 int 类型。
  // x = 4.0;//后续的赋值不会被考虑进去。

  //  静态分析：成功
  //解决方法,添加一个类型注释,用一个公共的父类
  num y = 3; // num 可以是 double 或 int。
  y = 4.0;
}
*/



// 6.构造函数调用和泛型方法调用的类型参数,根据上下文组合向上推断

main() {
  // 推断为 <int>。
  List<int> list1 = [];

// 推断为 <double>。
  var list2 = [3.0,4,5];
  var i1 = 3.14.toInt();//转换为int

  // Dart 在推断 map() 方法的类型参数时将这个返回类型作为向上的信息：
  // 把每次遍历的返回类型作为向上的信息,返回给result1

   var result2 =  list2.map((e) => e+1);//e是num e+1还是num
  var ints = list2.map((x) => x.toInt());// 推断为 Iterable<int>。

// Dart 在推断 map() 方法的类型参数时将这个返回类型作为向上的信息： <int>。
}


