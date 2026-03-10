/*
类型扩展
使用 implements 继承某个类,可以使用他下面所有方法和操作符
,也可以继承这个类的父类
*/

extension type IntId(int i) implements int{
    show(){
      print("i = $i");
    }
}
extension type ListR(List list) implements Iterable{ //可以继承父类,使用父类中的方法
// extension type ListR(List list) {//如果不继承Iterable ,无法调用map方法
//自定义方法
  removeAll() {
    list.removeRange(0, list.length); //删除从0到最后
  }
}

extension type Father(String str) {
  // Father(this.str);//重定义
  factory Father.a(String value) = Father; //工厂构造函数重定向
// Only factory constructor can specify '=' redirection 只有工厂构造函数可以重定向
  factory Father.b(String value) = Son; //重定向给了自己子类的命名构造函数,因为类型和参数都相同
  factory Father.c(String value) = Son.b;
}
extension type Son(String str) implements Father {
  // Son(this.str);//重定义
  Son.b(this.str);
}

main() {
  var id1 = IntId(100);
  var f1 = Father("abc");
  var f2 = Father.c("abc");

  var s1 = Son("bcd");
  var s2 = Son.b("123x");
  /*
  var l1 = IntId(100);
  l1 + 10;
  l1.show();
   */
  /*
  var list1 = ListR([1,2,3,4]);
  // list1.map((e) =>print("e = $e")).toList();
  list1.removeAll();

  print(list1.list);
  // print(list1.list);
   */
  /*

//普通的类演示工厂构造函数重定向
  A(100,"abc");
  A.withName("bbb");
  A.withName2("bbb");
  var o1 = A.withName3("cccc");
*/
}

//复习工厂构造函数
class A {
  int i;
  String name;

  // A(this.i,this.name);
  A(int i, String name)
      : i = i,
        name = name; //初始化列表的方法
  factory A.withName(String name) {
    // return A(100,name);
    return A.withName2(name);
  }

  factory A.withName2(String name) {
    return A(100, name);
  }

  factory A.withName3(String name) = A.withName2; //工厂构造方法的重定向
  factory A.b(int i , String name) = Ason;//重定向给了自己子类的命名构造函数,因为类型和参数都相同
}
class Ason extends A{
  Ason(super.i, super.name);
}