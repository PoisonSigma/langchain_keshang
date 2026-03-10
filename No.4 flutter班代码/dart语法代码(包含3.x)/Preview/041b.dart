
import '041.dart';

main(){
  var p1  = Person();
  // p1._a = 100;//这里可以看到,给属性赋值,默认就是调用setter,系统自动给每个属性设置了默认的setter和getter

  // print(p1._a); // Error: The getter '_a' isn't defined for the class 'Person'.
  p1.set_a = 200;//正确,因为set_a依然是一个方法,自己起的名字,set_a,所以可以给私有变量_a赋值
  p1.showInfo();
}