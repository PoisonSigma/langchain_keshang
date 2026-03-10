//dart中的setter和getter是通过关键字set和 get实现的
// set 方法是调用的时候像调用普通变量那样给方法赋值.
// get方法是像普通变量那样获取值
// 从调用的地方来看,感觉像是调用2个变量,而不是2个方法
// set方法因为需要复制,所以定义的时候要有()传入值,get方法没有()传入的形参,只有返回值
class Person {
  String name = "张三";
  int age = 22;
  double height = 170;
  int year = 0;
  int _a = 0;

  set set_a(int _a){
    this._a = _a;
  }
  void showInfo() {
    print("name = $name age = $age height = $height _a = $_a");
  }

  set changeAge(int age) {
    print("set方法 changeAge执行");
    this.age = age;
    year = 2023 - age;
  }
  // set age{//报错,因为age已经是成员变量名了
  set setAge(int age){
    print("set方法 setAge执行");
    this.age = age;
  }
  get cardId{
      return "110 101 $year 0102 0001";
  }
}

main() {
  var p1 = Person();
  p1.changeAge = 18; //set方法,等号在右边,是给方法赋值. 调用的时候不需要用 (),而是像赋值操作那样
  p1.showInfo();
  String id = p1.cardId as String;//这个是get方法,因为等号在左边,是从get方法中获取值
  print(id);
}
