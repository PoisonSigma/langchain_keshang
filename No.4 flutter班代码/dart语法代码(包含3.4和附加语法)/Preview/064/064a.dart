class Person {
  String name = ""; //给一个默认值
   static final Person instance =
      Person._init(); //既然是单例,就只创建一个对象,不要每次创建都给成员变量赋值了
  Person._init() {
    print("私有命名构造函数执行");
  }

  //factory关键字的构造函数要求return对象,但是不会像其他构造函数那样,执行到函数体的时候已经是创建对象了
  factory Person() {
   return instance; //如果不是static,那么报错Instance members can't be accessed from a factory constructor.不能从工厂构造函数访问实例成员
  }


}
main(){
    // var p1 = Person();
    // var p2 = Person();
    //
    // print(identical(p1, p2));
    //
    // print(p1.hashCode);
    // print(p2.hashCode);
    print(Person.instance.hashCode);

  var p1 = Person();
  p1.name = "张三";
}