/*
运算符重载关键字是 operator 加一个运算符
右边的()里面是传入的时候 运算符右边的对象
不是所有运算符都能被用户重载,例如 ++

 */

//在类中的操作符重载
class Person {
  String name;
  int age;

  Person(this.name, this.age);

  bool operator >(Person p1) {
    //如果当前对象的age 大于 >右边传入的 age,就返回真.
    return this.age > p1.age ? true : false;
  }

  bool operator <(Person p1) {
    //如果当前对象的age 大于 >右边传入的 age,就返回真.
    return this.age < p1.age ? true : false;
  }
  //自定义一个年龄相加的
   int operator + (Person p1){
     return this.age + p1.age;
  }

  //双目运算符,左移,我们把 当前对象的age 和<<右边的age相加保存当当前对象的age
  operator << (Person p1){
   this.age = this.age + p1.age;
    print("age = ${this.age}");
  }

  //不是所有操作符都可以重载
  // operator ++(Person p1){ //不能重载,报错:The string '++' isn't a user-definable operator.
  // }

  // bool operator ==(Object other) => identical(this, other);//这个是dart sdk自带的实现代码
  // bool operator==(Person ps){// 报错,没有重写 Object 类里面的 == 运算符
  //注意,下面的==运算符 再Object类里面已经有了,所以必须重写跟他参数一样的
  bool operator ==(Object other) {
    //重写了Object类的 == 运算符
    if (other is Person) {
      //is运算符判断是否是 Person类型,如果是的话,other就会自动转换成Person类型,可以调用Person的成员
      print("other=$other");
      //如果name相同,那么就返回ture,否则返回false
      return this.name == other.name ? true : false;
    } else {
      //如果不是Person类型直接放回false
      return false;
    }
  }

}


main() {
  var p1 = Person("张三",20);
  var p2 = Person("张三2",19);
  print(p1 == p2);
  print(p1>p2);
  print(p1<p2);

  p1<<p2;

}
