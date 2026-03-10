import 'dart:math';

main() {
  /*

    在dart2.12之后引入了空安全,就是把可以存储null值的类型 加一个 问号?变成可选类型
    基本类型不能存储null值.
    空安全可以让编译器在编译期间就检查出错误
    在2.12之前,基本类型可以储存null值,这样,容易引起崩溃.
    例如，如果一个方法要一个整数,但接收到null，程序将引发运行时错误。因为2.12之前, 普通类型可以存储null,
    例如 int a = null String str = null
    2.12引入空安全以后,null只能存入到可选类型中:
    String? str = null;
    String str2 = null;//报错
    int? age = null;
    int age2 = null;//报错
    引入空安全以后,可以把可选类型,和 基本类型区分开来,这样不会出现崩溃.
    空安全将潜在的运行时错误转变为编辑时分析错误。使用空安全，Dart分析器和编译器会标记非空变量是否：
    未被初始化为非null值
    已被赋值为null值。
    这些检查允许您在部署应用程序之前修复这些错误。


      Dart 3内置了空安全。 Dart 3阻止没有空安全的代码运行。
      如果文件中的dart 版本是3.0的,那么就是要求有空安全的,那么 在pubspec.yaml 文件中的 sdk版本要求必须 >= 2.12.0

        如果从 检查您从pub.dev安装的任何包是否有空安全版本

        Dart 2.x和空安全

从Dart 2.12到2.19，您需要启用空安全。您不能在早于Dart 2.12的SDK版本中使用空安全。

要启用空安全，请将SDK约束的下限设置为2.12或更高版本的语言版本。pubspec.yaml文件可能具有以下约束：

environment:
sdk: '>=2.12.0 <3.0.0'

终端命令找到flutter所在目录
which flutter

 把flutter 版本改成3.0.0  进入flutter目录 git checkout 3.0.0 对应dart sdk是2.17.0 ,在这个版本下,可以自由切换dart 2.0.0 和 2.12
 ,因为不是 dart 3.0不要求强制空安全,强制空安全必须 要求配置文件 约束 sdk版本>=2.12
     */

  // String? str = null; //2.12之前报错,没有可选类型
  // String str2 = null;//2.12之前正确,可以给基本类型赋值 null
  // int? age = null; //2.12之前报错,没有可选类型
  // str2.length;//2.12之前版本,不使用空安全的时候,运行报错  :NoSuchMethodError: The getter 'length' was called on null. 没有这种方法错误.读取方法` length `的值为null。
  //查看笔记中的空安全之前的类型结构图.null是所有类型的子类,而且null不定义任何方法.所以如果一个 类型,例如字符串String,里面的值是null,那么他调用里面的任何方法都会报错

  // int age2 = null;//2.12之前正确,可以给基本类型赋值 null


   Never? a = null; //Never类型,是空安全之后,所有类型的子类型,空安全之前所有类型的子类型是Null
   // 新的底部类型 Never 没有值。（哪种值同时是 String、bool 和 int？）该表达式永远无法成功完成评估。它必须抛出异常、中止执行，或者以其他方式确保期望表达式结果的周围代码永远不会运行。
  Null b = null;//Null类型不需要?就能赋值 null

  if(a is String?){
    print(" ${a.runtimeType} a是 String?的子类型");
  }
   if(b is String?){
     print(" ${b.runtimeType} b是 String?的子类型");
   }

/*
  //基本类型作为函数返回类型的时候,返回空 空安全会报错.
  // 没有空安全只会警告提示,但是可以运行,这样就有可能返回一个null

  String fun2(){
        //空安全下这里报错,因为没有返回 String
  }
*/

  // 未初始化的变量
  /*
  当您声明一个变量时，如果您没有给它一个显式的初始化器，Dart 将使用 null 进行默认初始化

   */
  /*
  int a; //没有空安全的时候, 默认变量的初始化是null
  // print(a); //空安全下,使用没有赋值的 变量报错
  A a1;
  // print(a1);
*/
  // print(A.c); //非空安全下 static 和 全局变量不初始化 默认是null
  // print(g_a);





  //测试用 Never作为返回值的抛出异常
  // wrongType("abc",123);
  var p1 = Point(100, 100);
  var p2 = Point(100, 100);
  // if (p1 == A()){ // 演示类型不同,抛出异常,返回值是Never类型
  if (p1 == p2){
    print("相等");
  }else{
    print("不相等");
  }
}










// int g_a;//空安全情况下,全局变量必须初始化
class A {
  int a = 0; //空安全下, 类的 成员需要初始化,否则报错
// int b; //不是空安全下, 成员变量不初始化不报错
// static int c;  //不是空安全情况下,static默认值是null,
}
//空安全之后的新的底部类型Never可以用来抛出异常
Never wrongType(String type, Object value) {
  throw ArgumentError("类型错误: 期望类型是Point,传入的是 ${value.runtimeType}");
}
// 使用空安全:
class Point {
  final double x, y;
  Point(this.x,this.y);
  bool operator ==(Object other) {
    if (other is! Point) wrongType('Point', other);
    //不使用空安全,类型不能提升成Point
    print("右边的类型是 ${other.runtimeType}");
    return x == other.x && y == other.y;
  }

// 构造函数和 hashCode...
  /*
  的最后一行访问 other 的 .x 和 .y。即使该函数没有任何返回或抛出，它已经被提升为 Point。
  控制流分析知道 wrongType() 的声明类型是 Never，这意味着 if 语句的 then 分支必须以某种方式中止。
  由于第二条语句只有在 other 是 Point 时才能达到，Dart 会将其提升。
  换句话说，使用 Never 在你自己的 API 中可以扩展 Dart 的可达性分析。
   */
}