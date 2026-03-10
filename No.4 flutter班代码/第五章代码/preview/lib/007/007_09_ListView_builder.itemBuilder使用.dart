import 'package:flutter/material.dart';
main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body:  HomePage())));
}
class HomePage extends StatelessWidget {
  HomePage({super.key});
  var list = ["a","b","c"];
  @override
  Widget build(BuildContext context) {
    return  Container(
      color: Colors.green,
      child: ListView.builder(
          // itemCount: 10,//子元素个数
          itemCount: list.length,
          itemBuilder: (context,index){
            //注意这里一定要返回widget,不返回不会提示错误,但是什么子元素都不显示
            return Container(
              height: 30,
                color: Colors.yellow,
                alignment: Alignment.center,
                margin: EdgeInsets.fromLTRB(20, 0, 20, 5),//这里加padding不会改变当前container的渲染背景
                padding: EdgeInsets.all(5),
                // child: Text("$index")
child: Text("${list[index]}"),
            );
      }),
    );
  }
}