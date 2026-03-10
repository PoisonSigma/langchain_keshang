

/*
ListView.builder的特点是屏幕页面要显示当前元素的时候,才开始执行 builder 对应的序列index里的代码,例如屏幕滚动到最下面index为8的时候,才执行(context,index = 8){ 这里代码会被执行}
一个指向小部件在小部件树中位置的句柄。
该类提供了一组方法，可以从 StatelessWidget.build 方法和 State 对象的方法中使用。
BuildContext 对象被传递给 WidgetBuilder 函数（例如 StatelessWidget.build），并且可以从 State.context 成员中获取。一些静态函数（例如 showDialog、Theme.of 等）也接受构建上下文，以便它们可以代表调用小部件执行操作，或者专门为给定上下文获取数据。
每个小部件都有自己的 BuildContext，它成为由 StatelessWidget.build 或 State.build 函数返回的小部件的父级。（同样地，RenderObjectWidgets 的任何子部件的父级也是如此。）特别是，这意味着在 build 方法内部，build 方法的小部件的构建上下文与由该 build 方法返回的小部件的构建上下文不同。这可能会导致一些棘手的情况。例如，Theme.of(context) 查找给定构建上下文的最近的封闭主题。如果小部件 Q 的构建方法包含其返回的小部件树中的一个主题，并尝试使用自己的上下文传递 Theme.of，那么小部件 Q 的构建方法将无法找到该主题对象。它将找到小部件 Q 的祖先中的任何主题。如果需要返回树的子部分的构建上下文，则可以使用 Builder 小部件：传递给 Builder.builder 回调的构建上下文将是 Builder 本身的构建上下文。
*/

import 'package:flutter/material.dart';

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
    return Container(
        color: Colors.green,
        child: ListView.builder(
            itemCount: 10, //子元素的个数,不传就是无限大
            itemBuilder: //里面返回的是每个子元素要显示的内容
                (context, index) {
              // Text("$index");//注意这里一定要返回widget,不返回不会提示错误,但是什么子元素都不显示
              /*
        return Container(
           color: Colors.yellow,
             margin: EdgeInsets.all(10),//可以看到背景,不会渲染外边距
             // padding: EdgeInsets.all(10),//渲染部分不会漏出背景
             child: Text("$index"));
      }
         */
            return   Column(
              children: <Widget>[
                Text("abc"),
                Divider()
              ],
            );

            })
    );
  }
}
