import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
  //runApp把home参数里面的Widget画到屏幕上
    runApp(MaterialApp(home: Widget1()));
}
class Widget1 extends StatelessWidget {
  const Widget1({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Text("000"),
        Text("111"),
        Widget2(),
      ],
    );

  }
}
class Widget2 extends StatelessWidget {
  const Widget2({super.key});

  @override
  Widget build(BuildContext context) {

    //这里Widget2对象把build里面返回的Widget作为Widget使用,
    // 返回给上一层,所以上一层的row,就变成了 111 spacer 222
    return Column(
      children: [
        Text("222"),
        Widget3()
      ],
    );
  }
}
class Widget3 extends StatefulWidget {
  const Widget3({super.key});
  @override
  State<Widget3> createState() => _Widget3State();
}
//build可以嵌套,把return的Widget一层层,向上返回
class _Widget3State extends State<Widget3> {
  int i = 0;
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[Text("333"),ElevatedButton(onPressed: (){
      print("${++i}");
      setState(() {
      });
      }, child: Text("$i")
      )
      ]
    );
  }
}


