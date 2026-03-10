//泛型继承
//泛型可以通过 extends关键字,限制泛型是某一个类型或者他的子类
//格式<T extends 某个类型>

class Person<T>{
  T id;
  Person(this.id);//构造函数中传入的参数id,因为id被定义为T类型,所以在这时,T被识别出传入的类型.
  showId(){

    print("T=$T");//打印类型
    print("id=$id");
  }
}
//这里证明extends某个子类,即使是mixin的子类,用with继承,也可以限制
//泛型中用 限制类型
mixin YongChun {
  attack(){
    print("大吼一声咏春叶问,然后直接切了对手中路,把对手打到");
  }
}
//因为mixin类和抽象类一样,不能实例化创建对象,所以我们用一个普通类继承子mixin类
// class ZhaoJiaBanFighter extends YongChun{ //错误 mixin类不能用extends继承,换成with
class ZhaoJiaBanFighter with YongChun{
}


//使用extends限制 泛型T是某一个类型或者他的子类就,下面是
// 要求T是 YongChun类型或者他的子类,因为YongChun是抽象类mixin不能创建对象,所以用一个子类ZhaoJiaBanFighter创建对象

// class ZhaoJiaBan<T with YongChun>{ //错误不能用with
class ZhaoJiaBan<T extends YongChun>{
  T fighter;
  ZhaoJiaBan(this.fighter);
  action(){
    fighter.attack();
  }
}
//证明 T extends 限定泛型是 可以是某一个类,而不光是子类,这里构造函数用Person创建对象
class LiJiaBan<T extends Person>{
  T person;
  LiJiaBan(this.person);
  action(){
    person.showId();
  }
}
main(){

  var f1 = ZhaoJiaBanFighter();
  var z1 = ZhaoJiaBan<ZhaoJiaBanFighter>(f1);
  var z2 = ZhaoJiaBan(f1);//泛型可以省略
  z1.action();
  z2.action();

  var p1 = Person(123);
  var l1 = LiJiaBan(p1);
  // var l2 = LiJiaBan(f1);//错误 LiJiaBan要的泛型T是需要 extends Person,    f1是ZhaoJiaBanFighter的对象,不是Person类或者子类
  l1.action();
}