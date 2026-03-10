import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
//第二个例子,为了演示 Widget的嵌套,这里演示 Center居中组件 里面 child参数 嵌套 文本框Text
/*
main(){
    runApp(

        MaterialApp(home:fun1()
      )
    );
}
Widget fun1(){  //返回类型是 Widget
  return Center(
    child: Text("1233213ab",style: TextStyle(fontSize: 100),),
  );
}
 */

// 复习之前语法里面学习的const 嵌套问题，最外层用了const，
// 那么里面就不用加，如果里面有单独的不是const的，那么最外层不能是const
main(){
  String str = "1233213ab";
  runApp(
       MaterialApp(home:Center(
        child: Text(str,style: const TextStyle(fontSize: 100),),
      )
      )
  );
}

