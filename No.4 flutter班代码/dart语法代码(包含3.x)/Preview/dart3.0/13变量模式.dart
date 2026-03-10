main() {
  // 变量模式
  // var a
  // String str
  // final int
  // _ 通配符
  // 变量模式将新变量绑定到已匹配或解构的值。它们通常作为解构模式的一部分出现，以捕获解构后的值。
  // 这些变量在只有在模式匹配时才能够访问的代码区域中处于作用域。

  const x = 1;
  const y = 2;
  var x1, x2;
  switch ((1, 2)) {
    /*
    // 'var a' 和 'var b' 是变量模式，分别绑定到 1 和 2。
    case (var a, var b): // ...
    // 'a' 和 'b' 在 case 体中作用域内,下面演示在外部定于变量用来匹配,但是会提示必须使用常量
        print("$a $b");
     */
  /*
    case (x, y): //外部定义的const常量才能匹配,无法在外部定义变量,这个是常量模式匹配
      print("常量模式匹配");
   */
    // case (x1, x2): //编译报错,不是常量
    // // The expression of a constant pattern must be a valid constant. (Documentation)  Try making the expression a valid constant.
    // // 常量模式的表达式必须是有效的常量。(文档)尝试使表达式成为一个有效的常量。

    // case const (1, 2):
    //   //上面的等价于这样
    //   print("外部定义的const x y,常量模式匹配");
    // case (int a ,int b)
  /*
  //使用final就不能赋值,不用final修饰就是变量,可以赋值
    case (int c,final int d):
      print("变量模式 c = $c d= $d");
      c = 100;
      // d = 200;//报错,d是final只能赋值一次
      print("变量模式 c = $c d= $d");

   */
  /*
  //类型对应不上,无法匹配
    case (int a,String b):
      print("a = $a b = $b");

   */
  //使用 _ 通配符,可以匹配任何类型,用作占位
  //   case (var a ,_):  //第二个元素使用了通配符,只留下a
  //     print("a = $a ");
  //   case _:  //虽然只有一个下划线,但是依然可以接受(1,2),把1,2当做整体一个元组Record类型,类型描述是:  (int, int)
  //     print("其他情况");

    case var r:
      print("r = $r");
      print("r.runtimeType = ${r.runtimeType}");
  }
}
