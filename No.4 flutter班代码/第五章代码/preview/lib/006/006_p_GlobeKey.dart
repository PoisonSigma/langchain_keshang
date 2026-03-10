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
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home: HomePage()));
}
class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  // 让 State 对象拥有 GlobalKey，以字段形式实例化它,这样可以让GlobalKey长期持有,而不是每次build都重新创建
   var key1 = GlobalKey();
   var key2 = GlobalKey();
   var key3 = GlobalKey();
  var list =<Widget> [
  ];
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    list = [
      Box(key:key1,a: 1),
      Box(key: key2,a: 1),
      Box(key: key3,a: 1),
    ];
  }
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
        appBar: AppBar(
          title: Text('appbarTitle'),
        ),
        body:  Column(
          children: list
        ),
      floatingActionButton: FloatingActionButton(onPressed: () {
        //currentWidget 通过全局key as转换 成 Widget
          Box box1 = key1.currentWidget as Box;
          box1.a+=10;

          //currentState 获取全局key对应的state
          _BoxState box1State = key1.currentState as _BoxState;
          box1State.b+=100;
          box1State.setState(() {

          });

      },
      child: Text("+1"),
      ),
    );

  }
}
class Box extends StatefulWidget {
  int a = 10;
   Box({required this.a, super.key});

  @override
  State<Box> createState() => _BoxState();
}

class _BoxState extends State<Box> {
  int b = 100;
  @override
  Widget build(BuildContext context) {
    print("_BoxState build");
    return Container(
      color: Colors.yellow,
      child: Row(
        children: <Widget>[
              Text("a= ${widget.a} b = $b"),
          ElevatedButton(onPressed: (){
            setState(() {
              widget.a++;
              b++;
            });

          }, child:Text("+1") )
        ],
      ),
    );
    
  }
}

