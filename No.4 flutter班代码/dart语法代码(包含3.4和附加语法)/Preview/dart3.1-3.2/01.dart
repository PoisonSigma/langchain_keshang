/*
Dart 3.1没有添加任何新功能，也没有对语言做任何更改。
Dart 3.2
Dart 3.2增加了对流分析的增强，包括：

扩展了类型推断以在私有final字段上工作。
以前仅适用于局部变量和参数，现在私有final可以通过空检查和is测试提升为非空类型。例如，现在以下代码是正确的：

class Example {
  final int? _privateField;

  Example(this._privateField);

  void f() {
    if (_privateField != null) {
      // _privateField已经被推断为非空类型；您可以在不进行空检查的情况下使用它。
      int i = _privateField; // OK
    }
  }
}

// 私有字段的推断也可以在类外部起作用：
void f(Example x) {
  if (x._privateField != null) {
    int i = x._privateField; // OK
  }
}
有关私有最终字段何时可以推断类型和何时无法推断类型的更多信息，请查看“修正类型推断失败”。

纠正了if-case语句中与被匹配值的类型推断行为不一致的问题，当被匹配值引发异常时。
 */
main(){

}
void fun1(String? str){
  if (str != null){
    String str2 = str;//普通函数中,可选类型可以类型推断.变成非空类型
  }
  if(str is String){
    String str2 = str;//is 类型推断变成非空类型
  }
}

class Example {
  final int? _privateField;
  final int? age;//final 非私有成员
  String? name;
  Example(this._privateField,this.age,this.name);

  void f() {
    if (_privateField != null) {  //这句话 != null 在dart 3.2之前 不能把私有字段推断成 非空类型
      // _privateField已经被推断为非空类型；您可以在不进行空检查的情况下使用它。
      int i = _privateField; // OK 这段代码只有在 dart 3.2以上有效,低于3.2会报错
      /*
      类型为` int?`不能被赋值给类型为` int `的变量。
` _privateField `不能被提升，因为字段提升仅在Dart 3.2及更高版本中可用, dart sdk文件超过3.2就行,再把pubspec.yaml文件中改成environment:
  sdk: '>=3.2.0'
       */
    }
    if (_privateField is int){ //dart 3.2 通过is把 私有final 类型推断成非空类型
      int i = _privateField;
    }

    if(age != null){
      // int i =  age;//final 非私有成员不能被类型提升
    }


    if(name != null){
      // String str = name;//报错dart 3.2之前,普通的可选类型也不能被类型推断
    }
  }
}

// 私有字段的推断也可以在类外部起作用：
void f(Example x) {
  if (x._privateField != null) {
    int i = x._privateField; // 在类外面,在同一个文件下,访问私有final成员,推断成 非空类型
  }
}