import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
/*

所有flutter代码都是放在lib目录中,默认入口文件是main.dart,也可以自己手动设置执行某个文件
runApp 把你传入的Widget小组件显示在屏幕上
runApp方法必须包含:import 'package:flutter/material.dart';
runApp方法只要一个参数:Widget翻译过来叫小部件,组件,控件,在flutter中,所有能显示出来的东西都是Widget的子类
因为Widget是抽象类abstract class,所以只能创建他的子类,例如Text



Text是一个文本框:参数data 是默认的参数,是必须填写的,直接用""传入,其他参数在{}中,是个命名可选参数列表,里面的参数必须有参数名字,因为没有required关键字所以可以传入也可以不传入
 */
main(){
    runApp(Text("hello flutter",
        textDirection: TextDirection.ltr,
        style: TextStyle(fontSize: 88,color: Colors.white),
    ));
}

class A{
    String a;
    int b;

    A(this.a, this.b);
    A.init(this.a, this.b);
}