//下面的规则,全是在脚手架里面scaffold里面的
/*
Container容器
因为Container中有许多其他小组件的属性,内容太多,所以属性不全讲,后面陆续给大家讲解
1.填充包围子项
2.如果宽度高度设置了值,就当做约束条件,改变包围的大小.比如设置了width:100,那么宽度就是100

容器首先用内边距 padding 包围child(后面会讲)
在绘制过程中，容器应用给定的变换transform属性，(后面会讲)
然后绘制背景装饰 decoration
然后绘制子项child，
最终绘制前景装饰foregroundDecoration

没有子项的容器会尽可能地变大，
嵌套container的大小尺寸:约束的优先级,外层的大于里层的,父级>child,
如果父级没有约束,才尽可能小的根据child的约束改变

如果有对其方式,例如居中,居左,而且父级没有约束,那么就最大化,不取子控件的尺寸(后面会讲)
 */

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            //这里不是今天要主要讲的内容,为了显示body的所在位置,所以用红色占位
            title: Container(
                color: Colors.red,
                height: 60,
                child: const Text('appbarTitle')),
          ),
          body: const HomePage())));
}

/*
main(){
  runApp(MaterialApp(home:   HomePage()
  ));
}
 */
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    double h = 100;

    return
        /*
    //这里container没有child会尽可能的变大,接近无限大,跟父级一样大
    Container(
      color: Colors.yellow,//color要绘制在子项后面的颜色.
    );

     */

/*
    //下面这段颜色color和decoration不能同时设置颜色,因为这2个颜色都会画在container里面,child的后面

      Container(
        // color: Colors.yellow,
        width: h,
        height: h,
        decoration: BoxDecoration(//背景装饰
          color: Colors.red,
          // borderRadius:BorderRadius.circular(h*0.25)//带圆角边框的装饰
        ),
        child: Text("abc"),
        foregroundDecoration: BoxDecoration(
          color: Colors.yellow,
          borderRadius:BorderRadius.circular(h*0.25)//带圆角边框的装饰
        ),

      );
*/
        //下面例子演示,如果
        //   父级的没有大小约束，在这种情况下，它们会尽可能地变小。子项的容器会根据子项的大小调整自己的大小。
        /*
    Container(
      color: Colors.green,
      child: Container(
        width: 200,
        height: 100,
        decoration: BoxDecoration(color: Colors.red,
        borderRadius: BorderRadius.circular(40)
        ),
      ),

    );
    */
        /*
      Container(
        color: Colors.green,
        child: Text("777")
      );
       */
        /*
      Container(
        //这个例子演示,外层,缺少宽或者高的时候,会尽可能小的,变成内层的宽或者高
        width: 200,
        color: Colors.green,
        child: Container(
          width: 200,
          height: 200,
          decoration: BoxDecoration(color: Colors.red,
              borderRadius: BorderRadius.circular(40)
          ),
        ),
      );
*/

        //container约束的优先级,外层的大于里层的,父级>child,如果父级没有约束,才尽可能小的根据child的约束改变
        //下面例子套了3个container,最外层200*200,因为最外层有约束,所以里面的约束不生效
        Container(
          // width: double.maxFinite, //300*200
      width: 400, //300*200
      color: Colors.green,
      // foregroundDecoration:BoxDecoration(
      //     color: Colors.blue, borderRadius: BorderRadius.circular(40)),
      child: Container(
        width: 200, //300*200
        height: 200,
        decoration: BoxDecoration(
            color: Colors.red, borderRadius: BorderRadius.circular(40)),
        child: Container(
            width: double.maxFinite, //300*200
            height: 400,
            decoration: BoxDecoration(
                color: Colors.yellow, borderRadius: BorderRadius.circular(100)),
            // alignment: Alignment.center,
            child: Text(
              "777",

              style: TextStyle(fontSize: 44),
              // textAlign: TextAlign.center,//只有水平居中
            )),
      ),
    );
  }
}
