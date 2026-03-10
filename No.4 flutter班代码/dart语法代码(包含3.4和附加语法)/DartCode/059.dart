//常量构造函数不能用函数体
//调用const的构造函数可以省略const,但是省略const以后,相同成员变量创建的对象存储空间就不一样了
class Person {
  final int a;
  static const str = "abc";
  const Person(this.a);

  // Person(this.a);
  /*
  const Person(this.a){//常量构造函数不能用函数体

  }
   */
  /*
   const Person.setA(this.a){//常量构造函数不能用函数体

   }
   */
}

main() {
  print(Person.str);
  const Person(100);
  // var p1 =const  Person(1);
  // var p2 =const  Person(1);
  // print(p1.hashCode);
  // print(p2.hashCode);
  // var result = identical(p1,p2);
  // print(result);

  //List也是如果有const就是相同地址,如果省略const,那么就不是相同地址
  // var l1 = [1, 2, 3];
  // var l2 = [1, 2, 3];
  // print(l1.hashCode);
  // print(l2.hashCode);
  // var result = identical(l1, l2);
  // print(result);
}
