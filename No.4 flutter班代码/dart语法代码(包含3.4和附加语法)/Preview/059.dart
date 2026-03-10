//常量构造函数不能用函数体
//调用const的构造函数可以省略const,但是省略const以后,相同成员变量创建的对象存储空间就不一样了

class Person {
  final int a;
  const Person(this.a);
  const Person.setA(this.a);
  // const Person.setA(this.a){  //错误,常量构造函数不能有函数体
  //
  // }
}

main() {
  var p1 = const Person(1);
  var p2 = const Person(1);
  var p3 = Person(1); //省略了const,但是创建的对象也不是之前的

  var result = identical(p1, p2);
  result = identical(p1, p3);
  print("result = $result");

  //List也是如果有const就是相同地址,如果省略const,那么就不是相同地址
  var l1 = const [1, 2, 3, 4, 5];
  var l2 = const [1, 2, 3, 4, 5];
  result = identical(l1, l2);
  print("result = $result");
}
