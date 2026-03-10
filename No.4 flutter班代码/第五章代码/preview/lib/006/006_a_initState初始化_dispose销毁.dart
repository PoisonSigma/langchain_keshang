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
    runApp(MyApp());
}
class MyApp extends StatelessWidget {
   MyApp({super.key});

   void initState() {//Stateless 这个方法是自己写的,不是重写父类的,不能自动跳入到这里
     // TODO: implement initState
     // super.initState();
     print("initState");
   }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home:  Scaffold(
    appBar: AppBar(
    title: Text('appbarTitle'),
    ),
    body: HomePage()
    ));
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int i = 0;
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    print("initState");
  }
  @override
  void dispose() {
    // TODO: implement dispose
    super.dispose();
    print("结束dispose");//可以重写 dispose() 来取消定时器
  }
  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,//居中

      children: <Widget>[
        ElevatedButton(onPressed: (){
        i++;
        }, child:Text("$i"))
      ],
    );

  }
}

