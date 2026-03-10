/*
发布日期：2024年2月15日 | Dart 3.3 公告

Dart 3.3 为语言添加了一些增强功能：
扩展类型是 Dart 中的一个新功能，允许零成本地包装现有类型。它们类似于包装器类和扩展方法，但具有不同的实现差异和不同的权衡。
格式
*/







//(int i )里面放的是底层的内置成员变量 int i,也可以放自定义的类
extension type IntId(int i) {  //括号里面的参数是什么,系统就默认生成这个参数的构造函数,例如这里会生成IntId(this.i)的构造函数
  //这里的int i 在类型中是包装的内置的成员变量,有内置的getter,可以 调用 对象.i //例如 var i1 = IntId(100)   i1.i
  operator <(IntId other) => i < other.i;

  // IntId(this.i);//报错,这个构造函数是系统已经定义的隐式构造函数,不能自己重定义
  // Can't use 'IntId' because it is declared more than once.不能使用` IntId `，因为它被声明了多次
  IntId.n(this.i); //命名构造函数,类名+方法名
  IntId.m(int j, String foo) : i = j + foo.length; //命名构造函数
}

extension type IntId2.a(int i) {  //这里生成的是 IntId2.a(this.i)
  // IntId2.a(this.i);//系统默认生成这个,所以这里报错重定义
  //因为IntId2 声明的时候直接声明了命名构造函数,
  // 所以隐式的未命名构造函数unnamed constructor 就没有被系统声明,需要自己定义
  IntId2(this.i); //需要自己手动声明未命名的构造函数
}

extension type IntId3._(int i) {
  //_下划线是私有构造函数
  // IntId3._(this.i);//重定义
}
extension type IntId4(int i) {

  // int i2;//Extension types can't declare instance fields. (Documentation)  Try replacing the field with a getter.
  // 报错,类型不能声明实例字段。尝试用getter替换字段。
  //声明成员,getter
  IntId4 get num => this; //正确,用getter来代替 成员变量
  //声明setter,这里只能打印,因为无法给其他成员变量赋值,其他成员变量也没有setter
  set set_i(int i) {
    print("i = $i");
    // i = value;//'i' can't be used as a setter because it's final 不能给内置的 i 设置setter,因为他是finnal

  }

}

class A{
  int age;
  A(this.age);
}
//可以扩展类型可以包装自定义的类作为内部类型
extension type  A2(A obj) {
    // String name; //不能定义成员变量,但是可以定义getter
  A get  value => obj;
}


void main() {
  var a1 =  A2(A(18));
  print("a1 = ${a1.value}");
  print("${a1.value.age}");


  int a = 100; //普通的整形int是有 很多运算的,例如 + - * /
  a = a + 10; //普通的int可以进行 数学运算,这里的需求是,让整形只有 < 小于号运算,其他运算没有,那么用下面的类型扩展
  var id1 = IntId(200); //定义的格式,是 像类的构造函数一样,上面 extension type int_id(int i)的格式
  // b1 + 10;//报错,自定义的 扩展类型 int_id 没有定义 + 加号运算符
  var id2 = IntId(300); //使用var定义也可以,但是右边要用自己创建类型的格式
  id1 < id2; //正确,自己定义了 < 运算符
  if (id1.i < id2.i) {
    print("<");
  }
  // int a2 = b1;//报错,类型不对
  int a3 = id1 as int;
  print("a3 = $a3");

  //调用自定义的命名构造函数
  var id3 = IntId.n(400);
  int i3 = id3.i; //可以,里面内置了隐式的i 的 getter
  // id3.i = 100;//不能给他的setter赋值,没有setter

  var id4 = IntId.m(1, "abc");
  print("id4.i=${id4.i}");
  //隐式构造函数

  var id5 = IntId2.a(100);
  var id6 = IntId2(200); //因为IntId2 声明的时候直接声明了命名构造函数,
  // 所以隐式的未命名构造函数就没有被系统声明

  var id7 = IntId3._(300); //私有构造函数,文件外不能访问,当前文件下可以访问

  var id8 = IntId4(100);
  print(id8.num); //打印getter
  id8.set_i = 200; //执行自定义的setter
  // id8.value;//错误static类型是属于某个类型的不是属于某个变量的
  print(IntId4.value); //value是static静态成员,是属于扩展类型的,不是属于某一个对象的
  IntId4.changeValue(200);
}
