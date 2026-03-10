class Person{
  Person(){

  }
  static  final Person _instance = Person._init();
  String name = "";
  Person._init(){
    print("命名构造函数执行了");
  }


  factory Person.share( ){
    // Person();//如果有了构造函数,例如这个 Person.share,那么就没有默认的构造函数Person()
    return  _instance;
    //如果不是static,那么报错Instance members can't be accessed from a factory constructor.不能从工厂构造函数访问实例成员
  }
  showInfo(){
    print("name=$name");
  }
}
main(){



  print(Person._instance.hashCode);

  var p1 = Person.share();
  var p2 = Person.share();
  print(p1.hashCode);
  print(p2.hashCode);
  p1.name= "张三";
  p2.name= "李四";
  p1.showInfo();
  p2.showInfo();
}