

main(){
  /*
  无修饰符是之前定义的默认的类
  abstract 类修饰符 是定义的抽象类


  =====
  base

base修饰符。基类禁止在其自己的库之外implements。这保证了：

当创建类的子类型的实例时，基类构造函数被调用。
所有实现的私有成员在子类型中存在。
基类中的新实现成员不会破坏子类型，因为所有子类型都继承了新成员。除非子类型已经声明了具有相同名称但签名不兼容的成员。
必须将任何实现或扩展基类的类标记为base、final或sealed。这样可以防止外部库破坏基类的保证。
*/

    var v1 = Vehicle(); //base 类可以创建对象
    v1.move(10);
    var c1 =Car(); //子类也可以创建对象
    c1._name = "小汽车";//同一个文件内,可以访问父类私有成员
    c1.move(100);

    var p1 = Person();
    p1.move(1000);
    var b1 = BYD();
    b1._wheels = 6;
    b1._name = "byd";


    var a1 = A(); //final可以创建对象,但是不能访问私有变量
  a1._name;//可以访问
  // var b1 = B();//报错sealed类不能创建对象,这样私有属性也不会被修改.
}
base class Vehicle{
  String _name = "宝驴";//私有成员
  String name2 = "毛驴";//非私有成员
  move(int meters){
      print("交通工具移动 $meters");
  }
}

// 可以被base final sealed类修饰符的类扩展,
base class Car extends Vehicle{
  int _wheels = 4;//轮子数 4个 .  子类也使用base ,保证子类的子类也都自动继承成员
    @override
  move(int meters) {

      print("小汽车 移动 $meters");

  }
  
}
base class BYD extends Car{ //孙子类也是必须是base,这样能保证有父类和爷爷类的成员


}
//在本文件内可以被实现implements
base class Person implements Vehicle{
  @override
  move(int meters) {
    // TODO: implement move
    print("人类移动 $meters");
  }

  @override
  String _name = "人类";

  @override
  String name2  = "张三";  //既然是用implements,那么继承过来父类的所有变量和属性都要实现
  
}
final class A extends Vehicle{

}
// class A2 extends A{//报错 final不能被继承
// }
sealed class B extends Vehicle{

}
