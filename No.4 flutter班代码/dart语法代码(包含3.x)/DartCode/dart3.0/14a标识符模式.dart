main(){
  // 标识符
  // 例如
  // name 常量名称,在外面定义的const常量
  // _  通配符  ,匹配全部,并且不存储结果
  // 标识符模式在出现它们的上下文中可能像常量模式或变量模式一样行为

  const int c = 2;
  switch("asdfasdfsdaffd"){
    case c://标识符模式常量行为,只能匹配固定的值
      print("标识符模式常量行为c = $c");
    // case _:
    //   print("_");
    default :
      print("default");
  }
}