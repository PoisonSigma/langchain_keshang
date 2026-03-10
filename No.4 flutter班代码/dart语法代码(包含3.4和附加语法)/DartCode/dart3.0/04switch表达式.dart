/*
Switch表达式
Switch表达式根据匹配的case表达式体生成一个值。你可以在Dart允许表达式的任何地方使用switch表达式，除了在表达式语句的开始位置。例如：

dart
Copy code
var x = switch (y) { ... };

print(switch (x) { ... });

return switch (x) { ... };
如果你想在表达式语句的开始位置使用switch，请使用switch语句。

Switch表达式允许你重写类似下面这样的switch语句：

dart
Copy code
// 其中slash、star、comma、semicolon等是常量变量...
switch (charCode) {
  case slash || star || plus || minus: // 逻辑或模式
    token = operator(charCode);
  case comma || semicolon: // 逻辑或模式
    token = punctuation(charCode);
  case >= digit0 && <= digit9: // 关系和逻辑与模式
    token = number();
  default:
    throw FormatException('Invalid');
}
成为一个表达式，如下所示：

dart
Copy code
token = switch (charCode) {
  slash || star || plus || minus => operator(charCode),
  comma || semicolon => punctuation(charCode),
  >= digit0 && <= digit9 => number(),
  _ => throw FormatException('Invalid')
};
Switch表达式的语法与switch语句的语法有所不同：

case不以case关键字开头。
case体是一个单一表达式，而不是一系列语句。
每个case必须有一个体；空的case没有隐式的穿透。
case模式与其体之间使用=>而不是:分隔。
case之间使用,分隔,可以写在一行
默认case只能使用_，而不允许同时存在default和_。
版本说明：Switch表达式需要至少3.0的语言版本。
 */
main() {
  //switch表达式 不能放在开头
  var a = 2;
  // var x = 0;
  var x = switch (a) {
    10 => "匹配到10xxx", //case之间使用,分隔 //switch表达式的语法是,把case省略
    10 || 20 || 30 => "匹配到10 20 30", //case之间使用,分隔,可以写在一行
  // default => "默认情况2",//默认case只能使用_，而不允许同时存在default和_。
    > 1 && < 10 => "2到9之间",
  //  20,不支持隐式穿透
  // 30=>"20 30",
    _ => "默认情况" // 因为=>箭头函数是返回这一行,那么就是把这一行赋值给 x,每一个case的匹配语句结尾用逗号隔开
  };
  switch (5) {
    case > 1 && < 10:
      print("switch 语句2到9之间");
  };
  /*
  print( switch (a) {
    10 => "匹配到10xxx",
    _=> "默认情况"
  });

   */
  print("x=$x");
  //  var result = test1();
  //  print(result);

  //switch语句可以隐式穿透
  switch(50){
    case 10:
    case 20:
    case 30:
      print("匹配到10 20 30");
  }

}

test1() {
  return switch (20) {
    10 => "匹配到10xxx", _ => "默认情况"
  };
}
