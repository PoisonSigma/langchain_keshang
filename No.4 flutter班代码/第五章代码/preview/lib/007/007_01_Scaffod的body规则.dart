/*
内容显示在 appBar 的下方，位于环境 MediaQuery 的 MediaQueryData.viewInsets 底部的上方，
在 floatingActionButton后方。
 在drawer 的后方,点击左上角后,弹出会挡住body。
 如果 resizeToAvoidBottomInset 设置为 false，那么当屏幕键盘出现时，body 的大小不会调整，
 即不会被 viewInsets.bottom 缩进。
Scaffold 的 body 中的部件会定位在 app bar 和 Scaffold 底部之间的可用空间的左上角。
居中显示，可以考虑将其放入 Center 部件中，
并让 Center 成为 body。如果你想让部件扩展以填充可用空间，
如果有column列放在body里,可能会溢出,改成用ListView可以自动滚动,不会溢出
 */

import 'package:flutter/material.dart';
main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          // resizeToAvoidBottomInset:false,//设置这个值,那么键盘弹起以后body尺寸不会缩小
          body:  HomePage(),
        //浮动按钮会始终在body的底部
        floatingActionButton: FloatingActionButton(onPressed: () {

        },),
        drawer: Container(  //点击左上角,弹出drawer后 body在drawer的后方
          color: Colors.yellow,

        ),
      )
  )

  );
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var tc1 = TextEditingController();//建立一个控制器,作用是绑定第一个TextField,通过这个控制器设置和获取文本text
  @override
  void initState() {
    // TODO: implement initState
    super.initState();

  }
  @override
  Widget build(BuildContext context) {

    /*
    //body中的控件默认在左上角
     return  Text("abc");
     */
//下面证明当body中的子控件有自己的尺寸的时候,body取子控件的尺寸,并且左上角对其
    return Container(
        width: 100,
        height: 100,
        color: Colors.yellow,
        child: Text("111"));
/*
    //下面代码证明body在appBar和键盘之间
    return  Container(
      height: 900,//设置尺寸足够大,但是无法超越父控件body对子控件的约束,所以还是在屏幕内
      color: Colors.green,
      alignment: Alignment.bottomCenter,//设置在底部居中
      child: TextField(
        controller: tc1,
        decoration: const InputDecoration(hintText: "请输入内容"),
        onChanged: (str){//当键盘改变
          print("str=$str");
          print("tc1.text=${tc1.text}");
        },
      ),
    );
 */


    // 居中显示，可以考虑将其放入 Center 部件中，
    // 并让 Center 成为 body。如果你想让部件扩展以填充可用空间，
    return Container(
      child: Center(//后面讲解
          child:Text("abc")),
    );




  }

}

