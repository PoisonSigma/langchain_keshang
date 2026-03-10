main() {
  //模式优先级

  // 逻辑或 ||
  //
  // 逻辑或模式通过 || 将子模式分隔开，并在任何分支匹配时进行匹配。分支从左到右进行评估。一旦有一个分支匹配，其余的分支将不再进行评估。
  // var color = Color.red;
  /*
  var color = Color.gray;
  var isPrimary = switch(color){
    Color.red || Color.yellow || Color.blue => true,//逻辑或,从左到有的顺序进行匹配,第一次发现匹配成功以后就不再继续匹配
      _=>false
  };
  print("isPrimary = $isPrimary");

   */
  /*
  // 逻辑或模式通过 || 将子模式分隔开，并在任何分支匹配时进行匹配。分支从左到右进行评估。一旦有一个分支匹配，其余的分支将不再进行评估。
  var r1 = (1,3);
  switch(r1){
    // case (var a,var b) || (var c ,var d): //编译报错,c和d会失去匹配,因为 逻辑或运算左边第一个分支就匹配成功了.不会向右边匹配
    //   print("错误");
    case (var a,var b) || (var a,var b):
      print("a = $a b = $b");
  }
   */
  // 逻辑与 &&
  // 由 && 分隔的一对模式仅在两个子模式都匹配时才匹配。如果左分支不匹配，则不会评估右分支。
  //但是每个子模式中的变量不能重叠，因为如果模式匹配，它们都将被绑定
  /*
  bool a = true;
  bool b = false;
  bool c = true;
  switch((1,2)){
    case (var a,var b) && (var c,var d ,var e):
      print("a=$a b = $b c=$c");
    // case (var a,var b) && (var c,var d )://匹配,解构后分别绑定4个变量
    //   print("a=$a b = $b c=$c d = $d");//匹配成功以后直接跳出switch
    case (var a,var b) && (var a,var c ) && (var e,var f ): //编译错误,重定义,每个子表达式不能有左边相同的变量
      print("a=$a b = $b c=$c ");
  }
*/
  //关系
//   关系模式使用任何等式或关系运算符（==、!=、<、>、<= 和 >=）将匹配值与给定常量进行比较。
//   关系模式在匹配数字范围时特别有用，尤其是与逻辑与模式结合使用时：
//下面是ascII码表对应的数字
  asciiCharType(int char) {
    const space = 32;
    const zero = 48;
    const nine = 57;

    return switch (char) {
      < space => "control",
      == space => "空格",
      > space && < zero => "标点符号",
      >= zero && <= nine => "数字",
      _ => "其他情况"
    };
  }

  print(asciiCharType(58));
}

enum Color {
  red,
  yellow,
  blue,
  gray //灰色非主色调
}
