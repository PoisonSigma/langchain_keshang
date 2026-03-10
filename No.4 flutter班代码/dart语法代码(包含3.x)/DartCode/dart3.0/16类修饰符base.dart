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
  var  p1 = Person17();
  p1._name;
  p1.name2;
  var w1 = Worker();
  w1._name;
  w1.name2;
  var s1 = S17();
  s1._name; //访问了父类的私有属性,因为这个implments是在父类的同一个文件之下.
  s1.name2;

}
base class Person17{
    String _name = "人类";
    String name2 = "张三";
}
base class Worker extends Person17{  //子类必须是base、final或sealed
}
class Test17{

}
base class S17 implements Person17{
  @override
  String _name = "S17的名字";

  @override
  String name2 = "S17的名字2";//同一文件下,可以使用implements

}