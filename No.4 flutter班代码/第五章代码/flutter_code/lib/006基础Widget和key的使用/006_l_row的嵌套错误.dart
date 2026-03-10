/*
RenderFlex children have non-zero flex but incoming width constraints are unbounded.
渲染flex子项拥有一个非零的flex,但是传入的宽度约束是无边界的
 */

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body: const HomePage())));
}
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    /*
    return Container(
      color: Colors.green,
      child: Row(
        
        children: <Widget>[
          Text("000"),
          Expanded(//解决方法1:用Expanded,计算外层剩余的高度,传给内层
            child: Container(
              color: Colors.yellow,
              // width: 300,//解决方法2,设置尺寸
              child: Row(
                children: <Widget>[
                  Text("111"),
                  Text("222"),
                  Expanded(child: Container(
                      color: Colors.red,
                      child: Text("3333")))
                ],
              ),
            ),
          ),
        ],
      ),
    );
     */
    return Container(
      color: Colors.green,
      child: ListView(
        // scrollDirection: Axis.vertical,//默认垂直滚动
        scrollDirection: Axis.horizontal,//水平滚动
        children: [
          Text("111"),
          Text("222"),
          Container(
            width:300 ,
            color: Colors.yellow,
            child: Row(
              children: <Widget>[
                Text("333"),
                Text("444"),
                Expanded(child: Text("555"),)
              ],
            ),
          ),
        ],
      ),
    );
  }
}