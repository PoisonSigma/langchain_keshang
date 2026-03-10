import "18a.dart";

main() {
  /*
      var r1 =  Runnable();
      r1.run();

      var b1 = B();
      b1.run();

      var d1 = D();
      d1.pause();
      var e1 = E();
      e1.stop();

   */
  var l1 = [Cell1(), Cell2(), Cell1(), Cell1()];
  l1.map((e) => e.Text()).toList();
}

showText(Textable cell) {
  cell.Text();
}

// class A extends Runnable{  //库之外,不能extends继承
// }
class B implements Runnable {
  //库之外可以实现
  @override
  void run() {
    print("B 运行");
  }
}

// class C extends Pausable{  //不能extends
// }
class D implements Pausable {
  @override
  void pause() {
    print("D 的暂停");
  }
}

class E implements Stoppable {
  @override
  void stop() {
    // TODO: implement stop
    print("E 停止");
  }
}

//可以实现多个接口
class F implements Runnable, Stoppable, Pausable {
  @override
  void pause() {
    // TODO: implement pause
  }

  @override
  void run() {
    // TODO: implement run
  }

  @override
  void stop() {
    // TODO: implement stop
  }
}

class Cell1 implements Textable, Runnable, Stoppable {
  @override
  void Text() {
    // TODO: implement Text
    print("Cell1 的文本");
  }

  @override
  void run() {
    // TODO: implement run
    // super.run();//报错,注意implements实现的方法不能调用父类中的方法,编译器会把普通方法也当做抽象方法
  }

  @override
  void stop() {
    // TODO: implement stop
  }
}

class Cell2 implements Textable, Pausable {
  @override
  void Text() {
    // TODO: implement Text
    print("Cell2 的文本");

  }

  @override
  void pause() {
    // TODO: implement pause
  }
}
