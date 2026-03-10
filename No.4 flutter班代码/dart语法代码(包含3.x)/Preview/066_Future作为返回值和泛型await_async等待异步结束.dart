/*
await是等待 Future里面的异步操作结束, 返回的是return的值,会阻塞线程,等待执行完以后才向下执行
async函数会返回Future
 */
import 'dart:async';
import 'dart:io';

main() async {
  print("start");


  var r1 = await Future<int>.value(123); //这里面返回的值是 123
  print("r1=$r1");
  var r2 = await Future<int>.delayed(Duration(seconds: 2), () {
    return 456;
    //这里没有返回int,报错
  });

  print("r2=$r2");

  var r3 = await getData2();
  print("r3=$r3");
  print("end");
}

 getData() {
  return Future.value(123); //正确
  // return Future.value("ABC");//错误,泛型错误
}

 Future<String> getData2() async {  //async函数返回类型是Future
  //会返回Future

  String result = await Future.delayed(Duration(seconds: 2), () {
    return "网络数据1";
  });
  return result;
}

//Future作为函数返回值
Future<int> fun3() {
  return Future.delayed(Duration(seconds: 1), () {
    return 100;
  });
}
