main() {
  var a1 = A("abc");
  a1.run();
  outsideFun(a1);
}
outsideFun(A a1){
  // if(a1._str is String){
  //   print("外部函数:  _str的类型是 ${a1._str.runtimeType}");
  //   a1._str.length;
  // }
  a1._str!;
  print("外部函数:  a1._str的类型是 ${a1._str.runtimeType}");
  a1._str.length;
}

/*
扩展类型提升以适用于私有的 final 字段。之前仅适用于局部变量和参数，
现在私有的 final 字段通过空检查和 is 测试可以提升为非空类型。例如，以下代码现在是有效的：
 */
class A {
  final String? _str;

  A(this._str);

  run() {
    if (_str != null) {
      print("类内 _str的类型是 ${_str.runtimeType}");
      _str.length;
    }
  }
}
