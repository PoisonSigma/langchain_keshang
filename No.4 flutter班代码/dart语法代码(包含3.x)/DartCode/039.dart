//通过对象.hashCode 的值判断是不是同一个对象

class Person {
  String name = "张三";
  int age = 0;
  double height = 180.5;

  Person(this.name, this.age, this.height) {
    print("构造函数Person()执行");
  }

/*
  命名构造函数,在类名后面加点.方法名,是在创建对象的时候同时执行的方法
  调用方法的格式跟静态方法很像,都是类名.方法名 但是静态方法是不会创建对象的
  */
  Person.setName(this.name) {
    print("命名构造函数setName 执行 name = $name");
  }

  //对象自己的方法可以访问自己的属性
  showInfo() {
    print("name = $name age = $age  height = $height");
  }

//下面代码,是以后flutter需要用到的json转模型
  Person.fromJson(Map json) {
    name = json["name"];
    age = json["age"];
    height = json["height"];
  }
}

main() {
  //通过对象.hashCode 的值判断是不是同一个对象
  //   var p1 = Person("李四", 30, 180.5);
  //   print("p1.hashCode = ${p1.hashCode}");
  //   p1 = Person("李四", 30, 180.5);
  //   print("p1.hashCode = ${p1.hashCode}");

  // int a = 100;
  // print("a.hashCode = ${a.hashCode}");
  // int b = 100;
  // print("b.hashCode = ${b.hashCode}");
  //
  // String str1 = "abc";
  // print("str1.hashCode = ${str1.hashCode}");
  // String str2 = "abc";
  // print("str2.hashCode = ${str2.hashCode}");
  // var p2 = Person.setName("李四");

  // p2.showInfo();

  var json = {
    "name":"天山童姥",
    "age":9999,
    "height":155.0
  };

  var p3 = Person.fromJson(json);

  p3.showInfo();
  p3.name;
  p3.age;
  p3.height;
  // var str = json["name"];
  var str = p3.name;
  print(p3.name);

}
