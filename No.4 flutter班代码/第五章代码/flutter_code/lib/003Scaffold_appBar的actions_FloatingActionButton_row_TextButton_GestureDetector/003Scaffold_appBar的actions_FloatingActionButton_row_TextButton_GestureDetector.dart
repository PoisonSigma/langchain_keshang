import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    int i = 0;
    runApp(
        MaterialApp(home: Scaffold(
      appBar:  AppBar(
        // leading: Icon(Icons.arrow_back),//导航栏左边,如果这个页面是被弹出的,则会插入一个 BackButton后退按钮,通过 automaticallyImplyLeading: false 关闭这个功能
        // automaticallyImplyLeading: false,//用来关闭上面的功能
        leading: const Text("后退"),
        title: const Text('abc'),
        //AppBar 里面的actions是导航栏右边的一组小控件,是 List<Widget>?
        actions: const [
          Text('111'),
          Text('222'),
          Icon(Icons.add)
        ],
      ),
      floatingActionButton: FloatingActionButton(onPressed: () {
        print("floatingActionButton点击了");
      },
        tooltip:"长按了floatingActionButton",
          // child:Icon(Icons.add)
        child: const Text('点击'),
      ),
      body: Row(
        children: [
          Text('i=$i'),
          Spacer(),//占位间隔,这节课先不用,否则一行装不下
          Text('222'),
          Spacer(),
          Text('333'),

          //文本按钮没有可见的边框,根据内容调整大小
          TextButton(
              onLongPress: (){
                print("长按");
              },
              onPressed: () {
            print("TextButton点击");
          }, child: Text("点我123456")),
          TextButton(
              onLongPress: (){
                print("长按");
              },
              onPressed: () {
            print("TextButton点击");
          }, child: Icon(Icons.home)),

          //GestureDetector小部件没有视觉表示，而是检测用户进行的手势。
          // 当用户点击child时，GestureDetector调用其onTap()回调函数
          GestureDetector(
            onLongPress: (){
              print("长按");
            },
            onTap:(){
              print("手势点击i=${++i}");

          },
          child:Text('手势点我'),

          )

      ],

      ) ,
    )
    )
    );
}
