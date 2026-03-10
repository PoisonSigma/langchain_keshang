import 'StringA.dart';
import 'StringB.dart';
main(){

  // int.parse("123");
  // var i1 = "123".parseInt();
  // print(i1);
  //  var str1 = "456";
  //  var i2 = str1.parseInt();
  // print(i2);
  //动态类型,不能调用扩展里面的方法,只有静态分析出来的类型,才能调用扩展里面的方法
  // 动态类型不起作用的原因是扩展方法针对接收器的静态类型进行解析。
  // 由于扩展方法是静态解析的，因此它们的速度与调用静态函数一样快。
  //  dynamic str2 = "789";//运行时错误,变异时候,正常
  // str2.parseInt();
  // var i3 = "123abc".parseInt();
  // print(i3);
}
