//dynamic类型是自动把2个变量按照实际传入的值,自动识别出2个类型,2个类型可以不同
String getStr1 ( row ,  line){
  print("row的类型是=${row.runtimeType}");//打印T的类型
  print("line的类型是=${line.runtimeType}");//打印T的类型
  return "位置在第$row行 第$line列";
}

//在功能上台,下面下面方法使用了泛型,跟上面的dynamic类型功能一样,但是泛型语法出现更早
//泛型的格式是<>尖括号里面放着类型
// 方法的()小括号前面加<>尖括号,里面是类型
//下面方法只给了一个泛型T,那么T的类型只能是一种,如果  row和line都用了一个T,那么如果传入的只都是int,T的类型就是int,如果传入了不同的类型,会变成Object
 String getStr2<T> (T row , T line){
  print("T=$T");//打印T的类型
   return "位置在第$row行 第$line列";
}
//允许使用多个泛型
String getStr3<T1,T2>(T1 row , T2 line){
  print("T1=$T1");//打印T的类型
  print("T2=$T2");//打印T的类型
  return "位置在第$row行 第$line列";
}
main(){

// 显示的在<>尖括号中指定类型,那么后面传入参数也要是这种类型
  var str =  getStr2<int>(3, 6);
  //已经在<>尖括号中显示的指定了int类型,传入的类型不是int,报错
  // str =  getStr<int>(3.1, 6.5);
  // The argument type 'double' can't be assigned to the parameter type 'int'. (Documentation)
  //参数类型double不能被复制到参数类型int

//下面没有在<>尖括号中指定类型,那么函数根据参数的实际类型自动变成这个类型
  //可以传入int类型
  str = getStr1(3, "abc");
  str = getStr2(3.1, 5.0);
  //传入String类型
   str = getStr2("甲", "丙");
   print(str);
   str = getStr2(3, "123");//Object类型


  str = getStr3(3, 5.0);

  List<int> l1 = [1,2,3]; //可以看到List的定义里面也有泛型<E>
  var l2 = [1,2,3,4];
}