/*
运算符重载关键字是 operator 加一个运算符
右边的()里面是传入的时候 运算符右边的对象
不是所有运算符都能被用户重载,例如 ++
 */
class Person {
  String name;
  int age;
  Person(this.name, this.age);
  bool operator >(Person other) {
    return age > other.age ? true : false;
  }

  bool operator <(Person other) {
    return age < other.age ? true : false;
  }

  // bool operator ==(Object other) => identical(this, other);//这个是dart sdk自带的实现代码
  // bool operator==(Person ps){// 报错,没有重写 Object 类里面的 == 运算符

  bool operator ==(Object other) {
    if (other is Person) {
      print("other = $other");
      return name == other.name ? true : false;
    } else {
      print("other = $other");
      return false;
    }
  }
//不是所有操作符都可以重载
  // operator ++(Person p1){ //不能重载,报错:The string '++' isn't a user-definable operator.
  // operator ++(Person p1){
  //
  // }

//双目运算符,左移,我们把 当前对象的age 和<<右边的age相加保存当当前对象的age
  operator << (Person other){
    age += other.age;
    print("age =$age");
  }
}

main() {
  var p1 = Person("张三", 18);
  var p2 = Person("张三", 19);
  //
  // print(p1>p2);
  // print(p1<p2);
  // print(p1 == p2);
  p1 << p2;
  print("p1.age = ${p1.age}");
}
