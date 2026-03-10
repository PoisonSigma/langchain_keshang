main() {
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
//假设我们有这么一个需求,Person作为父类,子类有2个,工人Worker和学生Student,要求这2个子类都有方法:学习咏春拳 和 王八拳,这2种拳法,我放在2个mixin混入类中

  var s1 = Student1();
  s1.lun(); //使用implements 继承多个接口调用方法,需要实现所有父类方法
  s1.zhonglu();
var w1 = Woker1();
w1.lun();
w1.zhonglu();

  var wb2 = WangBaQan2(); //mixin class可以直接创建对象
  wb2.lun();

  // YongChun2();//报错mixin混入 不带class关键字不能直接创建对象
  var s2 = Student2();
  s2.zhonglu();
  s2.lun();
  var w2 = Woker2();
  w2.lun();
  w2.zhonglu();
  // Speak(); abstack mixin class不能创建对象

  E3().show();
}

interface class YongChun1 {
  //这里使用接口是为了在库外不会被extends继承,只能被implements实现,那么这里的方法在库之外就必须重写了,相当于所有方法在库之外
  zhonglu() {
    print("永春攻击");
  }
}

class WangBaQan1 {
  //这里可以使用 interface也可以不适用,因为在子类中都是用implements都要强制重写方法
  lun() {
    print("王八拳攻击");
  }
}

class Person {
  breath() {
    print("人类呼吸");
  }
}

//implements实现接口需要在子类中,强制实现所有接口中的方法
class Student1 extends Person implements YongChun1, WangBaQan1 {
  // @override
  zhonglu() {
    print("切中路");
    // super.zhonglu();//注意implements继承的父类方法,在子类中不能被调用,会当做抽象方法,但是编译器会帮你把父类中的方法体自动修复
  }

  @override
  lun() {
    print("王八拳攻击");
  }
}

class Woker1 extends Person implements YongChun1, WangBaQan1 {
  @override
  lun() {
    // TODO: implement lun
    print("王八拳攻击");
  }

  @override
  zhonglu() {
    // TODO: implement zhonglu
    print("切中路");
  }
}

mixin YongChun2 {  //只用mixin修饰符,不加class不能创建对象
  //这里使用接口是为了在库外不会被extends继承,只能被implements实现,那么这里的方法在库之外就必须重写了,相当于所有方法在库之外
  zhonglu() {
    print("永春攻击");
  }
}

mixin class WangBaQan2 {  //mixin作为类修饰符 + class可以直接创建对象
  lun() {
    print("王八拳攻击");
  }
}

// //混入可以让一个子类继承父类的同时,再混入一个mixin,而且不像implements那样需要强制重写普通方法
class Woker2 extends Person with YongChun2, WangBaQan2 {}
class Student2 extends Person with YongChun2, WangBaQan2 {}


//只加mixin ,不加 class 当做抽象类来看,他可以定义抽象方法
mixin  A{
  a();//可以定义抽象方法
}
mixin class  B {
  //kick();//报错,不是抽象类,mixin当做类修饰符 ,有class ,不能定义抽象方法
}

// 5 .on关键字,限制 mixin可以被哪个类继承混入 例如 声明 mixin A  on Base ,代表 A只能被 Base继承
mixin Walk on Person3{
  walk(){
    print("走路");
  }
}
// class Person3 with Walk{ //报错,不能直接给mixin后面的on 的父类作为接口
// }
class Person3{
}
class Student3 extends Person3 with Walk{//正确,可以给Person3的子类混入接口
}

//6.抽象mixin类 ,abstract mixin class 因为是class,所以可以被extends继承,因为是abstract,所以可以有抽象方法
abstract mixin class  Speak{
      speak();
}
class Person4 with Speak{
  @override
  speak() {
    // TODO: implement speak
    print("人类说话");
  }
}
mixin A1 { //不能被extends继承
  a();//可以定义抽象方法
}
mixin  class A2{ //可以被extends继承
   // a();//报错,不是抽象类不能定义抽象方法
}
abstract mixin class A3{  //抽象混入类, 因为是class,所以可以被extends继承
  a();//可以定义抽象方法
  b(){  //普通方法
  }
}
// class C extends A1{   //报错,不能被extends继承
class C2 extends A3{
  @override
  a() {
  }

}

//7.混入继承多个mixin父类,有相同名字的方法,后继承的会覆盖先继承的

// implements继承2个父类,但是因为同名方法,所以只能实现一个方法
abstract class D1{
  show();
}
abstract class D2{
  show();
}
class D3 implements D1,D2{
  @override
  show() {
    // TODO: implement show
    //implements继承2个父类,但是因为同名方法,所以只能实现一个方法
  }
}

//mixin混入的2个同名方法,后混入的覆盖之前的
mixin E1{
   show(){
     print("E1");
   }
}
mixin E2{
  show(){
    print("E2");
  }
}
// class E3 with E1,E2{  // 这里的show方法E2覆盖E1
// }
class E3 with E2,E1{  // 这里的show方法E1覆盖E2
}