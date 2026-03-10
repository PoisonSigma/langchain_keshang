// abstract class Person {
//   action();
//
//   breath() {
//     print("Person 人呼吸了");
//   }
// }
//多态的父类可以是抽象类也可以是普通的类,下面的类是普通的类,action需要有方法体
class Person {
  action(){

  }

  breath() {
    print("Person 人呼吸了");
  }
}
class Worker extends Person {
  @override
  action() {
    print("工人工作");
  }
}

class Student extends Person {
  @override
  action() {
    // TODO: implement action
    print("学生学习");
  }
}

//执行动作,这个方法的入参是父类的类型的对象,多态中实现的原理是可以用子类的对象,给父类类型的参数传入值
// 多态:父类对象运行子类方法,根据传入子类对象的真实类型,执行子类自己的方法
// 其他语言多态:父类类型的指针指向子类对象,父类指针运行子类对象的方法
// 翻译成dart就是,父类类型的对象,里面实际存储的是子类对象,可以运行子类自己重写的方法
void performAction(Person obj) {
  obj.action();
}
//或者我之前做了8个不同类型子页面,用了一个方法去调用不同的页面,如果用if else 或者switch去判断页面类型,
// 然后执行下面的方法,那么每次扩充,都要修改if判断条件
//但是我把这些页面都让他们共同继承一个接口,在dart中叫抽象类,接口下面有一个方法,那么我就可以让主页面,每次都调用这些子页面里面继承过来的共同方法

main() {
  var w1 = Worker();
// w1.action();
  var s1 = Student();
// s1.action();


  performAction(w1);
  performAction(s1);
}
