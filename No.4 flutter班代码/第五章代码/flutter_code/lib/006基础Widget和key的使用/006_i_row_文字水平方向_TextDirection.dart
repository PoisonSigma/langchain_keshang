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
    return Row(
      // textDirection 属性控制着 Row 中子控件的渲染方向。TextDirection.ltr 是 Row 子控件的默认文本方向 ,从左到右
      // textDirection: TextDirection.ltr,//默认从左到右
      textDirection: TextDirection.rtl, // 设置为从右到左的文本方向
      children: <Widget>[
        FlutterLogo(),
        Text("abc bcd cde"),
        Text("123"),
        Icon(Icons.sunny)
      ],
    );
  }
}