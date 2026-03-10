/*
MaterialApp 是主题,自带方向设置,所以他里面的包含的widget都不需要设置方向
home 参数里面放一个 widget,用来显示,第一个例子放了一个文本框Text,并且没有写方向参数
 */



import 'package:flutter/material.dart';//为了使用MaterialApp

void main() {
  runApp(const MaterialApp(
    home://home这里可以放一个Widget,直接渲染到屏幕上,可以理解为,你画一个控件到屏幕上
      Text(
        "xxx1234",
        // textDirection: TextDirection.ltr,//在MaterialApp的home里面,所有的Widget都不需要填写方向
        style: TextStyle(color: Colors.red, fontSize: 40.0),
      )

  )
  );
}


