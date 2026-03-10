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
    // 默认情况下，占位符的大小适应其container。
    return Container(
      width: 100,
      height: 100,
      child:Placeholder()
    );

    // return Placeholder();//无限大
    /*
    return Row(
      children: <Widget>[
        Placeholder(  //在无限大的空间中,根据fallbackHeight fallbackWidth参数自动设置大小
          fallbackHeight: 100,//垂直方向父控件有高度约束屏幕那么高,所以不读取100
          fallbackWidth: 200,//因为row的主轴是水平方向,mainAxisSize = MainAxisSize.max,是无限大的 ,
          // 所以读取200
        )
      ],
    );

     */

    /*
    return  Container(
        width: 100,
        height: 100,
        // child: FlutterLogo());//他的尺寸可以更改

      child: Placeholder(),
    );

     */
  }
}
