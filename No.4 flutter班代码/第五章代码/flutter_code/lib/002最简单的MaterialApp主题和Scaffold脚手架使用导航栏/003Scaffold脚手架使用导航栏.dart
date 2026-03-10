/*
Scaffold 脚手架,
第3个例子为了MaterialApp主题里面带导航栏和背景
参数appBar ,需要用AppBar()来创建,里面的leading(最左侧)和title(中间位置)可以用Widget,例如这里用的是一个文本框Text,和 一个 图标Icon
注意使用 系统的图标要在 pubspec.yaml 文件里配置:  uses-material-design: true
 */

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home: Scaffold(
      appBar: AppBar(
          // leading: Text("左侧"),
        leading: Icon(Icons.menu),
          // 注意使用 系统的图标要在 pubspec.yaml 文件里配置:  uses-material-design: true
        title:  Icon(Icons.add),
        // Text("导航栏标题"),

      ),
      body:const Center(child: Text("内容123"))
    ),));
}