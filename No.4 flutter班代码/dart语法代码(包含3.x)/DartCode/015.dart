main() {
  //++和--操作,变量自己增加1,和自己减少1
  int i = 0;
  // print(i);
  // i++;
  // print(i);
  // i--;
  // print(i);
  // print(i++);//先执行了打印i的值,然后+1
  // print(i);
  //  print(i--);
  // print(i);

  // i++;
  // print(i);
  // print(i);
  // ++i;
  // print(i);
  // print(++i);//先执行让i+1,然后再打印.
  // --i;
  // print(i);
  // print(--i);

  //注意,一般情况下,怕其他程序员看代码麻烦,尽量不是用i++和其他表达式放在一起使用.可以单独让i++单独成为一行代码,或者使用++i;
  //1.像其他语言那样的for循环
  //括号里面 的3个表达式,用2个分号分开
  //第1个位置是定义一个变量,用来计数值
  //第2个表达式是判断是否结束循环的条件
  // //第3个表达式,通常用做计数器的增加减少,在每次循环里面的结尾执行
  // for(int i=0 ;i<3 ;i++){
  //     print(i);
  // }
  // for(int i=100;i>0;i--){
  //   print(i);
  // }

  //2.for in, in的左边,是每次遍历循环的时候取出来的元素. in右边是一个数组
  // List list = [1,2,5,6,7];
  // for(int item in list ){
  //   print(item);
  // }
  // List list2 =["abc","xyz","123",1230];
  // for(var item in list2){
  //   print(item);
  // }

//while循环,当()里的表达式成立,就执行{}里的循环代码
//   i = 0;
//    while(i>0){
//      print(i);
//      i--;
//    }
  // do while,先执行{}里的表达式,再判断while()括号里的条件
  i = 0;
  do {
    print(i);
    i--;
  } while (i>0);
}
