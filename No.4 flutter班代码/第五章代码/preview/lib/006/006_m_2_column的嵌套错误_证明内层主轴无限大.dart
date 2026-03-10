import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
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
    return  Column(
      children: [
        Container(//这个container高度已经超出屏幕大小还能放下,只是会报错,证明外层的Column的主轴方向,可以容纳无限大,但是会报错
          color: Colors.yellow,
          height: 2000,
          //这个container没有child,所以尺寸会撑到最大,因为有height设置,会默认宽度最大
        ),
        //既然上面的Container可以是无限大那么内层这个Column,的mainAxisSize会占用父级给内层的约束,无限大,那么内层Column的高度就是无限大
        Column(
          mainAxisSize: MainAxisSize.max,//默认值是最大
          children: <Widget>[

          ],
        ),
      ],
    );
  }
}