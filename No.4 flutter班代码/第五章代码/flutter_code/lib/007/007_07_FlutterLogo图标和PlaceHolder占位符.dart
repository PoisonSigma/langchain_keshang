//     一个绘制一个方框的小部件，代表着其他小部件将来可能添加的位置。
// 在开发过程中，此小部件非常有用，可以指示界面尚未完全完成。
// 默认情况下，占位符的大小适应其container。
// 如果占位符位于一个无界空间中，或者某个维度是无限大 它将根据给定的 fallbackWidth 和 fallbackHeight 调整大小。
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
    body给了占位符限制约束,所以不是无限大,fallbackWidth设置 无效
    return  Placeholder(
      fallbackWidth: 100,
      fallbackHeight: 100,
    );
     */
/*
    // 默认情况下，占位符的大小适应其container。
    return Container(
      width: 200,
      height: 200,
      child: Placeholder(
        fallbackHeight: 100,
        fallbackWidth:50,
      )
    );
*/
    /*
  // 如果占位符位于一个无界空间中，或者某个维度是无限大 它将根据给定的 fallbackWidth 和 fallbackHeight 调整大小。
  return Row(
    children: <Widget>[
      Placeholder(
        fallbackWidth: 100,
        fallbackHeight: 100,
      )
    ],
  );


   */
    return Container(
        width: 600,
        height: 600,
        child: FlutterLogo());
  }
}
