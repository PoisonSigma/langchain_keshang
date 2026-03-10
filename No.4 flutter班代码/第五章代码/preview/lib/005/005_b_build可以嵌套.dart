
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home: Widget1(),)); //runApp把home参数里面的Widget画到屏幕上
}
//build可以嵌套,把return的Widget一层层,向上返回
class Widget1 extends StatelessWidget {   //MyApp这个Widget把build里面返回的widget画在屏幕上
  const Widget1({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[

        Text("000"),
        Text("111"),
        Widget2()], //这里Widget2对象把build里面返回的Widget作为Widget使用,返回给上一层,所以上一层的row,就变成了 111 spacer 222
    );


  }
}
class Widget2 extends StatelessWidget {
  const Widget2({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text("222"),
        Widget3()
      ],
    );
  }
}
class Widget3 extends StatelessWidget {
  const Widget3({super.key});

  @override
  Widget build(BuildContext context) {
    return Text("333");
  }
}


