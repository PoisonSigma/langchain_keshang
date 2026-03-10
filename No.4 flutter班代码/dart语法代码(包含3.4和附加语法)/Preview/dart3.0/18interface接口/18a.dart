main(){
  /*
    为了定义一个接口，使用 interface 修饰符。在接口的定义库之外的库中可以实现该接口，但不能扩展它。这保证了：
1.可以实例化
2.当前库之外不能被extends继承
3.可以被implements实现多个接口

     */
}
interface class Runnable{
  void run(){
    print("Runnable 接口run方法运行");
  }
}
//抽象接口定义抽象方法
abstract interface class Stoppable{
  void stop();
}
//普通接口,定义外部external方法
interface class Pausable{
  external void pause();  //子类 extends 可以重写,也可以不重写 . 子类 implements必须实现重写 .. interface子类不能extends,所以只能 implements 实现
}



class A extends Runnable{ //本文件下,可以extends继承,库之外不可以extends
}
class B implements Runnable{
  @override
  void run() {
    print("B 运行");
  }
}
abstract interface class Textable{
  void Text();
}
