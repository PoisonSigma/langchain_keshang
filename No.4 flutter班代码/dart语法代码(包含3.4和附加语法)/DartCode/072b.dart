/*
版本说明：增强enums要求语言版本至少为2.17。
声明增强enums
Dart还允许enum声明声明具有字段、方法和const构造函数的类，这些类仅限于固定数量的已知常量实例。

要声明增强enum，请遵循与普通类类似的语法，但有一些额外的要求：

实例变量必须是final，包括mixin添加的变量。
所有生成的构造函数必须是const。
工厂构造函数只能返回固定、已知的enum实例之一。
不能扩展其他类，因为Enum会自动扩展。
不能为索引、hashCode、等值运算符==进行覆盖。
在enum中不能声明名为values的成员，因为它会与自动生成的静态values getter冲突。
所有enum的实例必须在声明的开始处声明，并且必须至少声明一个实例。
在增强enum中的实例方法可以使用this引用当前的enum值。
以下是一个声明具有多个实例、实例变量、getter和实现接口的增强enum的示例：
 */

enum Person{
  child(tall:100,weight:50),
  women(tall:160,weight:90),
  man(tall:180,weight:100);
  final int tall;
  final int weight;
  const  Person({required this.tall , required this.weight});//要求是常量构造函数
}

main(){
  // print(Person.child);
  // print(Person.child.tall);
  // print(Person.child.index);
  var l1 = Person.values;
  print(l1);
}