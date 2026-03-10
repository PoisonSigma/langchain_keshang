class Person{
  String name;
  Person._init(this.name ){
    print("init命名构造函数");
    print("name = $name");
  }


  //factory关键字的构造函数要求return对象,但是不会像其他构造函数那样,执行到函数体的时候已经是创建对象了
  factory Person(){ //报错,因为没有返回值
    print("默认构造函数");

    // return Person();//注意不能这样,因为这个方法自己就叫Person,等于反复递归调用自己
    return  Person._init("");//返回用明明构造函数创建的对象
  }
  factory Person.setName(String name){
    //这里自己的命名构造函数init会创建对象,把他返回的对象当做 工厂方法的 返回值
    return Person._init(name);
  }
}