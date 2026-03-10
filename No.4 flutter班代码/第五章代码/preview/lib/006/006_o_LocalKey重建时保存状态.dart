/*

总结,要重绘的有状态小部件,build里嵌套一层自定义的有状态小部件.这种情况被嵌套的小部件的state子类里的成员变量,如果没有key,就无法保存
如果在有状态小部件里面的State子类 里面有成员变量,那么如果在build的时候,改变位置,插入,排序,等,成员变量无法保存
解构:排序和build的是外层的有状态小部件StatefulWidget,需要保存的是内层嵌套的自定义的StatefulWidget,只有一层,没有这种问题.
ValueKey需要手动设置里面的字符串,要求不能重复,否则编译报错
UniqueKey系统自动设置不重复的key
一般用在购物车改变商品顺序用
 */

/*
键keys用于控制在部件（widgets）重建时，框架渲染控件需要考虑3个条件:1.运行时类型,2出现顺序,3keys
没有keys时候,重建rebuild时考虑2个因素:1.runtimeType 运行时类型.2出现顺序
有keys键的时候,需要增加一个条件,就是keys
键的作用,当在rebuild的时候,如果有多个相同的想通类型的widget对象,那么要用到keys,
要不然框架无法区分,是哪个对象
如果没有keys,那么重建以后当前绘制的相同类型的对象顺序永远和之前一样,因为框架只考虑出现顺序和类型
总结,有状态的小部件StatefulWidget里面的State子类状态,在build的时候如果没有key,就不会保存状态,
改变了位置,那么成员变量会变成第一次渲染的值
在一个位置,每次插入,里面状态,都是第一次渲染这个位置的状态,例如插入第0个位置,发现里面的成员变量是之前的值
如果build的小部件顺序没变,那么状态也不会被刷新,成员变量不变
里面的成员变量不会被保存.Widget部分的成员变量会被保存
有状态小部件,里面的没有State子类,里面成员变量可以正确保存


 */
import 'package:flutter/material.dart';

main() {
  runApp(
    MaterialApp(home: HomePage()),
  );
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  var list = [
    //Box1和Box2都是有状态的,所以他的State子类中的成员变量不会被记录,
    // Widget子类的成员变量会被记录
    Box1(color: Colors.red, num: 1),
    Box1(color: Colors.red, num: 2),
    Box2(color: Colors.blue, num: 2),
    Box2( key:Key("1"), color: Colors.blue, num: 3),
    Box2( key:ValueKey("2"), color: Colors.blue, num: 3),
    Box2( key:UniqueKey(), color: Colors.blue, num: 3),

    Box3(color: Colors.pink, num:4 ),//Box3是 无状态的,他没有State子类,不需要记录状态
  ];
  var listAll;
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    for(var item in list){
      print("item.runtimeType= ${item.runtimeType}");

    }

  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('标题栏'),
        ),
        body: Column(children:
        list
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {

            setState(() {
              list.shuffle();
              // list.insert(0,Box2(color: Colors.green, num: 100));//每次插入,里面状态,都是第一次渲染这个位置的状态
              print(list);
            });
          },
          child: Icon(Icons.refresh),
        ));
  }
}

class Box1 extends StatefulWidget {
  final Color color;
  int num;

  Box1({ required this.color, required this.num});
  // Box1({super.key, required this.color, required this.num});

  @override
  State<Box1> createState() => _Box1State();
}

class _Box1State extends State<Box1> {
  //没有key,State里的成员变量不能被正确保存,重回几次以后如果改变了位置,这个成员变量变成最开始的值99
  int state_i = 99;
  @override
  Widget build(BuildContext context) {
    return Container(
      color: widget.color,
      height: 100,
      child: Row(
        children: <Widget>[
          Text("box1没有key  widget.num=${widget.num}"),
          Text("  state_i=${state_i}"),
          ElevatedButton(onPressed: () {
            setState(() {
              widget.num++;
              state_i++;
            });
          }, child:Text("+1"),)
        ],
      ),
    );
  }
}



class Box2 extends StatefulWidget {
  final Color color;
  int num;

  // Box2({ required this.color, required this.num});
  Box2({super.key, required this.color, required this.num});

  @override
  State<Box2> createState() => _Box2State();
}

class _Box2State extends State<Box2> {
  //没有key,State里的成员变量不能被正确保存
  int state_i  = 100;
  @override
  Widget build(BuildContext context) {
    return Container(
      color: widget.color,
      width: 500,
      height: 100,
      child: Row(
        children: <Widget>[
          Text("box2有key  widget.num=${widget.num}"),
          Text("state_i=${state_i}"),
          ElevatedButton(onPressed: () {
            setState(() {
              widget.num++;
              state_i++;
            });
          }, child:Text("+1"),)
        ],
      ),
    );
  }
}

class Box3 extends StatelessWidget {
  //无状态小部件,里面的成员成员变量都不会改变,会正确保存
  final Color color;
  final int num;
  Box3({super.key, required this.color, required this.num});

  @override
  Widget build(BuildContext context) {
    return  Container(
      color: color,
      width: 500,
      height: 100,
      child: Row(
        children: <Widget>[
          Text("Box3是无状态的 num=${num}"),


        ],
      ),
    );
  }
}

