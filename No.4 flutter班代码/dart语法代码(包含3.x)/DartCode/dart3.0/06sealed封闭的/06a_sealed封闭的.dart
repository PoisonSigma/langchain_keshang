/*
sealed

为了创建一个已知的可枚举子类型集合，您需要使用 sealed 修饰符。这使您能够创建一个对所有这些子类型的 switch 语句，而该语句在编译时被确定为穷举的。

sealed 修饰符阻止一个类在其自身库之外被扩展或实现。密封类是隐式抽象的。

它们不能自己被实例化。
它们可以有工厂构造函数。
它们可以为它们的子类定义构造函数。
然而，密封类的子类不是隐式抽象的。

编译器知道所有可能的直接子类型，因为它们只能在同一个库中存在。这允许编译器在 switch 语句的 case 中没有穷举所有可能的子类型时发出警告：
如果你不想进行详尽的切换，或者希望在添加子类型时不会破坏 API，可以使用 final 修饰符。要深入了解 sealed 和 final 的比较，请阅读 sealed 与 final 的比较。


 */
main(){
   // Vehicle();//sealed不能直接创建对象
  // Car();//sealed子类可以创建对象
  // var sound = getVehicleSound(Car());
  var sound = getVehicleSound(Truck());
  print(sound);

}
String getVehicleSound(Vehicle v1){
    return switch(v1){
    Car()=>'vroom',
    Truck()=>'vrooooom',
    Bicycle()=>'ringring',
    // Vehicle()=>""
    // _=>"默认的"
    };
}
//交通工具 类有3个子类,小汽车, 卡车,自行车
 sealed class Vehicle{
}
class Car extends Vehicle{
}
class Truck extends Vehicle{
}
class Bicycle extends Vehicle{
}
final class A{
}
// class B1 extends A{ //普通class不能继承final class
//
// }
final class B extends A{
}
/*
sealed 和 final 的区别
如果你有一个你不希望用户能够直接创建子类型的类，那么在什么情况下应该使用 sealed 而不是 final？有一些简单的规则：

如果你希望用户能够直接构造类的实例，那么不能使用 sealed，因为 sealed 类型是隐式抽象的。

如果你的库中的类没有子类型，那么使用 sealed 就没有意义，因为你无法获得详尽性检查的好处。

否则，如果该类有一些你定义的子类型，那么 sealed 可能是你想要的。如果用户看到该类有一些子类型，能够方便地将它们作为 switch 语句的不同情况处理，并让编译器知道整个类型都被覆盖。

使用 sealed 意味着如果你以后在库中添加了另一个子类型，那么这将是一个破坏性的 API 更改。当出现新的子类型时，所有那些现有的 switch 语句都变得不穷尽，因为它们没有处理新类型。这与向枚举添加新值完全相同。

这些不穷尽的 switch 编译错误对用户很有用，因为它们引起用户注意，让他们知道他们的代码中需要处理新类型的地方。

但这也意味着每当你添加一个新的子类型时，都是一个破坏性的更改。如果你希望在不破坏的情况下添加新的子类型，那么最好使用 final 来标记超类型而不是 sealed。这意味着当用户对该超类型的值进行 switch 时，即使他们已经为所有子类型添加了情况，编译器也会强制它们添加另一个默认情况。如果以后添加更多的子类型，将执行该默认情况。
- 使用 final 完全防止类被扩展。
- 使用 sealed 选择在一组子类型上进行穷尽性检查。

 */