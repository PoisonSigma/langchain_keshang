//子类中方法的返回类型必须与父类中方法的返回类型相同或是其子类型。
class Animal{
     Animal getObj(){
        return Animal();
     }
}
class Cat extends Animal{
  /*
  @override
  Animal getObj() { //正确,返回类型和父类方法返回类型相同
    return Animal();
  }
   */
  /*
  @override
  Cat getObj() {
    return Cat();//正确,返回类型是父类的子类
  }
   */
  /*
  @override
  Dog getObj() {//正确,返回类型是父类的子类
    // TODO: implement getObj
    return Dog();
  }
   */
  /*
  @override
  Object getObj() {//错误,返回类型不能是父类型的父类型,只能是父类型或者是它的子类型
    return Object();
  }
   */
}

class Dog extends Animal{

}