import 'package:flutter/material.dart';

/*

所有flutter代码都是放在lib目录中,默认入口文件是main.dart,也可以自己手动设置执行某个文件
runApp 把你传入的Widget小组件显示在屏幕上
runApp方法必须包含:import 'package:flutter/material.dart';
runApp方法只要一个参数:Widget翻译过来叫小部件,组件,控件,在flutter中,所有能显示出来的东西都是Widget的子类
因为Widget是抽象类abstract class,所以只能创建他的子类,例如Text



Text是一个文本框:参数data 是默认的参数,是必须填写的,直接用""传入,其他参数在{}中,是个命名可选参数列表,里面的参数必须有参数名字,因为没有required关键字所以可以传入也可以不传入
 */
// void main() {
//   runApp(Text(
//     "xxx",
//     textDirection:
//         TextDirection.ltr, //如果没有这个会报错,找不到方向性小组件No Directionality widget found.
//     style: TextStyle(color: Colors.red, fontSize: 40.0),
//   ));
// }

main() {
String str = "abc123";
  runApp( Text(
    //因为str不是常量,所以Text左边不能加const
    str,
    // "hello flutter=============================",
    textDirection: TextDirection.ltr,
    style: const TextStyle(
        // TextStyle 的构造函数也是常量构造函数,所以里面2个命名参数color和fontSize都是常量的时候,TextStyle 左边加const
        color: Colors.red,
        fontSize: 44), //color和 fontSize都是const的常量,所以外层也要加const
  ));
}
