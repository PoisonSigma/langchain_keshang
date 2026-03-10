main(){
  // 括号
  // 格式 (子模式)
  //
  // 与括号表达式类似，模式中的括号允许您控制模式优先级
  //
  switch (6) {
    case const ((1 + 2) * 2):
      print("6");
    case const (1 + 2 * 2):
      print("5");
  }
}