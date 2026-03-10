import"StringA.dart" as M1;
import"StringB.dart" as M2;
main(){
  // var i3 = "123".parseInt();
  var i1 =M1.StringA("123").parseInt();//调用格式:前缀.扩展名( 变量),像构造函数调用一样.点方法
  var i2 = M2.StringB("456").parseInt();
  print(i1);
  print(i2);

}