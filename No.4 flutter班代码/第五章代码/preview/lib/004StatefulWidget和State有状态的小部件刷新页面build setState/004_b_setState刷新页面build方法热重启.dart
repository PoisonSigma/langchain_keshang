import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Row(
    children: [
      Text("777"),//这里的不会被被热启动刷新,因为他不在build里面
      Spacer(),
      TextButton(onPressed: (){
        print("点击按钮");
        //注意这里没有setState
      }, child: Text("点击按钮")),
      App2(key:Key("abc"))   ], //这里的key暂时用不上
  )));
}
//因为 StatefulWidget 和 State<>都是抽象类,不能直接创建对象,所以我们只能extends继承他,使用他的子类创建对象
class Widget1 extends  StatefulWidget{
  @override
  State<Widget1> createState() {
    // TODO: implement createState
    return State1();
  }
}
//
class State1 extends State<Widget1>{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Text("abc");
  }

}


//Widget和State之所以分成2个类,是因为Widget 和 State 是有自己不同的声明周期,State的build方法是持久的,
// Widget是临时的,那么临时对象消失以后,就没法找到他, 也就改变不了他的页面显示
// 但是Build里面的东西可以改变,通过刷新Build
class App2 extends StatefulWidget {
// App2({super.key});
App2({Key? key}):super(key: key);//相当于上面自动生成的
  @override
  State<App2> createState() {
    // TODO: implement createState
    //这里要返回的是父类型State<App2>  的对象
    return State2(); //重写方法的返回类型可以是父类或者是子类型
    // e补充01类型系统type system->02子类中重写方法的返回类型必须是父类型或者是它的子类型 在这课里给大家补充了这个语法
    //   我们返回了自己创建的子类的对象
  }
}

class State2 extends State<App2> {
  int i = 0;//自己类的成员变量
  @override
  //热启动会刷新build方法里面的内容,不在build方法里面的内容不会被刷新
  //build方法会把里面的内容,一层一层的向上返回,并且描述到屏幕上
  Widget build(BuildContext context) {
    print("重新进入build页面");
    // TODO: implement build
    // return Text("123");
    return Row(children: [
      ElevatedButton(onPressed: (){
          print("object ${++i}");
          setState(() { //这个方法可以刷新页面,重新进入build方法
            print("改变了");
          });
      }, child:Text("$i") )
    ],);
  }
}

//下面是系统自动生成的HelloWorld代码
class MyApp extends StatefulWidget {
  // const MyApp({super.key}); //调用父类的命名构造函数,简写
   const MyApp({Key? key}):super(key: key)  ;//这个自己写的等价与上面
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}

