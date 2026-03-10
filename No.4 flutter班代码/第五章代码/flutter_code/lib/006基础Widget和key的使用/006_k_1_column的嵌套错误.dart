/*
嵌套异常错误:
RenderFlex children have non-zero flex but incoming height constraints are unbounded.
渲染弹性属性Flex的子项具有非零的Flex弹性属性，但传入的高度限制是无边界的的。
当垂直约束是无界的时候
当一个 Column 包含一个或多个 Expanded 或 Flexible 子组件
，并且这个 Column 被放置在另一个 Column、ListView 或者一些不提供最大高度约束的其他上下文中时，
你会在运行时遇到一个异常，提示有子组件具有非零的弹性值flex值，
使用 Flexible 或 Expanded 意味着在布局完所有其他子组件后，
剩余的空间必须被平均分配。但是，如果传入的垂直约束是无界的，那么剩余的空间就是无限的。

解决这个问题的关键通常是确定为什么 Column 会接收到无界的垂直约束。
发生这种情况的一个常见原因是 Column 被放置在了另一个 Column 中（
没有在内部嵌套的 Column 周围使用 Expanded 或 Flexible）。当 Column 布局其非弹性子组件
（即那些没有被 Expanded 或 Flexible 包裹的子组件）时，它会给它们无界的约束，以便它们能够自行确定自己的尺寸
（通常传递无界约束是向子组件发出信号，表明它应该收缩包裹其内容）。在这种情况下，
通常的解决方案是将内部 Column 包裹在 Expanded 中，以指示它应该占据外部 Column 的剩余空间，
而不是允许它占用任何它想要的空间。
 */
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body: const HomePage())));
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    //之前学过:Expanded控件,会消耗所有可用尺寸,扩展到父级传入的限定尺寸
    //下面是一个错误例子,内层的Column被嵌套在外层的Column中,并且内层的Column,里面有Expanded,
    // 因为Expanded会在内层的列布局完2个Text之后,会把剩余空间平均分配,这个空间是父级传入的垂直大小,但是因为内层的Column嵌套在外层的Column里,
    // 没有指定垂直高度,因为内层的Column的主轴最大尺寸mainAxisSize默认值是max,占用最大,而外层Column垂直方向能容纳的高度也是无限大,只是会黄黑条纹的报错,那么内层Column的垂直高度就是无限大
    // 那么flutter框架认为这个垂直约束是无限的,那么内层的Expanded平均分配的垂直高度也是无限制的

    //下面解决方法是给内层Column设置了container的高度
    /*
    return Container(
      color: Colors.green,
      child: Column(
        children: <Widget>[
                Text("1111"),
          Text("2222"),
          Container(
            color: Colors.yellow,
            height:400 ,
            child: Column(
              children: <Widget>[
                Text("333"),
                Text("444"),
                Expanded(
                  flex: 1,
                  child:
                Container(
                    color: Colors.red,
                    child: Text("555")),
                )
              ],
            ),
          ),
          
        ],
      ),
    );
    */
    /*
//下面是第二种解决方法,把内层的Column放在Expanded中,那么他就把外层的Column的尺寸全部取走了,
    //变成了屏幕高度,总之解决方法就是给内层,Expanded所在的Column一个确定的大小就行了
    return Container(
      color: Colors.green,
      child: Column(
        children: <Widget>[
          Text("1111"),
          Text("2222"),
          Expanded(
            child: Column(
              children: <Widget>[
                Text("333"),
                Text("444"),
                Expanded(
                  flex: 1,
                  child: Container(color: Colors.red, child: Text("555")),
                )
              ],
            ),
          ),
        ],
      ),
    );
    */

    //下面演示以后学习的ListView里面也 会出现这种错误,ListView就是带滚动条的列
    /*
    return Container(
      color: Colors.green,
      child: ListView(
        children: [
          Text("111"),
          Text("222"),
          Container(
            color: Colors.yellow,
            height: 300,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,//交叉轴默认值是居中的
              children: <Widget>[
                Text("333"),
                Text("444"),
                Expanded(child: Container(
                    color: Colors.red,
                    child: Text("5555")))
              ],
            ),
          ),
        ],

      ),
    );
    */

    //下面演示以后学习的ListView里面也 会出现这种错误,ListView就是带滚动条的列
    return Container(
      color: Colors.green,
      child: ListView(
        children: [
          Text("111"),
          Text("222"),
          Container(
            height: 300,//解决方法就是设定一个高度,暂时不用Expanded因为计算不出来外面的剩余高度
            color: Colors.yellow,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start, //交叉轴默认值是居中的
              children: <Widget>[
                Text("333"),
                Text("444"),
                Expanded(
                    child: Container(color: Colors.red, child: Text("5555")))
              ],
            ),
          ),
        ],
      ),
    );

  }
}
