/*
这个例子演示 参数 itemExtentBuilder:itemExtentBuilder,  //可以单独设置某个元素高度
 */

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';

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
    return Container(
        color: Colors.green,
        child: ListView.builder(
            // itemExtentBuilder:(int index, SliverLayoutDimensions dimensions){
            itemExtentBuilder:(int index, _){
                return 10.0 * index;
            },
            itemCount: 10, //子元素的个数,不传就是无限大
            itemBuilder: //里面返回的是每个子元素要显示的内容
                (context, index) {
              return   Text("$index");
            })
    );
  }
}
