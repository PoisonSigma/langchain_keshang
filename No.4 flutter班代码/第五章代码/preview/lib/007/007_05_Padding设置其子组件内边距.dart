/*
Padding通过给定的填充值来设置其子组件内边距的小部件
Padding 和 Container.padding 没有任何区别
如果提供了Container.padding参数，Container会为您构建一个Padding小部件。
Container并不直接实现其属性。相反，Container将一些较简单的小部件组合在一起，形成一个方便的包装。
例如，Container.padding属性会导致容器构建一个Padding小部件，

可以随意以满足您需求的任何组合方式构建这些较简单的小部件。
事实上，Flutter中的大多数小部件都是其他较简单小部件的组合。
组合而不是继承是构建小部件的主要机制。


padding: const EdgeInsets.all(20),//上下左右都20
padding: EdgeInsets.fromLTRB(10, 0, 5, 20),//左上右下
padding: EdgeInsets.only(top: 20),//单独设置子控件一个方向的内边距


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
    /*
//这里演示使用Padding设置子控件的内边距,效果跟Container的padding属性一样
    return Container(
      width: 100,
      height: 100,
      color: Colors.yellow,
      child: Padding(
        //这里的Padding被外面的Container约束为100*100,他给子控件增加了20边距,让子控件变成60*60
        padding: EdgeInsets.all(20),
        child: Container(
          color: Colors.red,
        ),
      ),
    ) ;
*/

    //下面是Container的padding属性,跟直接用Padding类一样
    return Container(
      width: 100,
      height: 100,
      color: Colors.yellow,
      // padding: const EdgeInsets.all(20),//上下左右都20
      padding: EdgeInsets.fromLTRB(20, 0, 5, 20),//左上右下
      // padding: EdgeInsets.only(top: 20),//单独设置子控件一个方向的内边距
      child: Container(
        color: Colors.red,
      ),
    );
     

    /*
    return Container(
      width: 100,
      height: 100,
      color: Colors.green,
      child: Align(
        alignment: Alignment.center,
        child: Container(
          width: 50,
          height: 50,
          color: Colors.yellow,
        ),

      ),

    );
     */

  }

}