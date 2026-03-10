main(){
  // 列表模式要求模式中的元素数量与整个列表相匹配。你可以使用 rest 元素作为占位符来处理列表中的任意数量的元素。
  // Rest 元素
  // 列表模式可以包含一个 rest 元素（...），允许匹配任意长度的列表。
  // var [a,b,c,d] = [1,2,3,4,5,6,7];
  // print("$a $b $c $d");

  //创建rest变量,用来存储新的List,格式 ...加变量名
  // var [a,b, ...rest1,c,d] = [1,2,3,4,5,6,7];
  // print("$a $b $c $d");
  // print(rest1);

  // var [a,b, _,_,_,c,d] = [1,2,3,4,5,6,7];//需要3个下划线通配符才能解构,总体位数必须对上.不能接受任意位数
/*
  var list = [1,2,3,4,5,6,7,8,9,10,11,12];
  const a = 1;
  const b = 2;
  const c = 6;
  const d = 7;
  const rest2 = [3,4,5];
  switch(list){
    case [a,b,...var rest,c,d]:
    print("$a $b $c $d");
    print(rest);
    case [var a,var b,...var rest,var c,var d]:
      print("外层List模式 子模式变量模式 ,加 rest元素占位$a $b $c $d");
      print(rest);
  }
*/
  var list2 = [1,2,3,4,[5,6,7],8,9];
  var list3 = [1,2,3,4,...[5,6,7],8,9]; //数组降维,把2维度数组,变成1维.  3个点把[]打开,放到了1维数组中[1, 2, 3, 4, 5, 6, 7, 8, 9].  swift  flatMap
  print(list3);
}
