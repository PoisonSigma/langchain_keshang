import 'dart:io';

main(){
  print("start");
  getData();
  print("end");
}
getData(){


  /*
  命名构造函数
  value  //只有一句return值的时候用
  delayed //延迟描述
   */
  ////whenComplete是抛出异常也会执行的代码,如果不抛出异常,那么就会按照顺序执行,whenComplete放在哪里就在哪里执行,放在中间和结尾都行
  var f1 = Future.value("abc").then(
          (value) {
            sleep(Duration(seconds: 1));
            print("111延迟后 value = $value");
             throw Exception("abc");//自定义异常
          }
  ).whenComplete(() => print("执行完毕1111")).then((value){
    sleep(Duration(seconds: 1));
    print("222延迟后 value = $value");
  }).whenComplete(() => print("执行完毕222")).catchError((e) {
    print("e = $e");
  });
  // 抛出异常的时候,可以用onError接收到抛出的异常 ,error是捕获的异常,stackTrace (可以忽略)栈跟踪显示你都调用了哪些方法,
  // // 当onError捕获异常的时候catchError就不会捕获异常




}
