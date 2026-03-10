/*
扩展类型提升以适用于私有的 final 字段。之前仅适用于局部变量和参数，
现在私有的 final 字段通过空检查和 is 测试可以提升为非空类型。例如，以下代码现在是有效的：
 */
//类的成员变量在运行时可以赋值给新的变量赋值以后的类型提升

import '../013b.dart';
import '../036.dart';

main() {
  var a = A("abc");
  a.run();
  outSideFun(a);
}
outSideFun(A a1){
  if (a1._str != null) {
    // _str.length;//错误,编辑期间无法类型提升
    print("str的类型是 ${a1._str.runtimeType}"); //运行期编译器对成员变量类型提升,但是编辑期间无法类型提升
    String str2 = a1._str;//这段代码需要把dart版本改成>=3.2
    str2.length;
  }

}

class A {
  // final String? _str;
  final String? _str; //需要时 final 的私有变量可以类型提升
  A(this._str);

  run() {
    if (_str != null) {
      _str.length;//类型提升了
      print("str的类型是 ${_str.runtimeType}"); //运行期编译器对成员变量类型提升,但是编辑期间无法类型提升

      String str2 = _str;//这段代码需要把dart版本改成>=3.2
      str2.length;
    }
  }

}



