/*
自己总结:
总结,要重绘的有状态小部件,build里嵌套一层自定义的有状态小部件.这种情况被嵌套的小部件的state子类里的成员变量,如果没有key,就无法保存
如果在有状态小部件里面的State子类 里面有成员变量,那么如果在build的时候,改变位置,插入,排序,等,成员变量无法保存
解构:排序和build的是外层的有状态小部件StatefulWidget,需要保存的是内层嵌套的自定义的StatefulWidget,只有一层,没有这种问题.
ValueKey需要手动设置里面的字符串,要求不能重复,否则编译报错
UniqueKey系统自动设置不重复的key
一般用在购物车改变商品顺序用
 */
/*
官方解释
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
  runApp(const MaterialApp(home: HomePage()));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var list = <Widget>[
  // ValueKey需要手动设置里面的字符串,要求不能重复,否则编译报错
  // UniqueKey系统自动设置不重复的key
  //   Box1(key: Key("1"),  i: 100,color: Colors.yellow,),
    Box1(key: GlobalKey(),  i: 100,color: Colors.yellow,),
      // Box1(  i: 100,color: Colors.yellow,),
    // ValueKey("1") 是 Key重定向到ValueKey
    // Box1(key:UniqueKey(),  i: 100,color: Colors.red,),
    Box1(  i: 100,color: Colors.red,),
    // Box1(key: Key("1"), i: 100,color: Colors.blue,)//报错,重定义keys
    Box1(key: Key("2"),  i: 100,color: Colors.blue,),
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('标题栏'),
      ),
      body: Column(
        children: list,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {});
          list.shuffle();//给队列随机改变顺序
          // list.add(Box1(i: 50, color: Colors.black12));//添加出现在新位置上不会出错
          // list.insert(0, Box1(i: 50, color: Colors.black12));
        },
        child: const Icon(Icons.refresh),
      ),
    );
  }
}
class Box1 extends StatefulWidget {
  Box1({super.key,required this.i,required this.color});
  int i = 1;
  Color color;
  @override
  State<Box1> createState() => _Box1State();
}

class _Box1State extends State<Box1> {

  int i = 1000;
  @override
  Widget build(BuildContext context) {
    print("Box1 build");
    return Container(
      height: 100,
      color: widget.color,
      child: Row(
        children: <Widget>[
          Text("widget.i=${widget.i}  state.i = $i}"),
          ElevatedButton(onPressed: (){
          setState(() {
            widget.i++;
            i++;
          });
          }, child: Text("+1"),)
        ],
      ),
    );

  }
}

