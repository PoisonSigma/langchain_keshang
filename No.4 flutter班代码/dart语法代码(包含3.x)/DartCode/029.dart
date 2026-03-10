// 因为可选类型不能进行 运算,例如 判断是否 >60,所以用 !强制解包,把 可选类型变成普通的非空类型
// !强制解包,把可选类型变成非可选类型,例如把String?变成String,把int? 变成int但是如果可选类型里面保存的值是null,那么运行报错
//把可选类型当做函数形参
/*
try{
//容易出错的代码
}catch(e){
//出错后执行的代码
}
 */
fn1(int? score) {
  //强制解包
  try {
    score!; //当强制解包里面存的值是null的时候,就会程序中断.
    if (score > 60) {
      print("及格");
    } else {
      print("不及格");
    }
  } catch (e) {
    print("e=$e");
  }

  var s2 = score;//上面的强制解包在try里面,作用于不一样,这里score没有去掉null,还是可选类型
  //注意如果直接给可选类型赋值一个非可选类型的字面量,那么不能使用!强制解包,因为这个变量已经不会再变成可选类型,运行会警告,找不到null
  score = 100;
  // score!;//这里运行warning警告,因为上面已经给score赋值了0,那么编译器已经把score当做int类型来看,再运行!强制解包,运行会出警告
  //Warning: Operand of null-aware operation '!' has type 'int' which excludes null.
  //警告:空感知操作的操作数!的类型int不包含null
  //注意这里之所以会报错,因为score已经是字面量0,就变成了int类型,往下执行也不会有null值出现
  //注意这种警告是flutter3.0现在的版本有,也许以后这种警告会消失,例如swift中遇到这种情况就不会警告
  // score!;
}

//双冒号?? 运算符,代表,如果?? 左边是null,那么就返回右边的值,如果左边不是null,那么就返回左边的值
//str.isEmpty;//注意可选类型不能直接使用在String的方法,需要先转化成String类型
//var str2 = str!;//之前我们用强制解包,但是如果遇到null就会中断,需要用try catch来捕获异常
fn2(String? str){
  var str2 = str ?? "默认值";
  print("str2=$str2");

  str = "abc";
  str;//这里已经变成了String
  // var str3 = str ?? "默认值";//这里因为str是String所以不能用 ??去运算,会有警告Warning: Operand of null-aware operation '??' has type 'String' which excludes null.
}

// ?.运算符,可以直接让可选类型执行非可选类型的方法,如果str不是null就执行String的方法,如果是null就不执行返回null
fn3(String? str){
  // var r1 = str?.isEmpty ;
  var r1 = str?.isEmpty ?? false;
  print("r1=$r1");
}
main() {
  // fn1(null);
  // fn1(100);
  // int? i1 ;
  // // i1 > 100;
  // var i2 = i1;
  // fn2("abc");
  // fn2(null);
  fn3("abc");
  fn3(null);
}
