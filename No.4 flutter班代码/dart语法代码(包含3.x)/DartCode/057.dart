// import导入的时候通过as给导入的库加一个前缀,解决跟其他库的方法重名冲突的问题
// 导入的时候 show关键字是 部分导入,只暴漏 show关键字后面的方法
// hide也是部分导入,隐藏hide关键字后面的方法,其他的都暴漏出来
import 'dart:math' as M1;

import '057/057b.dart' as M2 show fun1, fun2;
import '057/057b.dart' as M3 hide fun3;

max(a, b) {
  print("自定义方法max执行");
  return a > b ? a : b;
}

main() {
  // var result = max(100, 50);
  // print(result);
  M2.fun1();
  M2.fun2();
  // M2.fun3();//没有暴漏在外面的fun3,会报错,找不到
  M3.fun4();
  // M3.fun3();//hide隐藏了fun3,所以找不到
}
