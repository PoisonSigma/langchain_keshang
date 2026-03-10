//通过children []数组设置每一个 ListView元素，特点是运行的时候 children 里面的代码全部运行一遍
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
    return  Container(
      // color: Colors.green,
      child: ListView(
          // scrollDirection:Axis.vertical,//默认垂直滚动
        // scrollDirection: Axis.horizontal,//滚动方向水平
        children: [
          Text("ab"),
          Container(
            color: Colors.yellow[900],
              child: Text("111")),
          Divider(
            // height: 20,
          color: Colors.black12, //黑色数字越小越淡
          //   color: Colors.black[100],//黑色没有[]
          ),
          Container(
              color: Colors.red,
              child: Text("ab")),
          Container(
            child: Icon(Icons.home),
          ),
          FlutterLogo()
        ],
      ),
    );
  }
}
