import '16类修饰符base.dart';

main(){
    var v1 = Vehicle();
    v1.move(10);
    var c1 = Car();
    // c1._name = "小汽车";//父类文件之外,不能访问父类私有成员
    c1.name2 = "小毛驴";
    print("c1.name2 = ${c1.name2}");
    var a1 = A(); //final可以创建对象,但是不能访问私有变量
    // a1._name;//报错,final里面没有父类的私有属性
    // var b1 = B();//报错sealed类不能创建对象,这样私有属性也不会被修改.
}

// 可以被扩展
base class Car extends Vehicle{
}
final class A extends Vehicle{

}
// class A2 extends A{//报错 final不能被继承
// }
sealed class B extends Vehicle{

}
// class C extends Vehicle{  //报错 继承base必须是 base、final或sealed
// }
//在base类所在库的文件之外不能被implements,这样 确保base类中的私有成员可以出现在子类中
//如果文件外可以implements,那么就必须实现私有成员,那么文件外就能访问私有成员
//这样就破坏了私有成员不能再文件外被访问的规则.
/*
base class Person implements Vehicle{ //报错,文件外不能implements 继承base类
//如果base 允许在文件之外 implements ,那么以为implements 要求必须重写所有的 成员和方法,
这样私有方法也会被实现,这样文件之外就可以访问父类的私有方法.这样就违背了设计base的目的,目的是文件外不能访问私有方法
    @override
    move(int meters) {
        // TODO: implement move
        print("人类移动 $meters");
    }
*/