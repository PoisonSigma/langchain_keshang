import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
/*
Scaffold 脚手架,
第3个例子为了MaterialApp主题里面带导航栏和背景
参数appBar ,需要用AppBar()来创建,里面的leading(最左侧)和title(中间位置)可以用Widget,例如这里用的是一个文本框Text,和 一个 图标Icon
注意使用 系统的图标要在 pubspec.yaml 文件里配置:  uses-material-design: true
 */
main(){
    runApp(MaterialApp(
      home: Scaffold(
          appBar:AppBar(
            leading: Icon(Icons.home), //导航栏最左侧的位置

title: Text("abc标题栏123"),
//           title: Icon(Icons.home),//这里演示AppBar 的title可以使用 Icon图标

            // title: Icon(Icons.menu),//这里演示AppBar 的title可以使用 Icon图标
          ),
          body:Text("这里是内容")
      ),
    ));
}

