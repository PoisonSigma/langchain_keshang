import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home:Row(children: [
      Text("7777"),//这里的不会被被热启动刷新,因为他不在build里面
      Spacer(),
      MyApp()
    ],)

    ));
}
class MyApp extends StatefulWidget {
  const MyApp({super.key});
  
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int i = 0;
  //热启动会刷新build方法里面的内容,不在build方法里面的内容不会被刷新
  //build方法会把里面的内容,一层一层的向上返回,并且描述到屏幕上
  @override
  Widget build(BuildContext context) {
    print("build执行了");
    return Row(children: [
      Text("${i}"),
      ElevatedButton(onPressed: (){
        print("按钮点击了${++i}");
        setState(() {
          print("abc");
        });
      }, child:Text("$i") )
    ],);
  }
}
