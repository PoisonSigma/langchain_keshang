/*

 1.margin是给container自己增加外边距

 2.父控件只有单独的一个子控件margin的作用跟在父级增加一个padding内边距视觉效果一样
 3.通过树形结构发现当前container尺寸会增加到带外边距的尺寸,
 但是装饰decoration,例如color颜色和圆角 不会在外边距上面渲染,decoration的尺寸是自己的尺寸去掉margin的尺寸,同时child的尺寸也是decoration的尺寸
 但是子控件约束的尺寸还是width和height
4.在父控件没有对齐方式的时候decoration的面积是container自己的尺寸减去 margin的尺寸,而不是width和height
 5.margin给自己增加外边距和 给父控件增加内边距padding的区别:
 margin可以给当前container自己周围增加外边框,
 这样可以在多个子控件的控件中,跟相邻其他控件单独隔开
 而padding只能整体对所有子控件增加内边距,无法对多个子控件进行单独设置边距

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
    //这个例子演示子控件的margin扩大了子控件的尺寸,但是decoration渲染面积没有被扩大
    return Container(
      width: 100,
      height: 100,
      color: Colors.green,
      // alignment: Alignment.center,
      //3.1 在没有对齐方式的时候decoration的面积是自己的尺寸减去 margin的尺寸,而不是width和height
      child:Container(
        margin: EdgeInsets.all(10),

        width: 50,
        height: 50,
        // color: Colors.yellow,
        decoration: BoxDecoration(color: Colors.yellow,
          borderRadius: BorderRadius.circular(10)

        ),
        // 3.通过树形结构发现当前container尺寸会增加到外边距的尺寸,
        // 但是装饰decoration,例如color颜色和圆角 不会在外边距上面渲染,decoration的尺寸还是自己的width和height
        //当前container能容纳的子控件尺寸还是自己的width和height50*50
        // child: Container(
        //   color: Colors.red ,
        // ),
      ),
    );
*/
/*
    //这个例子演示父控件有内边距padding,视觉效果跟上面的margin一样,但是子控件container尺寸是50*50,没有被padding扩大
    return Container(
      width: 100,
      height: 100,
      color: Colors.green,
      padding: EdgeInsets.all(10),
      child:Container(

        width: 50,
        height: 50,
        // color: Colors.yellow,
        decoration: BoxDecoration(color: Colors.yellow,
          borderRadius: BorderRadius.circular(10)

        ),
      ),
    );


 */
    /*
    //下面是一个具体的例子，展示了如何使用margin属性来创建一个48x48像素大方块
    //并且设置边距以确保它与其他相邻部件保持一定的距离：
    return Container(
      color: Colors.green,
      width: 60,
      height: 60,
      child: Container(
        //作用,在自己周围增加边距10,如果没有这个,也没有对其方式,
        // 那么子控件48*48将会被父控件直接变大到60
        //父控件只有单独的一个子控件margin的作用跟在父级增加一个padding一样
        margin: const EdgeInsets.all(10.0),
        color: Colors.yellow,
        width: 48.0,
        height: 48.0,
        child: Container(
          color: Colors.red,
        ),
      ),
    );
    */

    return Container(
      padding: EdgeInsets.fromLTRB(20, 0, 20, 20),
      color: Colors.green,
      child: Column(
        children: <Widget>[
          Container(
            margin: EdgeInsets.fromLTRB(20, 0, 20, 20),
            height: 50,
            color: Colors.red,
          ),
          Container(
            margin: EdgeInsets.fromLTRB(50, 0, 50, 20),
            height: 50,
            color: Colors.yellow,
          ),
          Container(
            margin: EdgeInsets.fromLTRB(100, 50, 100, 20),
            height: 50,
            color: Colors.blue,
          ),
        ],
      ),
    );
  }
}
