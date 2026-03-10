import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home: Widget1(),));

}
//大家通过自定义代码段输入stf来快速生成自定义的StatefulWidget有状态的小部件,
// 有状态就是指他可以改变里面的页面,内容,通过setState调用build方法实现

//因为 StatefulWidget 和 State<>都是抽象类,不能直接创建对象,所以我们只能extends继承他,使用他的子类创建对象
class Widget1 extends StatefulWidget{
  @override
  State<Widget1> createState() {
    // TODO: implement createState
    return State1();
  }
}
//Widget和State之所以分成2个类,是因为Widget 和 State 是有自己不同的声明周期,State的build方法是持久的,
// Widget是临时的,那么临时对象消失以后,就没法找到他, 也就改变不了他的页面显示
// 但是Build里面的东西可以改变,通过刷新Build
//重写方法的返回类型可以是父类或者是子类型
// e补充01类型系统type system->02子类中重写方法的返回类型必须是父类型或者是它的子类型 在这课里给大家补充了这个语法
//   我们返回了自己创建的子类的对象
class State1 extends State<Widget1>{
  int i = 0;
  @override
  Widget build(BuildContext context) {
    print("build执行了");
    print("${++i}");
   return Text("${i}");
  }
}





/*
//下面是系统自动生成的HelloWorld代码
class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return Text("abc");
  }
}
*/