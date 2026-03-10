

import 'package:json/json.dart'; //为了使用@JsonCodable()
/*
注意这里的运行,要使用实验性运行,而不是普通的dart run
dart run --enable-experiment=macros 01JsonCodable宏.dart
 */

@JsonCodable()
class Student {
  final String name;
  final int age;
  Student(this.name, this.age);
  //下面自己写toJson()方法是错误的,因为@JsonCodable() 帮我们写了这个方法
  /*
  toJson(){
  }
   */

  //fromJson也不能重写
  /*
   Student.fromJson(String str){
  }
   */
  //下面静态方法不能手写,跟命名构造函数Student.fromJson 冲突
  /*
  static fromJson(){
  }
   */
  @override
  String toString() {
    return 'Student{name: $name, age: $age}';
  }
}
void main() {
  var jsonStr = Student("zhang3", 18).toJson();
      // .toJson();
  print('json字符串是: $jsonStr');

  //Json字符串转模型对象
  var s1 = Student.fromJson(jsonStr);
  print("s1 = ${s1.toString()}");

}
