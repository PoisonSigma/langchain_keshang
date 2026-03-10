/*

*/
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
  runApp(MaterialApp(home: Scaffold(
      appBar: AppBar(
          title: Container(alignment: Alignment.center,
            height: 100,//这段appBar为了演示appBar占用的大小,其他不深究
            color: Colors.red,
            child: Text("abc"),
          )

      ),body
      :
  HomePage()  )));
}
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    //规则:Container没有width或者height,但是有对齐方式,那么width或者height无限大
    //最外层的容器Container因为没有尺寸,并且有对其方式center (Center extends Align)所以最大化
    return
    /*
      //下面例子演示,外层尺寸是300*300,内层Container因为没有child,
      // 所以他的尺寸会尽可能的大,也变成300*300
      //
      Container(
    width: 300,
      height:300,
      color: Colors.green,
        child: Container(
        color: Colors.red,
      ),
    );
     */
      Container(
        width: 300,
        height:300,
        color: Colors.green,
        //下面演示没有对齐方式的时候,嵌套container的大小尺寸:
        // 约束的优先级,外层的大于里层的,父级>child,
        //所以下面注释掉alignment后2个Container都变成了300
        //如果打开注释alignment后,里面的container就变成100,并且在外面container对齐是左上

        // alignment: Alignment.topLeft,  //
        child: Container(
          width: 100,
          height: 100,
          alignment: Alignment.bottomRight,
          color: Colors.yellow,
          child: Text("abc"),
        ),
      );
  }
}

