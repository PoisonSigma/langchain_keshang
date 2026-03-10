//dart中没有接口的概念,根据其他语言的概念,勒种只有方法声明,没有方法体的实现,这样的类. dart中的接口可以理解成:只有抽象方法的 abstract class抽象类
abstract class Person<T>{
  readId(T id);//抽象方法
  readId2(T id);//抽象方法
  readId3(T id);//抽象方法
}

//子类继承父类的时候也要带上泛型<>
/*
class Worker<T> implements Person
class Worker implements Person<T>
class Worker implements Person
这3种方式都不是我们想要的结果
 */
class Worker<T> implements Person<T>{
  T id;
  //通过构造函数初始化的时候,让T确定泛型的类型,如果不在构造函数中指定类型那么T的类型就是dynamic
  Worker(this.id);
  readType(){
    print("T = $T");
  }
  @override
  readId(T id) {
    // TODO: implement readId
    print("T = $T");
    print("id = $id");
  }

  @override
  readId2(T id) {
    // TODO: implement readId2
    print("T = $T");
    print("id = $id");
  }

  @override
  readId3(T id) {
    // TODO: implement readId3
    print("T = $T");
    print("id = $id");
  }
}
main(){
  var w1 = Worker("abc");
  w1.readId("bbb");
  w1.readId("abc");
  w1.readId2("xxx");
// w1.readType();
}