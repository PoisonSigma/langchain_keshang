//之前我们把dynamic类型转换成具体的String ,int等类型
class Person {}

class Worker extends Person {
  work() {
    print("工人工作了");
  }
}

class Student extends Person {
  study() {
    print("学生学习了");
  }
}
//通过is 判断类型以后,如果是子类型,那么对象的类型变成子类型,可以调用子类方法
action(Person p1){

    if(p1 is Worker ){
      p1.work();
    }
    if(p1 is Student){
       p1.study();
    }
}

main() {
  Person p1 = Worker();
  // Person p1 = Person();
  // p1.worker();//

  // p1.work();//父类对象没有子类方法;通过as 转换成子类的类型,调用子类方法
  // (p1 as Worker).work();

  Person p2 = Student();
  // (p2 as Student).study();
  action(p2);
}
