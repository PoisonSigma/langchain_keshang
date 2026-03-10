// import导入的时候通过as给导入的库加一个前缀,解决跟其他库的方法重名冲突的问题
// 导入的时候 show关键字是 部分导入,只暴漏 show关键字后面的方法
// hide也是部分导入,隐藏hide关键字后面的方法,其他的都暴漏出来


import 'dart:math' as M1; //把导入的库用as起一个别名,然后调用的时候用别名.方法,就是调用这个库里面的方法
import '010b.dart';
import '057/057b.dart' as M2 show fun1,fun2;//把057b文件连的所有函数加一个 M2.前缀
//show关键字,让导入的文件,只暴漏出后面的函数,其他的不报楼
import '057/057b.dart' as M3 hide fun1,fun2;//把导入的库起一个M3的前缀,同时隐藏fun1和fun2,其他的暴漏

max(int a, int b){
   return a>b? a : b;
}
main(){
   var result  = M1.max(100, 101);
   print(result);

   M2.fun1();
   M2.fun2();
   M3.fun3();
   M3.fun4();

}