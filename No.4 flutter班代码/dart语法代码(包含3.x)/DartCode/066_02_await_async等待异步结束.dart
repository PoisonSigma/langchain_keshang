/*
await是等待 Future里面的异步操作结束, 返回的是return的值,会阻塞线程,等待执行完以后才向下执行
async函数会返回Future
 */
main() async {
      print("start");
      /*
         var r1 = await Future.delayed(Duration(seconds: 1),(){
        print("1111");
        return "abc";
      });
         print("r1 = $r1");

       */
      /*
      var f1 = getData1();
      f1.then((value) => print("222 = $value"));
       */
      /*
      var f1 =await getData1();
      print("f1 = $f1");

       */
      fun3();
      print("end");
}

//async函数返回类型是Future
//会返回Future
Future<String> getData1() async {
  print("进入getData1");
  /*
  var  f1 = Future.delayed(Duration(seconds: 1),(){
    return "网络数据1";
  }).then((value) => print(value));
   */
  var  f1 = await Future.delayed(Duration(seconds: 1),(){
    return "网络数据1";
  });
  print("退出getData1");
  return f1;  //函数的return的类型,是aysnc函数的 Future的限定类型
}

fun3() async {
  print("fun3");
  var f1 =await fun2();
  print("f1= $f1");
}
fun2() async {
  var f1 =await getData1();
}