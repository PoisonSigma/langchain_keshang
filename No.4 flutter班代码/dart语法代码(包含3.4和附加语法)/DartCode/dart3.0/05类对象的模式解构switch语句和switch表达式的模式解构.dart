
//解构类实例
//对象模式匹配，允许给类的对象,里面getter进行解构
//所有实例变量生成一个隐式的 getter 方法。
// 非 final 实例变量和没有初始化器的延迟 final 实例变量也会生成一个隐式的 setter 方法。
// 要解构类的实例，使用var或者final 在类名称后面加()括号,里面 用getter:加上用来解构创建的变量
import 'dart:math';

main(){
  /*
  var Circle(radius:c1)  = Circle(10);
  final Circle(radius:c2)  = Circle(10);
  // c2 = 10;//final只能被设置一次
  // c1 = 100;
  print(c1);
  var Circle(GetName:name) = Circle(100);
  print(name);
  //getter和创建用来解构的变量radius同名,所以可以省略冒号:左边的getter名字
  // var Circle(radius:radius) = Circle(15);
  var Circle(:radius) = Circle(15);//getter同名的时候可以省略
  print("radius = $radius");
  var Circle(:GetName) = Circle(20);
  print("GetName = $GetName");
  //下面是使用switch语句进行 匹配,传入的是父类对象

   */
  // var c1 = Circle(10);
  // Shape c1 = Square(10);
  // test1(Shape());
 // var result = calculateArea(Shape());
 //  var result = calculateArea(Circle(1));
  var result = calculateArea(Square(1));
 print(result);


}
 test1(Shape c1){
   switch(c1){
   // case Square() || Circle():
   //   print("是圆形或者方形");
   //case里面匹配用的是 类的对象的解构方法
   //   case Square(length: var s) || Circle(radius: var s) when  s>0 :
   //     print("c1 是圆形或者方形,并且面积>0");
     case Square(length: var s) || Circle(radius: var s)  :
       if(s>0) {
         print("s= $s c1 是圆形或者方形,并且面积>0");
       }
   }
 }
 double calculateArea(Shape s1){
  return switch(s1){
  Square(length: var l) => l*l,
  Circle(radius:var r)=>pi * r * r,
  Shape()=> 0
  // _=>0
  };
 }
class Shape{
}
class Circle extends Shape{
  double radius;//半径
  get GetName{
    return "radius = $radius 圆形";
  }
  Circle(this.radius);
}
class Square extends Shape{
  double length;//半径
  Square(this.length);
}