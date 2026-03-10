/*
Scaffoldbody部分 内容显示在 appBar 的下方，位于环境 MediaQuery 的 MediaQueryData.viewInsets 底部的上方，
在 floatingActionButton后方。
 在drawer 的后方,点击左上角后,弹出会挡住body。
 如果 resizeToAvoidBottomInset 设置为 false，那么当屏幕键盘出现时，body 的大小不会调整，
 即不会被 viewInsets.bottom 缩进。
Scaffold 的 body 中的部件会定位在 app bar 和 Scaffold 底部之间的可用空间的左上角。
居中显示，可以考虑将其放入 Center 部件中，
并让 Center 成为 body。如果你想让部件扩展以填充可用空间，
如果有column列放在body里,可能会溢出,改成用ListView可以自动滚动,不会溢出

//下面证明当body中的子控件有自己的尺寸的时候,body取子控件的尺寸,作用像是没有尺寸的container 设置了左上角对其
 */

import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
    appBar: AppBar(
      title: const Text('标题栏'),
    ),
    body: const HomePage(),
    drawer: Container(
      //点击左上角,弹出drawer后 body在drawer的后方
      // width: 300,
      color: Colors.yellow,
      // child:Text("abc"),
    ),
    floatingActionButton: FloatingActionButton(
      onPressed: () {},
    ),
// resizeToAvoidBottomInset: false,//设置这个值,那么键盘弹起以后body尺寸不会缩小
  )));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var tc1 = TextEditingController();

  @override
  Widget build(BuildContext context) {
    /*
    return Container(
      width: 1000,//证明body约束内部的子控件的尺寸
    height: 1000,
    color: Colors.green,
      //Scaffold 的 body 中的部件会定位在 app bar 和 Scaffold 底部之间的可用空间的左上角。
      alignment: Alignment.bottomCenter,
      child: TextField(
        controller:tc1 ,
        onChanged: (str){
            print("str = $str");
            print("tc1.text = ${tc1.text}");
        },
        decoration: InputDecoration(hintText: "占位字符 请输入文字"),
      ),
    );
*/

    /*
    //居中显示，可以考虑将其放入 Center 部件中，
    return Center(child: Text("abc"));
    */


    //下面证明当body中的子控件有自己的尺寸的时候,body取子控件的尺寸,并且左上角对其
    return Container(
      width: 100,
        height:100 ,
        color: Colors.yellow,
        child: Text("1111")
    );
  }


}
