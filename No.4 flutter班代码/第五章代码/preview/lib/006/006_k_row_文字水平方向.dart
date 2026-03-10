import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: Text('appbarTitle'),
          ),
          body: HomePage())));
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {

    // textDirection 属性控制着 Row 中子控件的渲染方向。TextDirection.ltr 是 Row 子控件的默认文本方向 ,从左到右
    // TextDirection.rtl 是从右到左
    return Row(
      // textDirection: TextDirection.rtl, // 设置为从右到左的文本方向
      textDirection: TextDirection.ltr, // 设置为从右到左的文本方向
      children: <Widget>[
        // 在从右到左的布局中，这些子控件将从右到左进行排列
        Text("111 222 333 444 555"),
        Icon(Icons.sunny),
        FlutterLogo(),
      ],
    );



  }
}
