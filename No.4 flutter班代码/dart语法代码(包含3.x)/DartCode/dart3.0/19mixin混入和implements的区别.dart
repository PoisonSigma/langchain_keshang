main(){
  /*
    mixin混入
    mixin类声明需要至少3.0的语言版本。
    mixin比implements的好处是,在多层次继承的时候,不需要强制重写所有方法,普通方法可以直接继承过来使用
    普通的extends单线继承和implements多继承,无法满足一些要求,所以出现了混入mixin,混入的非抽象方法可以直接使用,不需要重写,可以降低耦合度
    1.可以完成多层次继承: 可以同时extends一个父类,再用with 混入多个mixin父类
    2.普通的多继承是用implements实现,这个要求把所有父类和接口的所有属性和方法都重写实现.mixin也是多继承,
    但是他跟implements的区别是,使用with关键字混入的mixin可以像extends那样使用,就是只有抽象方法才强制重写实现,普通方法可以不实现,直接继承过来使用.

    3.mixin class可以直接创建对象 ,mixin不能创建对象
    4.mixin class不能创建抽象方法,mixin 可以创建抽象方法
    5 .on关键字,限制 mixin可以被一个类的子类混入 例如 声明 mixin A  on Person ,代表 A只能被 Base的子类混入 ,例如 class Student extends Person with A
    6.抽象mixin类 ,abstract mixin class 因为是class,所以可以被extends继承,因为是abstract,所以可以有抽象方法
    7.混入继承多个mixin父类,有相同名字的方法,后继承的会覆盖先继承的
     */
  /*
  var w1 = Worker1();
  w1.zhonglu();
  w1.lun();
  var s1 = Student1();
  s1.zhonglu();
  s1.lun();
   */
  /*
  var yc2 =  YongChun2();//mixin class可以创建对象
  yc2.zhonglu();
  // WangBaQuan2();//报错,只有mixin没有class不能创建对象
   */
/*
   var w1 = Worker1();
   w1.lun();
   w1.zhonglu();
   var s1 = Student1();
   s1.lun();
   s1.zhonglu();

 */
  D3().d();
}
/*
interface class YongChun1{//这里使用接口是为了在库外不会被extends继承,只能被implements实现,那么这里的方法在库之外就必须重写了,相当于所有方法在库之外
    zhonglu(){
      print("切中路");
    }
}
class WangBaQuan1{
  //这里可以写方法体,也可以不写,因为在子类中都是用implements都要强制重写方法
  lun(){
    print("王八拳左右开轮");
  }
}
class Person1  {
  breath(){
    print("人类呼吸");
  }
}
class Worker1 extends Person1 implements YongChun1, WangBaQuan1{
  @override
  lun() {
    // TODO: implement lun
    print("王八拳左右开轮");
  }

  @override
  zhonglu() {
    // TODO: implement zhonglu
    print("切中路");
  }
}
class Student1 extends Person1 implements YongChun1,WangBaQuan1{
  @override
  lun() {
    // TODO: implement lun
    print("王八拳左右开轮");
  }

  @override
  zhonglu() {
    // TODO: implement zhonglu
    print("切中路");
  }
}
 */
mixin class YongChun2{
  zhonglu(){
    print("切中路");
  }
}
mixin  WangBaQuan2{  //只用mixin修饰符,不加class不能创建对象

  lun(){
    print("王八拳左右开轮");
  }
}
class Person2  {
  breath(){
    print("人类呼吸");
  }
}
class Worker1 extends Person2 with YongChun2, WangBaQuan2{
}
class Student1 extends Person2 with YongChun2,WangBaQuan2{
}

//只加mixin ,不加 class 当做抽象类来看,他可以定义抽象方法
mixin A{
  a();//可以定义抽象方法
}
mixin class B{
  // a();//报错,不是抽象类,mixin当做类修饰符 ,有class ,不能定义抽象方法
}
// 5 .on关键字,限制 mixin可以被哪个类继承混入 例如 声明 mixin A  on Base ,代表 A只能被 Base继承

// class Person3 with Walk{ //报错,不能直接给被on限制的父类作为接口
// }

mixin Walk on Person3{
    walk(){
      print("走路");
    }
}
class Person3{

}

class Student3 extends Person3 with Walk{ //只能给 on限制的子类作为混入的接口
}
// class A3 with Walk{//报错,A3不是 Walk的子类,所以不能混入
// }
//6.抽象mixin类 ,abstract mixin class 因为是class,所以可以被extends继承,因为是abstract,所以可以有抽象方法

abstract mixin class Speak{
  speak();//可以定义抽象方法
}
class A4 extends Speak{  //可以被extends
  @override
  speak() {
    // TODO: implement speak
  }
}
class A5 with Speak{
  @override
  speak() {
    // TODO: implement speak
  }
}
mixin A1{
  a();
}
 // class A2 extends A1{ //报错 类只能被其他类继承,不能被mixin继承
 // }
  mixin   B1{
  b();//可以定义抽象方法
}
//7.混入继承多个mixin父类,有相同名字的方法,后继承的会覆盖先继承的
// class D1 {
//   d(){
//     print("d1");
//   }
// }
// class D2 {
//   d(){
//     print("d2");
//   }
// }

// implements继承2个父类,但是因为同名方法,所以只能实现一个方法
// class D3 implements D1,D2{
//   @override
//   d() {
//     print("D3");
//   }
// }
mixin D1 {
  d(){
    print("d1");
  }
}
mixin D2 {
  d(){
    print("d2");
  }
}
//mixin混入的2个同名方法,后混入的覆盖之前的
// class D3 with D1,D2{
// }
class E1{

}
class D3  extends E1 with D2,D1{
}
