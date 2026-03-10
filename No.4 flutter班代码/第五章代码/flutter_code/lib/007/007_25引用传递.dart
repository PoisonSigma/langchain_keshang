main() {
  var a1 = A(18);
  print(a1);
  fun1(a1);
  print(a1);
}
//函数里面参数是对象的情况下,那么改变对象里面的成员变量,也改变外面传递进来的对象的值
fun1(A obj) {
  obj.a = 100;
}

class A {
  int a;

  A(this.a);

  @override
  String toString() {
    return 'A{a: $a}';
  }
}
