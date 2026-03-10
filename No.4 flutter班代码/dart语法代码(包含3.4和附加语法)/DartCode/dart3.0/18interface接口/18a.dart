main(){
  /*
    为了定义一个接口，使用 interface 修饰符。在接口的定义库之外的库中可以实现该接口，但不能扩展它。这保证了：
1.可以实例化
2.在当前库之外不能被extends继承,本库中可以
3.可以被implements实现多个接口
     */
  /*
  var t1 = Textable();
  t1.getText();
  var a1 = A();
  a1.getText();

   */
  var b1 = B();
  b1.run();
  b1.getText();
}
interface class Textable{
     getText(){
        print("接口中的 Text执行");
     }
}
abstract interface class Drawable{ //抽象接口,可以不写方法体
  draw();
}
class C extends Drawable{
  @override
  draw() {
    // TODO: implement draw
  }
}
//普通接口里面写external外部方法
interface class D {
 external  d();//外部方法,可以在普通类中不写方法体
}
class D1 extends D{
}
class D2 implements D{
  @override
  d() {
    // TODO: implement d
    print("d执行");
  }
  
}

interface class Runnable{
   run(){
     print("接口中的 运行");
   }
}
class A extends Textable{
  @override
  getText() {
    // TODO: implement getText
    print("A 的文本");
  }
}
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