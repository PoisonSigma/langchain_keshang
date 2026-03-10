/*
原生的 dart http请求  ,不讲了
逛网的 http库,不讲了
dio 国人自己写的库,用的最多
 */
import 'dart:io';

main() async {
  print("start");
/*
  Future((){
    sleep(Duration(seconds: 2));
    print("并行..");
    return "彭于晏二楼请";
    // return 123;
  }).then((value)=>print("value = $value"));

 */
  /*
  Future((){

    return "abc";
    // return 123;
  }).then((value){
    print("value = $value");
  });

   */
  /*
  Future.value("abc").then((value){
    print("value = $value");
  });

   */

  /*
  Future((){
    sleep(Duration(seconds: 2));
    print("并行..");
    return "彭于晏二楼请";
    // return 123;
  });

   */
  /*
  Future.delayed(Duration(seconds: 2),(){
    print("并行..");
    return "彭于晏二楼请";
  }).then((value){
    print("value = $value");
  });
   */
  /*
  Future(() {
    print("并行..");
    /*
    try {
      throw Exception("自定义异常123");
    }catch(e){
      print("e = $e");
    }

     */
    throw Exception("自定义异常123");
    return "彭于晏二楼请";
    // return 123;
  })
      .then((value) => print(
          "value = $value")) //注意throw抛出异常以后一定要接一个then否则 catchError 捕获了还是会报红字异常
      .whenComplete(() => print("执行结束aaaa"))
      .catchError((e) {
    print("e123 = $e");
  }).whenComplete(() => print("执行结束bbbb"));


   */

   var result = await Future((){
    sleep(Duration(seconds: 2));
    print("并行..");
    // return "彭于晏二楼请";
    return 123;
  });
  print("end");
   var result2 = getData();
  var result3 =  await fun2();
}
//
// Future<Null> getData() async{
//     // return 123;
// }

//异步函数,返回的类型,一定是Future类型
Future<int> getData() async{
    return 123;
}
fun2() async {
  await getData();
}