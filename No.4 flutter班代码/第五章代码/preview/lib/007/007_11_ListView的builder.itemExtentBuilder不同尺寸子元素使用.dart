/*

这个例子演示 参数 itemExtentBuilder:itemExtentBuilder,  //可以单独设置某个元素高度
 */

/*
一个指向小部件在小部件树中位置的句柄。
该类提供了一组方法，可以从 StatelessWidget.build 方法和 State 对象的方法中使用。
BuildContext 对象被传递给 WidgetBuilder 函数（例如 StatelessWidget.build），并且可以从 State.context 成员中获取。一些静态函数（例如 showDialog、Theme.of 等）也接受构建上下文，以便它们可以代表调用小部件执行操作，或者专门为给定上下文获取数据。
每个小部件都有自己的 BuildContext，它成为由 StatelessWidget.build 或 State.build 函数返回的小部件的父级。（同样地，RenderObjectWidgets 的任何子部件的父级也是如此。）特别是，这意味着在 build 方法内部，build 方法的小部件的构建上下文与由该 build 方法返回的小部件的构建上下文不同。这可能会导致一些棘手的情况。例如，Theme.of(context) 查找给定构建上下文的最近的封闭主题。如果小部件 Q 的构建方法包含其返回的小部件树中的一个主题，并尝试使用自己的上下文传递 Theme.of，那么小部件 Q 的构建方法将无法找到该主题对象。它将找到小部件 Q 的祖先中的任何主题。如果需要返回树的子部分的构建上下文，则可以使用 Builder 小部件：传递给 Builder.builder 回调的构建上下文将是 Builder 本身的构建上下文。
*/
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';

// 定义一个 ItemExtentBuilder 函数,第二个参数不用给
double itemExtentBuilder(int index, SliverLayoutDimensions dimensions) {
  // 假设我们有一个根据索引计算高度的简单逻辑
  // 例如，第0个项目高度为50，第1个项目高度为100，以此类推
  return 50.0 + (index * 50.0);
}

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {  //上下文从build方法中传入
    return MaterialApp(
      title: 'ItemExtentBuilder Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('ItemExtentBuilder Example'),
        ),
        body: ListView.builder(
          // 使用我们定义的 itemExtentBuilder 函数
          itemExtentBuilder:itemExtentBuilder,  //多了这个参数可以单独设置某个元素高度
          /*
          itemExtentBuilder: (int index, _) {
         //返回高度是当前序列 乘以 50
            return (index+1) * 50;
          },
           */
          itemCount: 10, //列表子控件个数
          itemBuilder: (BuildContext context, int index) { //上下文从build方法中传入
            //返回每个子控件,通过传入的index序列生成
            return ListTile(
              title: Text('Item $index'),
            );
          },
        ),
      ),
    );
  }
}