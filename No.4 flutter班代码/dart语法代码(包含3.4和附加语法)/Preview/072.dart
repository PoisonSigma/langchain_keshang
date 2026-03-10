/*
枚举类型
枚举类型，通常称为枚举或enums，是一种特殊的类，用于表示一组固定数量的常量值。

注意：所有的enums都自动扩展Enum类。它们也是封闭的，意味着它们不能被子类化、实现、混合或以其他方式显式实例化。

抽象类和mixin可以显式实现或扩展Enum，但除非它们被enum声明实现或混入，否则没有对象可以实际实现该类或mixin的类型。

声明简单enums
要声明简单的枚举类型，请使用enum关键字并列出要枚举的值：

dart
Copy code
enum Color { red, green, blue }
提示：在声明枚举类型时，您还可以使用尾随逗号以帮助防止复制粘贴错误。

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

dart
Copy code
enum Vehicle implements Comparable<Vehicle> {
  car(tires: 4, passengers: 5, carbonPerKilometer: 400),
  bus(tires: 6, passengers: 50, carbonPerKilometer: 800),
  bicycle(tires: 2, passengers: 1, carbonPerKilometer: 0);

  const Vehicle({
    required this.tires,
    required this.passengers,
    required this.carbonPerKilometer,
  });

  final int tires;
  final int passengers;
  final int carbonPerKilometer;

  int get carbonFootprint => (carbonPerKilometer / passengers).round();

  bool get isTwoWheeled => this == Vehicle.bicycle;

  @override
  int compareTo(Vehicle other) => carbonFootprint - other.carbonFootprint;
}
版本说明：增强enums要求语言版本至少为2.17。

使用enums
像访问任何其他静态变量一样访问枚举值：

dart
Copy code
final favoriteColor = Color.blue;
if (favoriteColor == Color.blue) {
  print('Your favorite color is blue!');
}
枚举中的每个值都有一个索引getter，它返回该值在enum声明中的从零开始的位置。例如，第一个值的索引为0，第二个值的索引为1。

dart
Copy code
assert(Color.red.index == 0);
assert(Color.green.index == 1);
assert(Color.blue.index == 2);
要获取所有枚举值的列表，请使用enum的values常量。

dart
Copy code
List<Color> colors = Color.values;
assert(colors[2] == Color.blue);
您可以在switch语句中使用enums，并且如果您未处理所有enums的值，将收到警告：

dart
Copy code
var aColor = Color.blue;

switch (aColor) {
  case Color.red:
    print('Red as roses!');
  case Color.green:
    print('Green as grass!');
  default: // 没有此项，您将看到一个警告。
    print(aColor); // 'Color.blue'
}
如果需要访问枚举值的名称，例如从Color.blue获取'blue'，请使用.name属性：

dart
Copy code
print(Color.blue.name); // 'blue'
您可以像在普通对象上一样访问枚举值的成员：

dart
Copy code
print(Vehicle.car.carbonFootprint);
 */