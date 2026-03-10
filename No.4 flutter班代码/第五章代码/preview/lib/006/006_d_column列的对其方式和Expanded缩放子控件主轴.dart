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
注意:Expanded扩充子控件的主轴,而不是交叉轴
 */
main() {
  runApp(MaterialApp(
    home: Scaffold(
        appBar: AppBar(
          title: Text('列的交叉轴'),
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
      // height: 210,
      color: Colors.green,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[

          Container(
            width: 200,
            height: 100,
            color: Colors.blue,
          ),
          //注意Expanded 是让子控件,沿着mainAxis主轴扩充,所以在列里面是扩充高度,宽度不改变
          Expanded(
            child: Container(
              color: Colors.pink,
              child: Text(
                "11111=",
                // textAlign: TextAlign.start,//对齐方式改变不了,根据外面CrossAxisAlignment改变
                style: TextStyle(fontSize: 25, backgroundColor: Colors.yellow),
              ),
            ),
          ),
          Expanded(
            child: Text(
              "22222=",
              style: TextStyle(fontSize: 25, backgroundColor: Colors.yellow),
            ),
          ),
          Expanded(
            child: Text(
              "33333=",
              style: TextStyle(fontSize: 25, backgroundColor: Colors.yellow),
            ),
          ),



        ],
      ),
    );
  }
}
