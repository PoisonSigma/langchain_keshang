/*
原理,从哪一层开始有对齐方式,他的子控件的尺寸就变成自己的尺寸,而不是被外层container尺寸改变大小
当container的child有了自己的尺寸,那么这个container被视为没有child的规则,
当不设置尺寸的时候,所以尺寸会变得无限接近父级尺寸
如果有了对齐方式,外层container如果没设置尺寸,会变得无限大,子控件有了自己的尺寸,外层container没有设置尺寸的话,这时外层container不再像没有对齐方式那样,跟随子控件大小改变,
而是外层container扩张到父级的大小,相当于内外层的container被对齐方式断开了



*/
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
              title: Container(
            alignment: Alignment.center,
            height: 100, //这段appBar为了演示appBar占用的大小,其他不深究
            color: Colors.red,
            child: Text("abc"),
          )),
          body: HomePage())));
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    //规则,Container有对齐方式,但是没有尺寸,会撑到更父级一样大,父级尺寸优先级大

    //最外层的容器Container没有尺寸,所以扩张到跟父级一样大.,
    // 因为他有对齐方式,他的子控件使用自己的尺寸
    return
      /*
      Container(
      color: Colors.green,
      alignment: Alignment.center,
      child: Container(
        height: 200.0,
        width: 200.0,
        color: Colors.yellow,
        child:  Align(// Align 控件使用了 Alignment 中定义的一个常量，即 Alignment.topRight ,右上角
          alignment: Alignment.topRight,
          child: Container(
            width: 50,
            height: 50,
            color: Colors.red,
          ),
        ),
      )
    );
*/

/*
        //下面例子演示 Alignment(1, -1) 这种通过数字设置 xy轴坐标对齐
        //Align的效果把自身尺寸设置成跟父级一样大小,再把child控件对齐,效果就像container设置了对齐方式一样
         Container(
          height: 200.0,
          color: Colors.yellow,
          child: const Align(
            alignment: Alignment(1, -1),   //1是 x轴或者y轴最大(最右或者最下)  -1是最小, 0是居中
            child: FlutterLogo(
              size: 60,
            ),
          ),
        );
*/

/*
        //下面例子效果跟上面一样,演示不使用Align ()类,而是在container中使用alignment
           Container(
            height: 200.0,
            width: 200.0,
            alignment:  Alignment(1, -1),
            color: Colors.yellow,
            child: FlutterLogo(
              size: 60,
            ),
          );
*/

      //下面这个例子,Align把子控件放到父空间的右上,
      // 外层Container的子控件的对其方式是左下,但是视觉效果好像没起作用
      //实际情况是这样:Align控件的尺寸扩张到外层container的尺寸变成了200*200,
      // 这个子控件Align已经是最大了,在最左下也不会改变位置,因为大小跟外层Container一样,所以看不出来
      //但是Align把子控件对齐方式设置成了父控件的的右上,所以视觉效果就是右上了,
      //为了演示这个,把Align外面再加一层红色Container来掩饰
/*
        Container(
          height: 200.0,
          width: 200.0,
          color: Colors.yellow,
          alignment: Alignment.bottomLeft,
          child:  Align(// Align 控件使用了 Alignment 中定义的一个常量，即 Alignment.topRight ,右上角
            alignment: Alignment.topRight,
            child: Container(
          width: 50,
              height: 50,
              color: Colors.green,
        ),
      ),
        );
*/
/*
        Container(
      height: 200.0,
      width: 200.0,
      color: Colors.yellow,
      alignment: Alignment.bottomLeft,
      child: Container(
        width: 100,
        height: 100, //加上尺寸可以看出来,Align已经是在外层Container的左下了
        color: Colors.red, //这个就是因为Align把外层200*200的Container填满了,所以看不出来左下对其的效果
        child: Align(
          // Align 控件使用了 Alignment 中定义的一个常量，即 Alignment.topRight ,右上角
          alignment: Alignment.topRight,
          child: Container(
            width: 50,
            height: 50,
            color: Colors.green,
          ),
        ),
      ),
    );
    //为了演示这个,把Align外面再加一层红色Container来掩饰
  }

 */
      Container(
        color: Colors.green,
        child: Align(
        // widthFactor: 2,//宽高是子控件的2倍
        //   heightFactor: 2,
          child: Container(
            width: 100,
            height: 200,
            color: Colors.yellow,
          ),
        ),
      );
  }
}
