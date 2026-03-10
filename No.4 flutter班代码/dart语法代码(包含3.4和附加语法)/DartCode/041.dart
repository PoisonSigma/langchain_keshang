//dart中的setter和getter是通过关键字set和 get实现的
// set 方法是调用的时候像调用普通变量那样给方法赋值.
// get方法是像普通变量那样获取值
// 从调用的地方来看,感觉像是调用2个变量,而不是2个方法
// set方法因为需要复制,所以定义的时候要有()传入值,get方法没有()传入的形参,只有返回值
//系统默认给属性设置了setter和getter用来赋值和读取值,私有属性,不能通过默认的setter和getter读取值和赋值,但是可以通过自定义的setter和getter赋值
class Person {
  String name = "张三";
  int age = 22;
  double height = 170;
  int year = 0;
  int _a = 0;
  void showInfo() {
    print("name = $name age = $age height = $height year = $year _a = $_a");
  }

  set setAge(int a){

  }
  set changeAge(int age) {
    this.age = age;
    year = 2023 - age;
    print("set 方法执行 changeAge执行");
  }
  get cardId{
    return "110101${year}01020001";
  }
}

main() {
  var p1 = Person();
  p1.changeAge = 18;
  p1.setAge = 100;
  p1._a = 100;
  p1.age = 200;
  p1.showInfo();

  String str = p1.cardId;

  print("str=$str");
}
