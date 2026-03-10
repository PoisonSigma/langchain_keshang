import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
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

main(){
    runApp(MaterialApp(home:  Scaffold(
    appBar: AppBar(
    title: Text('标题栏'),
    ),body
  :
  Body()
  )));
}
class Body extends StatelessWidget {
  const Body({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 300,//给一个固定高度,
      width: double.maxFinite,//最大宽度
      color: Colors.green,
      child: Row(
        // mainAxisAlignment: MainAxisAlignment.spaceEvenly,//均匀分布子控件,两边顶头也有空间
        mainAxisAlignment: MainAxisAlignment.spaceBetween,//均匀分布子控件,两边顶头没有空间
// crossAxisAlignment: CrossAxisAlignment.start,//顶端对齐
        crossAxisAlignment: CrossAxisAlignment.stretch,//只有交叉轴有拉伸stretch是拉伸,下面container会被拉伸Text不会被拉伸
          // 拥有每个均匀间隔图像的行
        children: [
          Container(width: 100,
          height: 100,
            color: Colors.red,
          ),
          Text("abc1234567890",style: TextStyle(backgroundColor: Colors.yellow),),
          Text("abc1234567890",style: TextStyle(fontSize: 10,backgroundColor: Colors.yellow),),
          Text("abc1234567890",style: TextStyle(fontSize: 10,backgroundColor: Colors.yellow),),

          /*
          //当大小超出范围会漏出黑黄的边,
          Expanded(//Expanded把里面的child按照flex的比例平均分配
            flex: 1,//每个child占比,默认是1
            child: Text("abc1234567890",style: TextStyle(fontSize: 40,
            backgroundColor: Colors.yellow),),),
          Expanded(
            flex: 1,//每个child占比
            child: Text("abc1234567890",style: TextStyle(fontSize: 40,
                backgroundColor: Colors.yellow),),),
          Expanded(
            flex: 2,//每个child占比
            child: Text("abc1234567890",style: TextStyle(fontSize: 40,
                backgroundColor: Colors.yellow),),),

           */
        ],),
    );
  }
}
