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
            title: Text("Container详解"),
          ),
          body: HomePage())));
}

//如果没有Scaffold上面的约束条件会有变化
// main(){
//     runApp(MaterialApp(home: HomePage()
//
//   ));
// }
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return
/*
      //这里container没有child会尽可能的变大,接近无限大
      Container(
      //color要绘制在子项后面的颜色.
      // 当背景是简单颜色时，应优先考虑使用此属性。其他情况,比如圆角颜色 使用 decoration 属性。如果使用了装饰，则此属性必须为 null


color: Colors.red,
    );
   */

      /*
      //下面这段颜色color和decoration不能同时设置颜色,因为这2个颜色都会画在container里面,child的后面
    Container(
      /*
      不同同时提供颜色和装饰
      Cannot provide both a color and a decoration
To provide both, use "decoration: BoxDecoration(color: color)".
       */
      // color: Colors.yellow,//要不给颜色,要不给装饰
    // 绘制在子项后面的装饰。


      decoration: BoxDecoration(
        color: Colors.green,//如果不要圆角,那么就直接用color填充颜色
        borderRadius: BorderRadius.circular(20)//带圆角边框的装饰
      )
    );
*/

/*
      //下面颜色color 和  decoration是在child的后面,decoration是在child的后面是背景装饰,foregroundDecoration是在child前面
      Container(
        width: 100,
        height: 100,
        // color: Colors.yellow,
        decoration: BoxDecoration(color: Colors.green),
        //背景装饰
        child: Text("abc"),

        foregroundDecoration: BoxDecoration( //前景装饰
            color: Colors.yellow,
            borderRadius: BorderRadius.circular(20)

        ),
      );
  }
*/

      /*
      //下面例子演示,如果
      //   父级的没有大小约束，在这种情况下，它们会尽可能地变小。子项的容器会根据子项的大小调整自己的大小。
      Container(
        color: Colors.red,
        //里面的Container有大小100*50,外面的container因为没有设置大小,所有大小跟着里面的child大小尽可能的小
        child: Container(

          width: 100,
          height: 50,
          decoration: BoxDecoration(
              color: Colors.green,
              borderRadius: BorderRadius.circular(20)
          ),
        ),
      );
  }
  */
/*
      //container约束的优先级,外层的大于里层的,父级>child,如果父级没有约束,才尽可能小的根据child的约束改变
      //下面例子套了3个container,最外层200*200,因为最外层有约束,所以里面的约束不生效

      //父级有约束,container会扩展自身适应父级约束,并且传递给child
      Container(
        width: 200, //如果这里设置了200,那么里面的2级都会跟着改变尺寸
        // height: 200,//如果这行注释掉,那么最外层的约束高度就没有,第二层300的高度就变成了最外层的约束
        color: Colors.red,
        child: Container(

          width: 300,
          height: 300,
          decoration: BoxDecoration(
              color: Colors.green,
              borderRadius: BorderRadius.circular(20)
          ),
          child: Container(
            color: Colors.yellow,
            width: 100,
            height: 100,
          ),
        ),
      );
  }
*/

      //   如果小部件有对齐方式，并且父级提供了无界约束，则 Container 会尝试围绕子项调整自身大小。
      //
      // 如果小部件有对齐方式，并且父级提供了有界约束，则 Container 会尝试扩展以适应父级，然后根据对齐方式在自身内部定位子项。
      //
      // 否则，小部件有子项但没有高度、宽度、约束和对齐方式，Container 会将父级传递给子项的约束，并调整自身大小以匹配子项。

      //当有对齐方式父类子类都有,并且尺寸不同,就分成2个,就最大化
      Container(
        // width: 400,
        height: 400,
        padding: EdgeInsets.all(20),
        //后面会讲
        color: Colors.yellow,
        alignment: Alignment.centerLeft,
        child: Container(
          width: 200,
          //宽度不给就是最大化
          height: 200,
          alignment: Alignment.topLeft,
          padding: const EdgeInsets.all(40.0),
          color: Colors.blue,
          // transform: Matrix4.rotationZ(0.2),//旋转//后面会讲
          child: Text(
            'Hello World',
          ),
        ),
      );
  }
}
