
main() {
  /*
    Dart 3.0 修改了一些2.0之前的语法：
可选命名参数的默认值 可以是冒号: 也可以是等号, 3.0之后必须是等号=
mixin混入在3.0以后才是类修饰符.3.0之前,不能修饰class, 3.0之前的普通class也可以用with混入继承到类中


     */
  // fun1(age: 18, name: "张三"); //命名可选参数,可以修改位置
  // fun2("李四", 200); //位置可选参数,参数顺序不能变
  // var a1 = A();
  // var b = B();
}

//dart3.0之前, 命名可选参数的默认值,可以用冒号:,也可以用等号= ,但是3.0之后,只能用=
// fun1({String name: "张三", int age = 18}) {
//   print("name = $name age = $age");
// }
//3.0只能用=等号
fun1({String name = "张三", int age = 18}) {
  print("name = $name age = $age");
}

fun2([String name = "张三", int age = 18]) {
  print("name = $name age = $age");
}
//3.0 mixin 变成类修饰符,可以修饰class ,而且3.0 想要使用 with混入,必须用 mixin修饰的类型才可以
/*
abstract mixin class A{
  a();
}
mixin B{
      b();
}
 */

//3.0要求with混入继承的时候,必须父类是mixin修饰符.
// mixin A{
// }
/*
//下面代码mixin是类修饰符,在3.0之前会报错
mixin class B{
}
 */

//下面代码,3.0报错,但是3.0之前运行正确
/*
class A{
}
 class B{
}
class Person with A,B{
}
 */
