// 常量模式在值等于常量时匹配：
//123、null、'string'、math.pi、SomeClass.constant、const Thing(1, 2)、const (1 + 2)
// 例如我们在空检查里面无法匹配到null,但是常量模式可以匹配null
//可以作为常量模式的格式有:
// 数字字面量123、45.56
// 布尔字面量true
// 字符串字面量 'string'
// 命名常量(宏定义)   someConstant、math.pi、double.infinity
// 常量构造函数 const Point(0, 0)
// 常量集合字面量   例如List const []、  集合 const {1, 2}
// 更复杂的常量表达式必须用括号括起来，并加上 const 前缀const (1 + 2)
main() {
  // int? r = 1;
  // int? r = null;
  // int? r = 100;
  int? r = 3;

  constPattern(r);
}
constPattern(int? r){
  switch (r) {
    case 1: //常量模式匹配
      print("1");
    // case var s?:
    //   print("空检查匹配,只接受非空值 s=$s");
    case null://常量模式匹配
      print("null");
  case const (1 + 2):  //表达式需要用()括起来,并且外面加const
    print("匹配到 表达式 1+2");

  }
}
