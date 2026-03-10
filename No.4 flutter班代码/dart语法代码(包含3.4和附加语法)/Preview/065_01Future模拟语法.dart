import 'dart:async';
import 'dart:io';
main(){
  print("start");

  AOr(add);
  // A(add );//抽象类不能被创建对象

  print("end");
}

void add(){
  sleep(Duration(seconds: 2));
  print("add()方法");
}
abstract class A {
  factory A(Function fn ) {
    // return Son();
    return AOr(fn);
  }


}

class AOr implements A {
  AOr(Function fn ){
    // print("SonA start ===");
    Timer(Duration(seconds: 2),(){//延迟2秒
      fn();
    });
    Timer.run((){
      fn();
    });
    // print("SonA end =====");
  }
}
