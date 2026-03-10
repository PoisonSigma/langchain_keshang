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
    return Column(
      // textDirection: TextDirection.rtl, //文字方向只能修改水平方向的文字方向,垂直排列的column不起作用
      // verticalDirection: VerticalDirection.down,//默认向下排列
      verticalDirection: VerticalDirection.up,//向上排列
      children: <Widget>[
        Text("123"),
        Text("abc"),
        FlutterLogo()

      ],
    );
  }
}