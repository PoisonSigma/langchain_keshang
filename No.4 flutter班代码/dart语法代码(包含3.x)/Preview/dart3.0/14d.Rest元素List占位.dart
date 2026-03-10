main(){
  // 列表模式要求模式中的元素数量与整个列表相匹配。你可以使用 rest 元素作为占位符来处理列表中的任意数量的元素。
  // Rest 元素
  // 列表模式可以包含一个 rest 元素（...），允许匹配任意长度的列表。

    // var [a,b,c,d] = [1,2,3,4,5,6,7]; //运行错误,位数对不上
    // print("$a $b $c $d");
    // var [a,b,_,_,_,c,d] = [1,2,3,4,5,6,7];  //需要3个下划线通配符才能解构,总体位数必须对上.不能接受任意位数

  // var[a,b, ..., c,d] =[1,2,3,4,5,6,7]; //正确 使用 ... 占位符可以是占位任意长度.12,  67向左右两边顶头,中间用...占位
  // print("$a $b $c $d");


  //创建rest变量,用来存储新的List,格式 ...加变量名
  // var [a1,b1,...rest,c1,d1] = [1,2,3,4,5,6,7];
  //   print("$a1 $b1 $c1 $d1");
  //   print("rest = $rest");

    var list2 = [1,2,3,4,5,6,7];


    const a2 = 1;
    const b2 = 2;
    const c2 = 6;
    const d2 = 7;
    const rest2 = [3,4,5];
    switch(list2){
      case [a2,b2, ...var rest,c2,d2 ]:  //先匹配List模式,再匹配常量子模式,接受固定的常量[1,2,3,4,5,6,7]
        print("$a2 $b2 $c2 $d2");
        print("rest = $rest");

        //把rest元素用在变量模式中匹配
        // case  [var a,var b,...var rest,var c, var d]:  //先匹配List模式,再匹配变量模式 ,中间的rest占位,可以接受任意数组
        //  print("switch 中的 匹配");
        //   print("$a $b $c $d");
        //   print("rest = $rest");

    }
}