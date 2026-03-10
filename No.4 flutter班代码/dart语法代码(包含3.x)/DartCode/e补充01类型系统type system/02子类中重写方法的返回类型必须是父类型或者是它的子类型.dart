//子类中方法的返回类型必须与父类中方法的返回类型相同或是其子类型。
import '01子类override覆盖父类方法时使用正确传入参入参类型.dart';

class Animal{
  Animal getObj(){
        return Animal();
  }
  show(){
    print("Animal show()");
  }
  /*
  Animal(){
  }
  factory Animal.a(){
    return Animal();
  }
   */
}
class Cat extends Animal{
  @override

  Animal getObj() {
    return Animal();//正确,返回类型和父类方法返回类型相同
  }

  /*
  Cat getObj() {
    return Cat();//正确,返回类型是父类的子类
  }
   */
  /*
  Dog getObj() {
    return Dog();//正确,返回类型是父类的其他子类
  }
   */
  /*
  Object getObj() {
    return Object();//错误,不能返回父类型的超类,根类
  }
   */

}
class Dog extends Animal{
}
main(){
  Animal a1 = Animal();
  // print(a1.runtimeType);
   var result = a1.getObj();
   a1.show();

  // print(result.runtimeType);
}