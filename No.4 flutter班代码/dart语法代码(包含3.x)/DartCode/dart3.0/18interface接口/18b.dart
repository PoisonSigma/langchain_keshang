import "18a.dart";
main(){

      var l1 = [B(),C(),D(),D2()];
      // l1.map((e) => e.getText()).toList();
      for(var item in l1){
          item.getText();
      }
}
/*
class A extends Textable{  //在接口类所在的库之外,不能被 extends继承
  @override
  getText() {
    // TODO: implement getText
    print("A 的文本");
  }
}

 */
//接口所在类之外可以implements实现多个接口
class B implements Textable , Runnable{
  @override
  getText() {
    // TODO: implement getText
    print("B 的文本");
  }

  @override
  run() {
    // TODO: implement run
    print("B 运行");
  }

}
class C implements Textable{
  @override
  getText() {
    // TODO: implement getText
    print("C 的文本显示");
  }
}
class D implements Textable{
  @override
  getText() {
    // TODO: implement getText
    print("D 的文本显示");
  }
}
/*
class D1 extends D{ //库之外不能extends
}
 */
class D2 implements D{
  @override
  d() {
    // TODO: implement d
    print("d执行");
  }

  @override
  getText() {
    // TODO: implement getText
    print("D2 的文本");
  }
}