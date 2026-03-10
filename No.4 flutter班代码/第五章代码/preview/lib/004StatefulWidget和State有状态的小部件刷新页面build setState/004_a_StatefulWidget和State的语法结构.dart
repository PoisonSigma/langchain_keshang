import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
    runApp(MaterialApp(home:Widget1() ,));
}
class Widget1 extends StatefulWidget{
  @override
  State<Widget1> createState() {
    // TODO: implement createState
    //因为State<Widget1>是抽象类,所以不能创建对象,我们自己创建一个子类,继承自他,然后返回他的对象
    return State1();
  }
}
class State1 extends  State<Widget1>{
  @override
  //必须重写的build方法,把里面返回的小部件显示在屏幕上
  Widget build(BuildContext context) {
    // TODO: implement build
    return Text("abc");
  }

}
//大家通过自定义代码段输入stf来快速生成自定义的StatefulWidget有状态的小部件,
// 有状态就是指他可以改变里面的页面,内容,通过setState调用build方法实现
