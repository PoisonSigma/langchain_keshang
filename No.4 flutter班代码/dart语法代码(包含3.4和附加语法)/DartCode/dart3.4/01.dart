/*
自己做的json转模型的工具：
https://gitee.com/wx18903612715/flutter-model-making-tool
*/

/*


# 使用json宏

 - 1
JsonCodable 宏尚不稳定，目前处于实验性标志后面。它仅适用于 Dart 3.5.0-152 或更高版本。这个版本可以从 Dart dev 通道或 Flutter master 通道获取。

- 2
 运行 dart --version 并确保你有 Dart 3.5.0-152 或更高版本。


- 3
pubspec 文件中编辑 SDK 约束以要求 Dart 版本：sdk: ^3.5.0-152


- 4
dart pub add json
- 5
analysis_options.yaml 文件中启用实验。文件位于项目根目录：
```
analyzer:
  enable-experiment:
    - macros
```

- 6
import 'package:json/json.dart';

- 7
 dart run --enable-experiment=macros 01.dart
 */
import 'package:json/json.dart';

import 'A2.dart';
@JsonCodable()
class Student{
  String name;
  int age;

  Student(this.name, this.age);
  /*
  //下面自己写toJson()方法是错误的,因为@JsonCodable() 帮我们写了这个方法
  toJson(){
  }
   */
  /*
  //命名构造函数fromJson也不能重写
  Student.fromJson(){
  }
   */
  //静态方法,跟命名构造函数重命,调用的时候 冲突
  // static fromJson(){
  // }

  @override
  String toString() {
    return 'Student{name: $name, age: $age}';
  }
}
main(){

  var s1 = Student("张三",18);
  //对象转Map  toJson()
  var jsonMap = s1.toJson();
  print("jsonMap = $jsonMap");
  print(jsonMap["name"]);
  print(jsonMap["age"]);
  /*
  //json字符串是key和 字符串的value是 带双引号的
  {
    "name": "张三",
    "age": 18
}
   */
  //fromJson    Map转对象
  var s2 = Student.fromJson(jsonMap);
  print("s2.toString() = ${s2.toString()}");
  print("s1.toString() = ${s1.toString()}");
  print("${s1.hashCode}");
  print("${s2.hashCode}");
  
   var a2 = A2.fromMap({"name":"li4","age":30});
   print(a2.toString());
  A2(name: "zhang3", age: 18);
}