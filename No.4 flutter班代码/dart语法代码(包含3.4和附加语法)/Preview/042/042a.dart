import 'poi/042b.dart';
//使用import关键字加上文件路径可以包含文件夹和其他文件,里面的类就可以被当前文件使用
main(){
   var p1 = Person042b();
   p1.showInfo();
}

class Person042a {
   String name = "张三";
   int age = 22;
   double height = 170;

   void showInfo() {
      print("name = $name age = $age height = $height");
   }
}
