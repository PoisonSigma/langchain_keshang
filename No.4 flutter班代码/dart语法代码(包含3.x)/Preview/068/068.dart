

import 'poisonLib.dart';

main(){
var p1 = P1();
p1.show();
test();//使用 模块p1.dart下的方法

  var p2 = P2();//使用模块p2.dart下的方法
  // var p3 = P3();//错误,p3.dart没有被引入到poisonLib库中,所以无法使用

  IOException;//当前文件如果没有包含 头文件,会报错,但是在poisonLib.dart库中, export导出了 头文件,所以不报错 export 'dart:io';
}