//替换类型 Substituting types
class Animal{
  
}
class Cat extends Animal{
      CatEat(){
        
      }  
}
class BlackCat extends Cat{

}
class Dog extends Animal{

}
main(){
  // dart引入2个概念,生产者和消费者 ,
  // 1.生产者 右边创建的对象
  // 2.消费者 接受保存生产者产生对象的变量,或者是函数的形参,接收的参数
  // 1. 简单类型赋值
  // 赋值左边是 消费者 , =等号右边是生产者
    Animal c = Cat();//正确 ,子类对象可以赋值给父类指针
  //可以理解为c是消费者,他接受 右边生产者 生产的对象. 右边生产者替换到左边消费者里面的东西是安全的
  //c消费者要消费的东西,右边的生产者都有. 父类中的方法,在子类中都有
    // Cat c2 = Animal();//错误,Cat里面有子类的方法CatEat() ,父类中没有定义
  //左边消费者是 子类对象,里面有特有的方法.  右边生产者的对象是父类的,里面没有左边消费者要消费的特有方法



//泛型中, 类型注释 ,子类可以赋值给左边的父类
List<Animal> list1 = <Cat>[Cat(),Cat()]; //右边是子类,可以赋值给左边的父类
List<Cat>list2 = <BlackCat>[BlackCat(),BlackCat()];
// List<Cat>list3 = <Animal>[Animal(),Animal()];//静态分析错误,右边是父类,不能赋值给左边


//用as强转后静态分析正确,运行时候错误,是否正确,取决于,实际类型
// List<Cat>list3 = <Animal>[Animal(),Animal()] as List<Cat>;//用强制转换后静态分析正确,但是运行时错误,
// List<Animal>' is not a subtype of type 'List<Cat>' in type cast在类型转换中，List<Animal> `不是类型` List<Cat> `的子类型

//函数的替换类型,在01,02课中 函数的入参和返回类型中讲过
//01 传入类型: 重写函数的参数是父类型方法的传入类型 或者 超类
//02 返回类型: 子类中方法的返回类型必须与父类中方法的返回类型相同或是其子类型。
}



