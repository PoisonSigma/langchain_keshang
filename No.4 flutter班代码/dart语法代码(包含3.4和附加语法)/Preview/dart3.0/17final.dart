/*
final
 final 修饰符。这可以防止来自当前库之外的类进行子类型化。禁止继承和实现都可以完全阻止子类型化。这保证了：

您可以安全地向 API 中添加增量更改。
您可以调用实例方法，确保它们尚未在第三方子类中被覆盖。
final 类可以在同一库中被扩展或实现。final 修饰符包含了 base 的效果，因此任何子类也必须标记为 base、final 或 sealed。

dart

 */
main(){

}
class A17{ //无修饰符的普通类,为了试验普通类可以在类外被继承
}
final class Person17{
      move(){

      }
}

// class Worker extends Person{//报错
// }
// final 修饰符包含了 base 的效果，因此任何子类也必须标记为 base、final 或 sealed。
base class A extends Person17{
}
final class B extends Person17{
}
sealed class C extends Person17{
}