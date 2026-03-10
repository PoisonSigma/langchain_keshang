// 连续2个点..是级联操作符,作用是把一个对象下面的方法或者成员连续使用出来.
// 级联操作返回的是对象
// 第一行的对象结尾不能加分号,最后一个成员或者方法结束再加分号,本质上是一行代码

class Person {
  String name = "张三";
  int age = 18;

  showInfo() {
    print("name = $name age = $age");
  }

  action() {
    print("action()执行 人类做了动作");
  }
}

main() {
  // var p1 = Person();
  // p1.action();
  // p1.showInfo();
  //级联操作符返回的是对象本身,返回..级联操作符左边的对象

  // var p1 = Person();
  // print("p1.hashCode = ${p1.hashCode}");
  // var result = p1..action();
  // print("result.hashCode = ${result.hashCode}");

  //下面是不换行让大家看到级联操作的本质是一条语句,换行是为了看起来格式好看
  // p1..action()..age = 30..showInfo();
  // p1..action()
  //   ..age = 30
  //   ..showInfo();

  //错误例子,中间有分号
  // p1..action()
  //   ..age = 30
  //   ..showInfo();

  //推荐使用
  var p2 = Person() //先执行赋值符号右边的操作,再把整体对象返回给p2
    ..age = 30
    ..showInfo();

}
