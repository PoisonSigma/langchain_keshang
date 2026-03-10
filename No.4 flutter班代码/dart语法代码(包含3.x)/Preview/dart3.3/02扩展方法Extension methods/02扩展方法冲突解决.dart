// import 'StringA.dart' as M1;//用as添加前缀  使用方法  M1.StringA("123").parseInt();
// import 'StringB.dart' as M2 ;//用as添加不同的前缀
import 'StringA.dart';
import 'StringB.dart' hide StringB;//两个扩展里面有相同的 方法名,用hide 隐藏一个 扩展名
main(){
int i1 = "abc".parseInt();//隐藏A以后只剩下B
  print(i1);

  /*
  //添加前缀用法特殊:
  int a = M1.StringA("123").parseInt();
  int b = M2.StringB("abc").parseInt();
  print(a);
  print(B);

   */
}
