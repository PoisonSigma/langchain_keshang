import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
/*
响应小部件生命周期事件
在 StatefulWidget 上调用 createState() 后，框架会将新的状态对象插入到树中，然后调用状态对象的 initState()。
State 的子类可以重写 initState()，以执行只需要在初始化时发生的工作。
例如，可以重写 initState() 来配置动画或订阅平台服务。实现 initState() 的必须以调用 super.initState 开头。
当不再需要状态对象时，框架会调用状态对象的 dispose()。重写 dispose() 函数以执行清理工作。
例如，可以重写 dispose() 来取消定时器或取消订阅平台服务。dispose() 的实现通常以调用 super.dispose 结束。
 */
main(){
  runApp(MaterialApp(home: Scaffold(
      appBar: AppBar(
        title: Text('生命周期'),
      ),body
      :  HomePage()

  ),));
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
  int  i = 0;
  HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  void dispose() {
    // TODO: implement dispose
    super.dispose();
    print("销毁");
  }
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    print("initState初始化");
  }
  @override
  Widget build(BuildContext context) {
    print("build执行了");
    return
      // Container(
      //   //如果不给尺寸Container就是跟子元素一样的尺寸
      //   width: double.maxFinite,//最大尺寸
      //   height: 100,
      //   // alignment: Alignment.center,//居中对齐
      //     alignment: Alignment.bottomRight,//居中对齐
      //   color: Colors.red,
      //
      //   child: Text("abc",style: TextStyle(fontSize: 40,color: Colors.yellow,backgroundColor: Colors.green),));

      Container(
          // width: double.maxFinite,//最大尺寸
        width: 200,
        height: 100,
        alignment: Alignment.center,//居中对齐
        // alignment: Alignment.bottomRight,//居中对齐
        child: Text("abc",
            // textAlign: TextAlign.center,//无法通过Text自己的居中来让Text居中到屏幕中间
            style: TextStyle(fontSize: 40,color: Colors.yellow,backgroundColor: Colors.green)),
      );
  }
}
