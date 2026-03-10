main(){
    /*
    final
 final 修饰符。这可以防止来自当前库之外的类进行子类型化。禁止继承和实现都可以完全阻止子类型化。这保证了：

您可以安全地向 API 中添加增量更改。
您可以调用实例方法，确保它们尚未在第三方子类中被覆盖。
final 类可以在同一库中被扩展或实现。final 修饰符包含了 base 的效果，因此任何子类也必须标记为 base、final 或 sealed。

dart
     */
  var w1 = Woker();
  w1.run();
  w1.name;
}
final class Person{
  String name = "人类";
  run(){

  }
}
final class Woker extends Person{  //子类必须是 base、final 或 sealed

}
