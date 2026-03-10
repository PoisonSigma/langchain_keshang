
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(
        home:Widget1(key:Key("abc")
        ) ));//带参数key的
  // runApp(const MaterialApp(home:Widget1() ));
}
/*
class Widget1 extends StatelessWidget{
  // const Widget1({ super.key });//简写
  const Widget1({Key? key}):super(key: key);//初始化列表的语法方法
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Text("000");
  }

}
 */
//直接输入stl快捷键
class Widget1 extends StatelessWidget {
  int i = 0;
  Widget1({super.key});
//StatelessWidget 无状态的小部件,之间在里面重写build就行了,不用像有状态的小部件StatefulWidget需要createState ,
// 然在里面返回State的子类对象,再build
  @override
  Widget build(BuildContext context) {
    print("build执行");
    return Column(
      children: [
        Text("000"),
        Text("111"),
        ElevatedButton(onPressed: (){
        print("${++i}");
        }, child:Text("$i") )
      ],
    );
  }
}
