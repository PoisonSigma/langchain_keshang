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
  String str1 = "abc";
  str1.length;
  String? str2 = null;//空安全之后可以使用可选类型来存储 null和普通类型
  str2?.length;
  // str2!.length;//强制解包发现值为null会报错
  /*
  String str3 = null; //空安全之后,null不能被存入到基本类型
  str3.length;
  Null a1 = null;
 // String? str = null; //2.12之前报错,没有可选类型
  // String str2 = null;//2.12之前正确,可以给基本类型赋值 null
  // int? age = null; //2.12之前报错,没有可选类型
  // str2.length;//2.12之前版本,不使用空安全的时候,运行报错  :NoSuchMethodError: The getter 'length' was called on null. 没有这种方法错误.读取方法` length `的值为null。
  //查看笔记中的空安全之前的类型结构图.null是所有类型的子类,而且null不定义任何方法.所以如果一个 类型,例如字符串String,里面的值是null,那么他调用里面的任何方法都会报错

  // int age2 = null;//2.12之前正确,可以给基本类型赋值 null

   */

/*
  空安全将潜在的运行时错误转变为编辑时分析错误。使用空安全，Dart分析器和编译器会标记非空变量是否：
  未被初始化为非null值
  已被赋值为null值。
  这些检查允许您在部署应用程序之前修复这些错误。
 */
  String str4;
  // print(str4);//空安全要求非空类型的变量在使用之前被初始化

  Never? a = null;//Never类型,是空安全之后,所有类型的子类型,空安全之前所有类型的子类型是Null
  // fun1();
  Null b = null;//Null 存储null不需要加?
  String? str = null;
}
// Null fun1(){ //Never和Null都可以抛出异常或者错误

Never fun1(){
  throw FormatException("123");
  // throw ArgumentError("123");
}



//基本类型作为函数返回类型的时候,返回空 空安全会报错.
// 没有空安全只会警告提示,但是可以运行,这样就有可能返回一个null
/*
String fun2(){
    return null;
}
 */