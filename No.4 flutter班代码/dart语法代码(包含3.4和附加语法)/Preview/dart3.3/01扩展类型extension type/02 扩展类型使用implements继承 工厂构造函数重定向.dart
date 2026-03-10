/*
类型扩展
使用 implements 继承某个类,可以使用他下面所有方法和操作符
,也可以继承这个类的父类
 */
extension type IntId5(int i) implements int {
// 'IntId5' 可以调用 'int' 的所有成员，
// 以及它在此处声明的任何其他内容。
}

//implements可以继承底层类型的父类,
// 底层类型是 List,但是继承的是List的父类 Iterable
//implements Iterable<T>
extension type ListR<T>(List<T> list) implements Iterable {
// extension type ListR<T>(List<T> list) { //如果不继承Iterable ,无法调用map方法
//自定义方法
  RemoveAll() {
    list.removeRange(0, list.length); //删除从0到最后
  }
}

//复习工厂构造函数和重定向
class A {
  int i;
  String name;

  A(this.i, this.name); //私有的命名构造函数
  // factory A.withA(this.i,this.name){  //注意工厂构造函数中不能使用 形参初始化
  factory A.withName(String name) {
    return A(0, name);
  }
  factory A.a(String name) = A.withName;//工厂构造函数重定向
  factory A.b(int i ,String name ) = ASon;//父类重定向子类的构造函数
}
class ASon extends A{
  ASon(super.i, super.name);



}
class B {
  int i;
  String name;

  B._init(this.i, this.name); //私有的命名构造函数
// factory A.withA(this.i,this.name){  //注意工厂构造函数中不能使用 形参初始化
//普通的类不能使用 = 赋值,把一个类的构造函数赋值给另一个类
// factory B.withName(String name) = A.withName(String name); //注意看普通的类,无法把一个类的构造函数赋值给另一个类
}

//下面这段是复习 子类继承父类,构造函数后面的冒号初始化列表的内容

class Father<T> {
  T str;

  Father(this.str);
}

class Son<T> extends Father<T> {
  // Son(super.str,this.age);
  int age;

  // Son(String str,this.age):super(str);//在构造函数
  Son(T str, int age)
      : age = age,
        super(str); //这个等价于上面
}

// 工厂构造函数重定向 ,使用 =等号
// 另一个在相同表示类型上有效的扩展类型。这使您可以在多个扩展类型之间重用操作
// Only factory constructor can specify '=' redirection 只有工厂构造函数可以重定向
extension type Father2(String str) {
  factory Father2.str(String str2) = Father2; //重定向给自己系统自动生成的未命名构造函数
  factory Father2.str2(String str) = SonStr.a;//重定向给了自己子类的命名构造函数,因为类型和参数都相同
  //这里相当于 Father2.str(String str) =  SonStr(this.str);
  show() {
    print("str = $str");
  }
}
extension type SonStr(String str) implements Father2 {
  SonStr.a(this.str);
// SonStr(this.str);//系统自动生成的未命名构造函数
}
// extension type SonInt ( int i ) implements Father2{
//
// }

main() {
  var s1 = SonStr("111");
  s1.show();//继承了父类的方法
  var f2a = Father2.str("222");
  f2a.show();
  var f2b = Father2.str2("333");
  f2b.show();
  var f2c = Father2("444"); //这个跟上面一样,都是把传入的值,初始化了底层类型变量str
  f2c.show();






  var id9 = IntId5(100);
  id9 + 100; //正确,因为IntId5 implements int 所以可以调用int下面所有方法和操作符

  // var l1 = ListR(Iterable.generate(3,( index) =>  2 * index ).toList());
  var l2 = ListR([1, 2, 3, 4]);

  l2.RemoveAll();
  print(l2);
  l2 = ListR([7, 8, 9]);
  l2
      .map((e) => print("e= $e"))
      .toList(); //调用Iterable 里面的Map方法,如果不用implement继承 Iterable ,继承 List也可以,因为List继承Iterable,这里只是演示可以继承底层类型的父类

}
