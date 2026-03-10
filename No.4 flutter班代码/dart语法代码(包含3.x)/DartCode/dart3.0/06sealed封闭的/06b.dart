import '06a_sealed封闭的.dart';
//文件外,不能继承sealed类型的class
// class Car extends Vehicle{
// }
// class Truck extends Vehicle{
// }
// class Bicycle extends Vehicle{
// }
//sealed的子类,可以被继承
class Byd extends Car{
}
//final class也不能在文件外被继承

// final class C extends B{
// }
