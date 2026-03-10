import 'dart:io';

import '050.dart';

main(){
    var a = 100;//这里右边是一个字面量,所有左边var静态分析就能得到结果是 int类型
    var f1 = fun1();//这里右边是一个函数,而这个函数的返回类型没设置,所以编译器无法静态分析出来他的类型,所以var也只能显示dynamic类型
}

//下面这3个函数为了证明,自己不给函数写明确的返回类型,编译器无法静态分析出函数的返回类型,那么就会认为函数返回是dynamic类型
//所有函数的返回类型,编译器都没法退出来他的精确类型,那么就会显示动态类型
//除非是async异步函数才会强制推断出来时Future类型,但是他里面的类型限定,例如 int String之类的类型,还是无法推断出来
fun1(){
  return 1;
}

//选学,异步方法,一定返回一个Future对象,但是如果不设置返回类型,那么编译器也会识别成Dynamic
Future<int> fun2() async {
    sleep(Duration(seconds: 2));
    return 1;
}

fun3() async {
  sleep(Duration(seconds: 2));
  return 1;
}