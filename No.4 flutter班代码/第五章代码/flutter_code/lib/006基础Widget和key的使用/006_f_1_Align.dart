/*
原理,从哪一层开始有对齐方式,他的子控件的尺寸就变成自己的尺寸,而不是被外层container尺寸改变大小
当container的child有了自己的尺寸,那么这个container被视为没有child的规则,当不设置尺寸的时候,所以尺寸会变得无限接近父级尺寸
如果有了对齐方式,外层container如果没设置尺寸,会变得无限大,子控件有了自己的尺寸,外层container没有设置尺寸的话,这时外层container不再像没有对齐方式那样,跟随子控件大小改变,
而是外层container扩张到父级的大小,相当于内外层的container被对齐方式断开了
*/
import 'package:flutter/material.dart';
main(){
    runApp(MaterialApp(home:  Scaffold(
    appBar: AppBar(
    title: Container(
        color: Colors.red,
        height:  60,
        child: Text('Align对齐')),
    ),
    body: HomePage()
    )));
}
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
   /*
    return Container(
      width: 100,
        color: Colors.green,
        alignment: Alignment.topRight,
        child: Text("abc"),
    );
    */


    //Align的效果把自身尺寸设置成跟父级一样大小,再把child控件对齐,效果就像container设置了对齐方式一样
    return Container(
      width: 200,
      color: Colors.green,
      child:Align(
        widthFactor: 1.5,
        heightFactor: 1,
        // alignment: Alignment.topRight,
          alignment:Alignment(0,0),  //1是 x轴或者y轴最大(最右或者最下)  -1是最小, 0是居中
        child:  Text("abc",style: TextStyle(fontSize: 44),),
      )
    );


    return Container(
      color:  Colors.green,
      alignment: Alignment.bottomLeft,
      child: Container(
        width: 100,
        height: 100,
        decoration: BoxDecoration(color: Colors.yellow,
        borderRadius: BorderRadius.circular(40)
        ),
        child: Align(
          alignment: Alignment.topRight,
          child: Container(
            width: 50,
            height: 50,
            color: Colors.red,
          ),
        ),
      )
    );


  }
}
