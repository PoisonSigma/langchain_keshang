/*
RenderFlex children have non-zero flex but incoming width constraints are unbounded.
渲染flex子项拥有一个非零的flex,但是传入的宽度约束是无边界的
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
    /*
    return Container(
      color: Colors.green,
      child: Row(
        children: <Widget>[
          Container(
            width: 200,//解决错误方法就是给内层的row加一个宽度约束,或者加Expanded
            color: Colors.yellow,
            child: Row(
              children: <Widget>[
                Text("111"),
                Text("222"),
                Expanded(child: Text("333"))
              ],
            ),
          ),


        ],
      ),
    );
    */
    return Container(
      color: Colors.green,
      child: ListView(

        // scrollDirection: Axis.vertical,//默认滚动方向垂直
        scrollDirection: Axis.horizontal,//水平滚动

        children: [
      Text("111="),
          Text("222="),
          Container(
            width: 300,//解决方法给内层的row设置确定的宽度来让Expanded分配剩余宽度
            color: Colors.yellow,
            child: Row(
              // crossAxisAlignment: CrossAxisAlignment.start,//默认交叉轴是居中的
              children: <Widget>[
                Text("333="),
                Text("444="),
                Expanded(child: Text("555"),)
              ],
            ),
          ),
        ],
      ),
    );
  }
}