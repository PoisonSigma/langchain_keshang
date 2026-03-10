import '043b.dart';
// dart中定义私有成员和属性不是用的private 或者 protected 受保护的关键字,而是用下_划线开头
// 在同一个文件下,_开头的对象的私有方法和私有成员可以被访问
// 不在同一个文件下,import引入进来的不能访问_开头的私有成员
// 使用普通方法访问私有方法和私有成员变量
class Person043a {
  String name = "张三";
  int age = 22;
  double height = 170;
   int _id = 123;
  void _showInfo() {
    print("name = $name age = $age height = $height id = $_id");
  }

}

main(){
  var p1 = Person043a();
  p1._id = 124;//在同一个文件下,_开头的对象的私有方法和私有成员可以被访问
  p1._showInfo();

  var p2 = Person043b();
  // p2._id;//不在同一个文件下,import引入进来的不能访问_开头的私有成员
  // p2._showInfo();
  p2.age;//可以访问普通的成员
  p2.SetId = 99; //用set方法给赋值
  p2.showPrivate();//使用普通方法访问私有方法和私有成员变量
  print("id=${ p2.getId}");
}