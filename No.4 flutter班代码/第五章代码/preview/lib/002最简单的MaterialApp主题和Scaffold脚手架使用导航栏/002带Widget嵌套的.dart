/*




第二个例子,为了演示 Widget的嵌套,这里演示 Center居中组件 里面 child参数 嵌套 文本框Text
 */



import 'package:flutter/material.dart';

void main() {
  runApp(
      MaterialApp(
    // const  MaterialApp( //  报错,这里调用函数在MaterialApp 前面不能加const
    home: fun1()//
  )
  );
}

Widget fun1(){//注意函数返回类型不能不写,否则就变成dynamic 会报错
  // 复习之前语法里面学习的const 嵌套问题，最外层用了const，那么里面就不用加，如果里面有单独的不是const的，那么最外层不能是const
  String str = "123";
  return  Center(
    child: Text(
      str,
      style: const TextStyle(color: Colors.red, fontSize: 40.0),
    ),
  );
}

