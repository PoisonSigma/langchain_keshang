/*
终端执行命令:
找到flutter sdk位置:
which flutter
进入这个目录
cmd+, 设置,dart 找到 Dart SDK path:,然后 点击3个点


    Dart 3.0 修改了一些2.0之前的语法：
可选命名参数的默认值 可以是冒号: 也可以是等号, 3.0之后必须是等号=
mixin混入在3.0以后才是类修饰符.3.0之前,不能修饰class, 3.0之前的普通class也可以用with混入继承到类中

mixin混入在3.0以后才是类修饰符.3.0之前,不能修饰class, 3.0之前的普通class也可以用with混入继承到类中

如果continue语句指定了一个未连接到循环语句（for、do 和 while）或switch成员的标签，现在将会引发编译时错误。
 */
main(){
      // fun1(name:  "张三");
      // fun2("张三");

      var p1 = Person();
      p1.a();
      p1.b();
      // var p2 = Person2();
      // p2.a2();
      // p2.b2();

}
//下面是dart3.0以后可选命名参数,默认值 用等号= ,但是在3.0之前用冒号:
fun3({required String name,int age = 100}){

}
//位置可选参数的默认值依然是用等号=
fun4([String name = "张三", age = 200]){

}


//下面代码在dart 3.0之前 代码里面运行正确
/*
fun1({ String name , int age : 100} ){
  print("name = $name age = $age");
}
//位置可选参数默认值还是等号= ,这个 dart 3.0 和 3.0之前都正确
fun2([String name = "张三",int age =200]){
  print("name = $name age = $age");
}
 */


//dart 3.0 之前之后 使用mixin关键字定义的混入类型 都能被with继承混入

mixin  A {
   a(){
     print("a()");
   }
}
mixin  B {
  b(){
    print("b()");
  }
}
//可以with混入
class Person with A,B{
}
//错误3.0之前没有类修饰符 这个概念,mixin不能放在class前面
// mixin class C{
//
// }
/*
//错误,mixin不能当类修饰符
abstract mixin class D{
}

 */
class A2{
  a2(){
    print("a2()");
  }
}
class B2{
  b2(){
    print("b2()");
  }
}
//3.0之前,普通的 class,不带mixin也能被with混入,但是这段代码在3.0之后会报错
/*
class Person2 with A2,B2{
}

 */