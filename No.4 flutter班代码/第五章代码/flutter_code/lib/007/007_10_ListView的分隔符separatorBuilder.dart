//ListView.separated的特点是,可以 通过builder设置每个元素,又可以通过separatorBuilder设置每个分隔符,例如Divider()

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
    var list = ["abc","bcd","efg"];
    var colorNum = [100,200,300];
    return  ListView.separated(itemBuilder:  (context, index) {
      // Text("$index");//注意这里一定要返回widget,不返回不会提示错误,但是什么子元素都不显示
      /*
        return Container(
           color: Colors.yellow,
             margin: EdgeInsets.all(10),//可以看到背景,不会渲染外边距
             // padding: EdgeInsets.all(10),//渲染部分不会漏出背景
             child: Text("$index"));
      }
         */
      return   Container(
        alignment: Alignment.center,
          color: Colors.yellow[colorNum[index]],
          child: Text("${list[index]}"));

    }, separatorBuilder: (BuildContext context, int index){
      //返回的是分隔符要显示的widget
      return Divider(
        height: 40,
        color: Colors.green[500],
      );
    }, itemCount: list.length);
  }
}