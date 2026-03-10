/*
这个例子演示列column的主轴和交叉轴尺寸规则
 */
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
    return Container(
      height: 300,
      color: Colors.green,
      child: Column(
        // mainAxisSize: MainAxisSize.max,
        mainAxisSize: MainAxisSize.min,

        children: <Widget>[
          Text("abc"),
          Container(
            width: 100,
            height: 100,
            color: Colors.yellow,
          ),
          Container(
            width: 150,
            height: 100,
            color: Colors.red,
          ),
          Expanded(
            child: Container(
              width: 100,
              height: 100,
              color: Colors.blue,
            ),
          )
        ],
      ),
    );
  }
}
