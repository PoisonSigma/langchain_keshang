import "063a.dart";
main(){
  // var p1 = Person._init("abc");//文件外,不能调用私有方法
  // print(p1);
  var p2 = Person("张三");
  p2.showInfo();

  var p3 = Person("张三");
  p2.showInfo();
  print(identical(p2, p3));
}