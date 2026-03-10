import 'dart:math';

main() {
  // 常量模式在值等于常量时匹配：
//123、null、'string'、math.pi、SomeClass.constant、const Person(1, 2)、const (1 + 2)
// 例如我们在空检查里面无法匹配到null,但是常量模式可以匹配null
//可以作为常量模式的格式有:
// 数字字面量123、45.56
// 布尔字面量true
// 字符串字面量 'string'
// 命名常量  例如数学库里的常量  math.pi、double.infinity
// 常量构造函数 const Point(0, 0)
// 常量集合字面量   例如List const []、  集合 const {1, 2}
// 更复杂的常量表达式必须用括号括起来，并加上 const 前缀const (1 + 2)
// int? a = 1;
// int? a = null;
//   int? a = 3;
  int? a = 10000;
  constPattern(a);
  /*
  var p1 =const Person("张三");
  var p2 =const Person("张三");
  var p3 = Person("张三");
  print(p1.hashCode);
  print(p2.hashCode);
  print(p3.hashCode);
  constClass(p1);

   */
}

constPattern(int? r) {
  switch (r) {
    case 1:
      print("1");
    // case var s?:
    //   print("s = $s");
    case null:
      print("null");
    case const (1 + 2):
      print("1+2");
    case Person.id:
      print(" Person.id");
  }
}
constClass(Person? p){
  switch(p){
    case const Person("张三"):
      print("常量构造函数");
  }
}

class Person {
  static const int id = 10000;
  final String name;

  const Person(this.name);
}
