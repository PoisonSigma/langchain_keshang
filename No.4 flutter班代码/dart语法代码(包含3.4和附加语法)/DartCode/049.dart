// 多态:父类对象运行子类方法,根据传入子类对象的真实类型,执行子类自己的方法
// 其他语言多态:父类类型的指针指向子类对象,父类指针运行子类对象的方法
// 翻译成dart就是,父类类型的对象,里面实际存储的是子类对象,可以运行子类自己重写的方法
// abstract class Person{
//   action();
//   breath() {
//     print("Person 人呼吸了");
//   }
// }
//多态的父类可以是抽象类也可以是普通的类,下面的类是普通的类,action需要有方法体
class Person{
  action(){

  }
  breath() {
    print("Person 人呼吸了");
  }
}
class Worker extends Person{
  @override
  action() {
    // TODO: implement action
    print("工人工作了");
  }

}
class Student extends Person{
  @override
  action() {
    // TODO: implement action
    print("学生学习了");
  }
}
//执行动作,这个方法的入参是父类的类型的对象,多态中实现的原理是可以用子类的对象,给父类类型的参数传入值
performAction(Person obj){
  obj.action();
}
main(){
      performAction(Student());
      performAction(Worker());
}