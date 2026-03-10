class Person{
  String name;
  Person._init(this.name);

  //factory关键字的构造函数要求return对象,但是不会像其他构造函数那样,执行到函数体的时候已经是创建对象了
  factory Person( String name){
        return  Person._init(name);
  }
  factory Person.setName( String name){
    return  Person._init(name);
  }
  showInfo(){
    print("name=$name");
  }
}

main(){
    var p1 = Person._init("abc");
    print(p1);
  var p2 = Person("张三");
  p2.showInfo();

  var p3 = Person("张三");
  p2.showInfo();
  print(identical(p2, p3));
}