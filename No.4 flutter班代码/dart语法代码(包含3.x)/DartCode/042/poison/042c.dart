import '../042b.dart';

class Person042c {
  String name = "张三";
  int age = 22;
  double height = 170;
  int year = 0;

  void showInfo() {
    print("name = $name age = $age height = $height year = $year");
  }
}

main(){
   var p1 = Person042b();
   p1.showInfo();
}