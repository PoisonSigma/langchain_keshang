// 扩展类型的运行时类型是它的表示类型
// 通过下面语法调用表示类型的方法
// is
// if case
// switch case
extension type IntId(int value){  // 表示类型是int

}

void main() {
  var i = IntId(1);

  // 'i' 的运行时类型是表示类型 'int'。
  if (i is int) print(i.value); // 打印 1。
  // 可以在运行时对 'n' 使用 'int' 方法。
  if (i case int x) print(x.toRadixString(10)); // 打印 1。
  switch (i) {
     // case  int a : print("${a.runtimeType}   "); //i的运行是类型是int
    case var b : print("${b.runtimeType}   ");//这个编译器自动提示不出runtimeType,可以自己手写或者复制
  }
}
