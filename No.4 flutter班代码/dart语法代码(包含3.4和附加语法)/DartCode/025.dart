main() {
  //is运算符可以判断一个变量是否属于一个类型或者他的子类型
  // is!跟is完全相反,当 运算符is!左边的变量不属于右边的类型,或者不属于右边的子类型,才返回ture
  var str = "100"; //"123";
  // if(str is String){
  //   print("str 是String类型");
  // }else if(str is int){
  //   print("str 是int类型");
  // }
  if (str is! String) {
    print("第1行");
  } else if (str is! int) {
    print("第2行");
  }

  //is运算符,左边如果是右边的子类,也返回true ,这里没有其他语言基础的可以理解为,类也是一个类型,而继承父类,父类是他的爸爸,听不懂,到后面也会讲
//在这里引入类的概念,是为了让大家先知道is可以判断类
  if (str is Object) {
    print("是Object");
  } else {
    print("不是Object");
  }
  
}
