import 'dart:async';
import 'dart:io';

main() {
  // A();//实例化一个抽象类的名字,实际是创建的子类的,非抽象类的对象
  print("start");
  // Timer(Duration(seconds: 0),(){
  /*
    Timer.run((){
      getData();
    });

     */
  /*
    A(getData);
    print("end");
    A((){
      print("网络数据结束2222");
    });

     */

  /*
  Future(() {
    print("网络数据结束3333");
    return "abc";
  }).then((value) {
    print("value = $value");
    return 123;
  }
  ).then((value) => print("value = $value"));

   */

/*

  var future1 =  A((){
    sleep(Duration(seconds: 2));
    print("网络请求结束111");
  }).then((){
    sleep(Duration(seconds: 1));
    print("1111");
    return "xxxx1111";
  }).then((){
    sleep(Duration(seconds: 1));
    print("2222");
    return "xxxx2222";
  });
  */

  /*
  var future2 = Future((){
    sleep(Duration(seconds: 2));
    print("网络请求结束111");
    return "第一次的请求结果";
  });
  future2.then((value) => print("value = $value"));
*/
  var future3 = Future((){
    sleep(Duration(seconds: 2));
    print("网络请求结束111");
    return "第一次的请求结果";
    /*
    var fn1 =  (){
      print("abc");
      return "abc";
    };

    return  fn1 ;


  }).then((value) =>  print("value = ${value()}"));

     */
  }).then((value) =>  "abc").then((value)=>print("value = ${value}"));


  print("end");
}

getData() {
  sleep(Duration(seconds: 2));
  print("网络请求结束");
  return "abcdef";
}

abstract class A {
  // factory A.a(){
  //   return SonA();
  // }
  factory A(Function fn){
    return _A(fn);
  }

  A then(Function fn);
}
// class SonA extends A{
//
// }
class _A implements A {
  _A(Function fn) {
    Timer.run(() {
      fn();
    });
  }

  @override
  A then(Function fn) {
    // TODO: implement then
    Timer.run(() {
      fn();
    });

    return  this;
  }
}
