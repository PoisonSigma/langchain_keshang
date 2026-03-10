
// 这是一个错误：
import '06b.dart';


// class Bad extends Amigo {}//the class 'Amigo' can't be extended, implemented, or mixed in outside of its library because it's a sealed clas
//sealed 类不能在文件外被继承
// 但这两个都是可以的：
class OtherLucky extends Lucky {} //sealed类的子类可以在类外被继承
class OtherDusty implements Dusty {}

main(){

}