/*
  命名构造函数,在类名后面加点.方法名,是在创建对象的时候同时执行的方法
  调用方法的格式跟静态方法很像,都是类名.方法名 但是静态方法是不会创建对象的
  */
class Person {
  String name = "张三";
  int age = 22;
  double height = 170;

  Person(this.name, this.age, this.height);

  Person.setName(this.name);

  Person.setAge(this.age);
//下面代码,是以后flutter需要用到的json转模型
  Person.fromJson(Map json) {
    name = json["name"];
    age = json["age"];
    height = json["height"];
  }

  void showInfo() {
    print("name = $name age = $age height = $height");
  }
}

//通过对象.hashCode 的值判断是不是同一个对象
main() {
  var p1 = Person.setName("王五");
  print("p1 = ${p1.hashCode}"); //创建的不是一个对象因为hashcode不一样,说明对象不同
  p1 = Person.setName("王五");
  print("p1 = ${p1.hashCode}");
  int a = 100;
  int b = 100;
//数值类的hashCode,如果值相同,hashCode就相同,无法判断是同一个变量
  print("a.hashCode ${a.hashCode}  ");
  print("b.hashCode ${b.hashCode}  ");

  p1 = Person.setAge(100); //这里已经创建了第二个对象
  print("p1 = ${p1.hashCode}");
  p1.showInfo();

//下面代码,是以后flutter需要用到的json转模型
  var json = {
    "name":"天山童姥",
    "age":9999,
    "height":155
  };
  var p2 = Person.fromJson(json);
  p2.showInfo();
}
