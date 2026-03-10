//父控件通过全局key获取子控件的成员和方法
/*
GlobalKey 在整个应用程序中是唯一的，用于唯一地标识元素
让 State 对象拥有 GlobalKey，并在 State.initState 之外的地方（如 State 类的字段）实例化它。
GlobalKey 不应在每次build时重新创建。它们应该是长生命周期的对象，通常由 State 对象拥有。
        currentWidget 通过全局key as转换 成 Widget
          Box box1 = key1.currentWidget as Box;
          box1.a+=10;

          currentState 获取全局key as 转换 获取 对应的state
          _BoxState box1State = key1.currentState as _BoxState;
 */
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(home: HomePage()));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  // List<Widget> list = [];
  var list = <Widget>[];
  var key1 = GlobalKey();
  var key2 = GlobalKey();
  var key3 = GlobalKey();
  // late GlobalKey key1;
  // late GlobalKey key2;
  // late GlobalKey key3;

  @override
  void initState() {
    // TODO: implement initState
    //并在 State.initState 之外的地方（如 State 类的字段）实例化它。
    super.initState();
    // key1 = GlobalKey();
    // key2 = GlobalKey();
    // key3 = GlobalKey();
    list = <Widget>[
      Box(key: key1),
      // Box(key: key1,),//2个widget给了一个key,会报错
      Box(key: key2),
      Box(key: key3),
    ];
  }



  @override
  Widget build(BuildContext context) {

    print("父控件build");

    return Scaffold(
      appBar: AppBar(
        title: Text('appbarTitle'),
      ),
      body: Container(
        color: Colors.green,
        child: Column(
          children: list,
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          //   currentWidget 通过全局key as转换 成 Widget

          setState(() {
            var box1 = key1.currentWidget as Box;
            box1.a += 100;
            var box1State = key1.currentState as _BoxState;
            box1State.b += 1000;
            print(box1.hashCode);
            print(box1State.hashCode);
            print("setState");
            //刷新子控件
            box1State.setState(() { //让子控件刷新,并且访问widget和state的正确方式
              print(box1.hashCode);
              print(box1State.hashCode);
            });
          });

        },
        child: Icon(Icons.refresh),
      ),
    );
  }
}

class Box extends StatefulWidget {
  int a = 0;

  Box({super.key});

  @override
  State<Box> createState() => _BoxState();
}

class _BoxState extends State<Box> {
  int b = 0;

  @override
  Widget build(BuildContext context) {
    print("_BoxState build");
    return Container(
      color: Colors.yellow,
      child: Row(
        children: <Widget>[
          Text("widget.a = ${widget.a}  b = $b "),
        ],
      ),
    );
  }
}
