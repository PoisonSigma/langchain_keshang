import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  int i = 0;
  runApp(MaterialApp(
    home: Scaffold(
        appBar: AppBar(
          // leading: Icon(Icons.arrow_back),//导航栏左边,如果这个页面是被弹出的,则会插入一个 BackButton后退按钮,通过 automaticallyImplyLeading: false 关闭这个功能
          // automaticallyImplyLeading: false,//用来关闭上面的功能
          title: Text("标题栏"),
          //AppBar 里面的actions是导航栏右边的一组小控件,是 List<Widget>?
          actions: [Text("右边第1个"), Text("右边第2个"), Icon(Icons.add)],
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            print("点击了按钮 i = ${++i}");
          },
          tooltip: "长按描述abc", //长按按钮时候的描述文字
          child: Icon(Icons.add),
        ),
        body: Row(
          //行 水平排列里面的子组件
          // mainAxisAlignment: MainAxisAlignment.center, //这个是居中
          // mainAxisAlignment:MainAxisAlignment.start, //start 左对齐
          mainAxisAlignment: MainAxisAlignment.end, //end 左对齐
          children: [
            //  Widget数组,里面放水平排列的子组件

            Text("i = $i"), //这里不能刷新页面,需要后续学习 有状态的Widget
            Text(' '),
            //GestureDetector小部件没有视觉表示，而是检测用户进行的手势。
            // 当用户点击child时，GestureDetector调用其onTap()回调函数

            GestureDetector(
              onTap: () {
                print("onTap点击了");
              },
              child: Text("这里通过手势点击"),
            ),
            Text("abc"),

            Text('end'),
            //Button类的有很多,这节课先讲一个最简单的文本按钮
            TextButton(
                //文本按钮没有可见的边框,根据内容调整大小
                onLongPress: () {
                  print("长按1");
                },
                onPressed: () {
                  //点击事件
                  print("点击了按钮1");
                  print("${++i}");
                },
                child: Icon(Icons.home)),

            TextButton(
              //一个按钮
              onPressed: () {
                print("点击了按钮2");
                print("${++i}");
              },
              onLongPress: () {
                print("长按按钮2");
              },
              child: Text('点我123123213'),
            )
          ],
        )),
  ));
}
