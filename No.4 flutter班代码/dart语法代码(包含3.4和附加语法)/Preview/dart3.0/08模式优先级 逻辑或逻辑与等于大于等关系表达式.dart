main(){
  /*
    //模式优先级

  // 逻辑或 ||
  //
  // 逻辑或模式通过 || 将子模式分隔开，并在任何分支匹配时进行匹配。分支从左到右进行评估。一旦有一个分支匹配，其余的分支将不再进行评估。


  // var color = Color.red;
  var color = Color.gray;
  //这个例子判断如果是红黄蓝就 主色调就是true,其他情况为false
  var isPrimary = switch (color) {
  Color.red || Color.yellow || Color.blue => true,  //逻辑或,从左到有的顺序进行匹配,第一次发现匹配成功以后就不再继续匹配
  _ => false
  };
  print("isPrimary = $isPrimary");


   */
/*
  // 逻辑或模式通过 || 将子模式分隔开，并在任何分支匹配时进行匹配。分支从左到右进行评估。一旦有一个分支匹配，其余的分支将不再进行评估。
  var r1 = (1,2);
  switch(r1){
    // case (var a ,var b) ||  (var c ,var d) ://编译报错,c和d会失去匹配,因为 逻辑或运算左边第一个分支就匹配成功了.不会向右边匹配
    case (var a ,var b) ||(var a ,var b) ://绑定相同的变量编译正确,但是也只有 逻辑或左边的第一个分支会被匹配和解构,|| 逻辑或运算右边的分支不会被解构
      print("a = $a b = $b");
    case (1,2):
      print("这个case不会被匹配,因为上面的case匹配成功了,就会跳出switch");

  }
*/
/*
  // 逻辑与 &&
  // 由 && 分隔的一对模式仅在两个子模式都匹配时才匹配。如果左分支不匹配，则不会评估右分支。
  //但是每个子模式中的变量不能重叠，因为如果模式匹配，它们都将被绑定

  switch ((1, 2)) {
    case (var a, var b) && (var c, var d):
      print("a =$a b=$b c=$c d=$d"); //匹配,解构后分别绑定4个变量
  // 错误，两个子模式都尝试绑定 'b'。
  //   case (var a, var b) && (var b, var c): // 这个case被匹配以后,2个相同的变量b被绑定 ,错误是重定义
  }
*/

//关系
//   关系模式使用任何等式或关系运算符（==、!=、<、>、<= 和 >=）将匹配值与给定常量进行比较。
//   关系模式在匹配数字范围时特别有用，尤其是与逻辑与模式结合使用时：
//下面是ascII码表对应的数字
  String asciiCharType(int char) {
    const space = 32;
    const zero = 48;
    const nine = 57;

    return switch (char) {
      < space => 'control',  //小于空格返回空值
      == space => 'space',  //等于空格返回空格
      > space && < zero => 'punctuation',//空格到0之间返回标点
      >= zero && <= nine => 'digit',//0到9 返回数字
    
      _ => ''
    };
  }
}


enum Color{
  red,
  yellow,
  blue,
  gray//灰色非主色调
}