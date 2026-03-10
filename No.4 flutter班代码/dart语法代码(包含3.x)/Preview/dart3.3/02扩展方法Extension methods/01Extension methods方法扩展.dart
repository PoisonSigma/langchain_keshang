import 'StringA.dart'; //导入自己写的扩展方法的文件

main() {
  int a1 = int.parse("123");
  print(a1);
  print("123".length); //调用String的方法
  int a = "123".parseInt(); //调用自定义的扩展方法

  print(a.runtimeType);
  print(a);

  // 您不能在动态类型的变量上调用扩展方法。例如，以下代码会导致运行时异常：

  dynamic d1 = "123"; //动态类型不能调用扩展方法
  // print(d1.parseInt()); // 运行时异常：NoSuchMethodError
  //类型推断可以调用扩展方法
  var v1 = '123';
  print(v1.parseInt()); //正常运行, 这里的var是静态解析的,鼠标放在这里可以看到类型已经推断成String了
  // 动态类型不起作用的原因是扩展方法针对接收器的静态类型进行解析。由于扩展方法是静态解析的，因此它们的速度与调用静态函数一样快。
  StringA.name = "静态字段赋值";

  print("1234567".id); //调用getter
  "1234567".id = 456; //调用setter
  print(StringA.name);
  //每个扩展方法都能修改静态成员,因为静态成员是属于这个类型String的,可以理解为,是这个类的,不是某个对象的.
  "abc".id = 123;
  print(StringA.name);
}
