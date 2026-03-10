import 'dart:io';

main() {
  print("start");
  /*
      var f1 = Future((){
        return "abc";
      });
      f1.then((value) => print(value));
      //Future.value直接return值
    var f2 = Future.value("abc");
      f2.then((value) => print(value));

      var f3 = Future(() {
        sleep(Duration(seconds: 2));
        print("f3");
      });
      //delayed 延迟几秒执行
      Future.delayed(Duration(seconds: 4),(){
        print("f4");
      });
*/
  ////whenComplete是抛出异常也会执行的代码,如果不抛出异常,那么就会按照顺序执行,whenComplete放在哪里就在哪里执行,放在中间和结尾都行
  // 抛出异常的时候,可以用onError接收到抛出的异常 ,error是捕获的异常,stackTrace (可以忽略)栈跟踪显示你都调用了哪些方法,
  // // 当onError捕获异常的时候catchError就不会捕获异常
  Future.value("abc").then((value){
    sleep(Duration(seconds: 2));
    print("value = $value");
    /*
    try {
      throw Exception("自定义异常1");
    }catch(e){
      print("e = $e");
    }
     */
    throw Exception("自定义异常1");
  }
  ).whenComplete(() => print("执行完毕1111"))
      .then((value) => print("value22222 = $value "))////抛出异常以后直接用onError 或 catchError 虽然会捕获异常,但是还是会崩溃,在异常后面加.then可以解决崩溃问题
    .whenComplete(() => print("执行完毕22222"))
      .onError((error, stackTrace)
  {
  print("error = $error stackTrace = $stackTrace");
  }).  catchError((e) {
  print("e = $e");
  });

  print("end");
}
