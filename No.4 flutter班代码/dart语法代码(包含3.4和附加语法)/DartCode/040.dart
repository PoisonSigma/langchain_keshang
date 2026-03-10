//静态方法是类所拥有的方法,不需要创建对象就能访问,可以访问静态成员变量,不能访问普通成员变量
//静态成员变量属于类所拥有的成员变量,不能被对象访问
//当我知道这个类下,他的某个属性,所有对象都一样,那他可以作为静态成员变量,所有对象的操作也都相同,那就可以作为静态方法

class StudentMiddleSchoolOne{
  String name = "张三";
  int age = 22;
  double height = 170;
  static String timeForSchool = "6:30";
  static showTime(){
    print("上学时间是 $timeForSchool");
    return 1;
  }
}
main(){

   StudentMiddleSchoolOne.timeForSchool = "7:30";
  var p1 = StudentMiddleSchoolOne.showTime();//静态方法调用的时候是 类名.方法名, 像是命名构造函数,但是不能创建对象
   //返回的是静态方法返回的值

  print(p1);
  //错误,对象不能访问静态方法
  var p2 = StudentMiddleSchoolOne();
  // p2.showTime();
//错误,对象不能访问静态成员变量
// p2.timeForSchool;

}