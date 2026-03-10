/*
类的构造函数是常量构造函数,但是如果调用构造函数的时候,传入的值,是可变的,不是常量,那么调用的时候也不能加const
如果常量构造函数 加了const 要求里面传入的参数必须是不可变的,例如是 const类型的,如果是类的对象,要求这个对象也是用常量构造函数创建的
 */
//自定义的文本框Text1
class Text1 {
  final String data;
  const Text1(this.data);
}

main() {
  const Text1("hello world");
  // String data = "hello world";
  // // const Text1(data); //传入的参数不是const类型,调用的时候不能加const
  const String data = "hello world";
  const Text1(data); //
}
