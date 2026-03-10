// 因为可选类型不能进行 运算,例如 判断是否 >60,所以用 !强制解包,把 可选类型变成普通的非空类型
// !强制解包,把可选类型变成非可选类型,例如把String?变成String,把int? 变成int但是如果可选类型里面保存的值是null,那么运行报错
//把可选类型当做函数形参
fn1(int? score) {
  try {
     score!;//强制以后变成了非空类型int
     score!;//错误,已经强制解包变成int了,再强制解包出错
    if (score > 60) {
      print("及格");
    } else {
      print("不及格");
    }
  } catch (e) {
    print(e);
  }
  //注意如果直接给可选类型赋值一个非可选类型的字面量,那么不能使用!强制解包,因为这个变量已经不会再变成可选类型,运行会警告,找不到null
  score = 0;
  var s2 = score;//注意这里编译器已经知道score就是int类型了,所以var推断出来的s2,自动就是int类型,而不是?类型
  int? i1;
  var i2 = i1;//这里推断出来i2是int类型
  int? i3 = 123;
  var i4 = i3;//这里推断出i4是int类型

  // score!;//这里运行错误,因为上面已经给score赋值了0,那么编译器已经把score当做int类型来看,再运行!强制解包,运行会出警告
  //Warning: Operand of null-aware operation '!' has type 'int' which excludes null.
  //警告:空感知操作的操作数!的类型int不包含null
  //注意这里之所以会报错,因为score已经是字面量0,就变成了int类型,往下执行也不会有null值出现
  //注意这种警告是flutter3.0现在的版本有,也许以后这种警告会消失,例如swift中遇到这种情况就不会警告
}


fn2(String? str){
  //双冒号?? 运算符,代表,如果?? 左边是null,那么就返回右边的值,如果左边不是null,那么就返回左边的值
  //str.isEmpty;//注意可选类型不能直接使用在String的方法,需要先转化成String类型
  //var str2 = str!;//之前我们用强制解包,但是如果遇到null就会中断,需要用try catch来捕获异常
  var str2 = str ?? "默认值";  //这个代码没用try catch也没有中断,因为没有强制解包出null值,这个代码是遇到左边str为null就自动返回右边的值了.
  print("str2=$str2");

  //需要注意的点,如果给可选类型,直接赋值字面量"字符串",那么运行会出现警告,提示??操作符发现没有找到null:
  str = "abc";
  // var str3 = str ?? "默认值";//运行到这里会有警告,不影响运行,但是非常经典的警告:
  // Warning: Operand of null-aware operation '??' has type 'String' which excludes null.
  // 空感知操作符 ?? 的类型是String 不包含null,因为这里上面明确看到复制了字面量"字符串"
  //跟上面函数fn2(String? str)的区别是,str有可能传入null也有可能传入String,但是 上面代码赋值 = "abc"以后,abc已经永远变成了不会变成null的String类型
  //所以编译器出现警告,不影响运行
  //解决这种警告的方法是,去掉??
  var str4 = str;//这里var自动推断除了String类型,而不是String?类型,因为上面,我们明确告诉编译器str = "abc"
  str4.isEmpty;//String类型可以直接运行String方法
}
fn3(String? str){
   str?.isEmpty;// ?运算符,可以直接让可选类型执行非可选类型的方法,如果str不是null就执行String的方法,如果是null就不执行返回null
  var r = str?.isEmpty;  //这里返回的结果也是可选类型,因为 ?.遇到null就不执行了,那么返回的也是null
  print("r=$r");

  //如果遇到想让上面的保存结果r不是可选类型,可以联合 ??给出默认值
  var r2 = str?.isEmpty ?? false; //如果str是null,那么左边就不执行了返回null, 那么??左边就是null,所以返回了右边的false赋值给r2

}
main() {

  fn1(null);
  // fn2("abc");
  // fn2(null);//传入null的时候没用try
  // fn3("123");
  // fn3(null);





}



