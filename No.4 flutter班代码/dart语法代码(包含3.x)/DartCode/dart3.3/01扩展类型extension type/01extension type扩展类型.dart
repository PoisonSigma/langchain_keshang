/*
发布日期：2024年2月15日 | Dart 3.3 公告

Dart 3.3 为语言添加了一些增强功能：
扩展类型是 Dart 中的一个新功能，允许零成本地包装现有类型。它们类似于包装器类和扩展方法，但具有不同的实现差异和不同的权衡。
格式
*/

//系统会根据声明后面扩展类型的格式,隐式的生成构造函数, 未命名的,或者命名的构造函数
extension type IntId(int i) {
  //系统会默认生成包装的底层的对象的getter,但是不会生成setter
  int get iValue => i + 100000;
  // int i2;//报错,不能创建成员变量,编译器提示改成getter
  set setName (int value){
      print("调用setter");
  } //自己生成setter i
  // IntId(this.i);//系统会默认生成,包装类型的构造函数,这里面生成的是 默认的,未命名的
  showId() => print("id = $i");

  operator <(int other) => i < other;
}

class A {
  //复习命名构造函数
  int age;

  A(this.age);

  A.withA(this.age); //命名构造函数
  //setter跟getter的复习
  int get age2 => age + 1;
  set age2(int i) => age = i;
}
//给自定的类型进行包装
extension type A2(A obj){
  // A2(this.obj);//重定义
  A2.a(this.obj);
}

//
extension type IntId2.n(int i) {
  // IntId2.n(this.i);//系统默认生成了命名构造函数IntId2.n
  IntId2(this.i); //默认的未命名构造函数在这里需要自己生成
  IntId2.m(this.i);
}
extension type IntId3._(int i){
      IntId3(this.i);
}

main() {
  /*
  //getter setter的复习
  var a1 = A(18);
  a1.age = 100;
  a1.age2 = 88;
  print(a1.age);
  print(a1.age2);


   */
/*
    //目的是不想让自己封装的id的整形,拥有 int的方法,例如数学运算
    int a = 100;//普通的int有 操作符重载 + - 等
    a + 10;

    //
    IntId id1 = IntId(100);
    // id1+10;//报错,自定义的 扩展类型,没有 int的方法和操作符重载
    id1.showId();

    print(id1 < 99);

    var id2 = IntId(200);
    print(id1 < id2.i);  // 用包装类型里面的底层类型去比较 ,系统默认生成了底层类型的getter
 */

//getter setter的调用
/*
  var id3 = IntId(100);
  // id3.i = 99;//没有setter
  print(id3.iValue);
  id3.setName = 99;
*/

var id4 = IntId3._(100);//同一个文件内,就是同一个库,私有的命名构造函数可以调用
}
