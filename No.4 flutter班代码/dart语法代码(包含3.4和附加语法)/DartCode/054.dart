//泛型可以通过 extends关键字,限制泛型是某一个类型或者他的子类
//格式<T extends 某个类型>


//这里证明extends某个子类,即使是mixin的子类,用with继承,也可以限制



mixin YongChun{
  attack();
}


//因为mixin类和抽象类一样,不能实例化创建对象,所以我们用一个普通类继承自mixin类
// class ZhaoJiaBanFighter extends YongChun{ //错误 mixin类不能用extends继承,换成with
class ZhaoJiaBanFighter with YongChun{
  @override
  attack() {
    // TODO: implement attack
    //实现
      print("大吼一声咏春叶问,然后直接切了对手中路,把对手打到");
  }
}
//使用extends限制 泛型T是某一个类型或者他的子类,下面是
// 要求T是 YongChun类型或者他的子类,因为YongChun是抽象类mixin不能创建对象,所以用一个子类ZhaoJiaBanFighter创建对象
// class ZhaoJiaBan<T with YongChun>{ //错误不能用with
class ZhaoJiaBan<T extends YongChun >{
    T fighter;
    ZhaoJiaBan(this.fighter);
    action(){
       fighter.attack();//用限制类型的泛型,可以让 泛型类型的对象,点出泛型的方法
      //作用,可以调用出限制类型的方法.
    }
}

//证明 T extends 限定泛型是 可以是某一个类,而不光是子类,这里构造函数用Person创建对象
class Person<T>{
  T id;
  Person(this.id);//构造函数中传入的参数id,因为id被定义为T类型,所以在这时,T被识别出传入的类型.
  showId(){
    print("T=$T");//打印类型
    print("id=$id");
  }
}
class LiJiaban <T extends Person>{
  T person;
  LiJiaban(this.person);
  action(){
    person.showId();
  }
}
main(){
 // var y1 = YongChun();
  var f1 = ZhaoJiaBanFighter();
 // var z1 = ZhaoJiaBan(f1);
 // z1.action();
  var p1 = Person(123);
  // p1.showId();
  var l1 =  LiJiaban(p1);//错误,不是Person或者他的子类,会报错
  //  var l1 =  LiJiaban(f1);//错误,不是Person或者他的子类,会报错
   l1.action();
}