import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home: Scaffold(
    appBar: AppBar(
    title: Text('appbarTitle'),
    ),body
  :
  MyApp()
  ),));
}

//StatelessWidget 无状态的小部件,之间在里面重写build就行了,不用像有状态的小部件StatefulWidget需要createState ,然在里面返回State的子类对象,再build
class MyApp2 extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Text("abc");
  }
  
}

class MyApp extends StatelessWidget {
  int i = 0;
  //  MyApp({super.key});
  MyApp({Key? key}):super(key: key);
//
  @override
  Widget build(BuildContext context) {
    return Row(
      children: <Widget>[
        ElevatedButton(onPressed: (){
          //这里没法使用setState
        print("${++i}");
        }, child: Text("$i")),
        Spacer(),
        Text("$i")

      ],
    );

  }
}
