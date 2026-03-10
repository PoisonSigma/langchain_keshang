// mainAxisAlignment，主轴对齐 跟row和column元素的排列方向是同一个方向
// crossAxisAlignment   交叉轴对齐 跟row或者column垂直的方向
//对齐小部件Aligning widgets
//Row和Column 子元素元素的排列方式
//下面2个排列方式一个是平行一个是垂直
//mainAxisAlignment，主轴对齐 跟row和column元素的排列方向是同一个方向
//crossAxisAlignment   交叉轴对齐 跟row或者column垂直的方向
//这2个参数是枚举类型提供了各种常量来控制对齐方式
//注意:有时候居中不了,是因为row或者column会根据里面的元素来设置最大宽度和高度
//如果最大宽度或者高度不是整个屏幕大小,那么居中以后也会跟着尺寸变小以后偏左或者偏上
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

/*
响应小部件生命周期事件
在 StatefulWidget 上调用 createState() 后，框架会将新的状态对象插入到树中，然后调用状态对象的 initState()。
State 的子类可以重写 initState()，以执行只需要在初始化时发生的工作。
例如，可以重写 initState() 来配置动画或订阅平台服务。实现 initState() 的必须以调用 super.initState 开头。
当不再需要状态对象时，框架会调用状态对象的 dispose()。重写 dispose() 函数以执行清理工作。
例如，可以重写 dispose() 来取消定时器或取消订阅平台服务。dispose() 的实现通常以调用 super.dispose 结束。
 */
main() {
  runApp(MaterialApp(
    home: Scaffold(
        appBar: AppBar(
          title: Text('生命周期'),
        ),
        body: HomePage()),
  ));
}

class Widget2 extends StatelessWidget {
  const Widget2({super.key});

  //Stateless 这个方法是自己写的,不是重写父类的,不能自动跳入到这里
  // void initState() { //无状态的widget没有生命周期方法
  //   // TODO: implement initState
  //   super.initState();
  // }
  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}

class HomePage extends StatefulWidget {
  HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    print("build执行了");
    return Container(
      height: 200,
      color: Colors.green,
      child: Row(
        /*
        // mainAxisAlignment: MainAxisAlignment.spaceEvenly,//均匀分布子控件,两边顶头也有空间
          mainAxisAlignment: MainAxisAlignment.spaceBetween,//均匀分布子控件,两边顶头没有空间
      // crossAxisAlignment: CrossAxisAlignment.start,//顶端对齐
          crossAxisAlignment: CrossAxisAlignment.stretch,//只有交叉轴有拉伸stretch是拉伸,下面container会被拉伸Text不会被拉伸
         */
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        //mainAxisAlignment: MainAxisAlignment.spaceAround,//中间分布平均的控件,两边顶头的用一半的中间的空间

        //交叉轴默认对齐方式是center ,主轴是start
        // crossAxisAlignment: CrossAxisAlignment.end,//交叉轴底部对齐
        // crossAxisAlignment: CrossAxisAlignment.stretch,
        ////只有交叉轴有拉伸stretch是拉伸,下面container会被拉伸Text不会被拉伸
        children: <Widget>[
          /*
          Container(
            width: 100,
            height: 100,
            color: Colors.blue,
          ),

          Text(
            "abc=",
            style: TextStyle(fontSize: 25, backgroundColor: Colors.yellow),
          ),
          Text(
            "abc=",
            style: TextStyle(fontSize: 25, backgroundColor: Colors.yellow),
          ),
          Text(
            "abc=",
            style: TextStyle(fontSize: 25, backgroundColor: Colors.yellow),
          ),
          */

        Container(
        width: 100,
        height: 100,
        color: Colors.blue,
      ),
          Expanded( //按比例缩放子控件
            // flex: 1,//默认值是1
            child: Text(
              "abc1234567890=",
              style: TextStyle(fontSize: 40, backgroundColor: Colors.yellow),
            ),

          ),
          Expanded(
              flex: 2,
              child: Container(
            color: Colors.red,
          )),
          Expanded(
              flex: 2,

              child: Text(
            "789=",
            textAlign: TextAlign.center,
            style: TextStyle(
                fontSize: 25, backgroundColor: Colors.yellow),
          )),
          Expanded(child: Text(
            "abc=",
            style: TextStyle(fontSize: 25, backgroundColor: Colors.yellow),
          ))
        ],
      ),
    );
  }
}
