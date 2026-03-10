
import 'dart:math';

main(){
  //解构类实例
  //对象模式匹配，允许给类的对象,里面公开的getter进行解构
  //所有实例变量生成一个隐式的 getter 方法。
  // 非 final 实例变量和没有初始化器的延迟 final 实例变量也会生成一个隐式的 setter 方法。
  // 要解构类的实例，使用var或者final 在类名称后面加()括号,里面 用getter:加上用来解构创建的变量
     var Circle(radius: s) = Circle(10);//系统给成员变量生成的隐式getter:radius
     final Circle(GetName:name) = Circle(20);//自己创建的getter :GetName,final用来定义name的类型是final
     // name = "123";//报错final只能被赋值1次.
     //这里的Circle的对外公开的getter是radius,这个是radius成员变量系统自动生成的隐式getter,所以可以用radius解构对象
      var Circle(GetName:str) = Circle(5);//对外的getter是自定义的GetName


      print("str=$str");
      //getter和创建用来解构的变量radius同名,所以可以省略冒号:左边的getter名字
      var Circle(:radius) = Circle(10);
    Shape c1 = Circle(1);
    //下面是使用switch语句进行 匹配,传入的是父类对象
    switch( c1){
      // case Square() || Circle():
      //   print("是原型或者方形");
    //case里面匹配用的是 类的对象的解构方法
      // case Square(length: var s) || Circle(radius: var s):  //这里没有加when做判断,所以后面的case不执行了.匹配到一个结果就自动break
      //   print("是圆形或者方形");
    // 使用when做判断条件,限制 解构匹配的变量
      case Square(length: var s) || Circle(radius: var s) when s > 0:  //使用when对 case 里面解构的 变量进行判断
        //自定义的类解构的时候里面的getter 可以解构
        print("c1 是圆形或者方形,并且面积>0");
    }


    //使用swtich表达式给变量赋值多个值

     // double calculateArea(Shape shape) => switch (shape) {
     //   Square(length: var l) => l * l,
     //   Circle(radius: var r) => math.pi * r * r
     // };
    // var area = calcullateArea(Circle(1));
     var area = calcullateArea(Shape());
     print("面积是=$area");
}
double calcullateArea(Shape s1){
  return switch(s1){
    //这里匹配用的也是 解构实例对象 类名(getter: var 变量名)
    Square(length:var l) => l*l,//正方形面积是 长度*长度,
  Circle(radius:var r)=> pi * r*r,
  Shape()=>0 //switch要求必须穷举所有类型,所以不写父类型会报错

  };
}


class Shape{
}
class Square extends Shape{
  double length;//长度
  Square(this.length);

}
class Circle extends Shape{
  double radius;//半径
  Circle(this.radius);
  get GetName{ //对外公开了一个原型
    return "圆形";
  }
}