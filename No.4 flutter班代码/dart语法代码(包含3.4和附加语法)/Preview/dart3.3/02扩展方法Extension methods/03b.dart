import "03未命名扩展Unnamed extensions.dart";
import "03未命名扩展Unnamed extensions.dart" as M3;
import "StringA.dart";
main(){
  // M3.StringA("123").parseInt();//普通的有名字的扩展方法
  
  // int a = "123".parseIntUnamed();//报错,找不到定义,未命名的扩展方法不能被包外调用
}