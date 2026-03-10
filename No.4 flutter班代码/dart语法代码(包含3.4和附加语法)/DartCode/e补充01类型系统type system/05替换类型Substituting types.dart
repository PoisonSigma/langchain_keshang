//替换类型 Substituting types
class Animal{
      beath(){
        print("动物呼吸");
      }
}
class Cat extends Animal{
   CatEat(){
     print("猫吃🐟");
   }
}
// dart引入2个概念,生产者和消费者 ,
// 1.生产者 右边创建的对象
// 2.消费者 接受保存生产者产生对象的变量,或者是函数的形参,接收的参数
// 1. 简单类型赋值
// 赋值左边是 消费者 , =等号右边是生产者
main(){
  /*
    Animal c1  = Cat();
    c1.beath();
    // c1.CatEat();//不可以
   */
  /*
  Cat c1  = Animal();//错误,左边是子类类的变量,右边是父类的对象
  c1.CatEat();
   */
  //泛型中, 类型注释 ,子类可以赋值给左边的父类
  List<Animal>list1 = <Cat>[Cat(),Cat() ] ;//合法
  List<Animal>list2 = <Cat>[Cat(),Cat() ] ;//静态分析合法
  // list2.first.beath();
  // list2.first.CatEat();//不能调用

  //用as强转后静态分析正确,运行时候错误,是否正确,取决于,实际类型
  var list3 = list2 as List<Cat>;
  // list3.first.CatEat();
  List<Animal>list4 = <Animal>[Animal(),Animal() ] ;

  // (list4 as List<Cat>).first.CatEat();//用强制转换后静态分析正确,但是运行时错误,


  run(list3);
}
run(List<Animal> list){
  list.first.beath();
}