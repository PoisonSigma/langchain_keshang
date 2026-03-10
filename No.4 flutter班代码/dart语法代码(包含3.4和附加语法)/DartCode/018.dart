main(){
  // List.generate 生成数组
  //参数1,序号,自动生成的index是每次遍历出来的序号. =>右边是一个表达式, 表达式计算的值用来填充到List中
  //这个例子,序号是[0,1,2,3,4] ,右边表达式,把序号index*2, 那么就是 [0,2,4,6,8];
  //  var list1 = List.generate(3, (index) => "str"); //[0,1,2] ["str","str","str"]
  //  print(list1);
  //  var list2 = List.generate(3, (index) => index*2);//[0,1,2] [0,2,4]
  //  print(list2);


  //...3个点的作用是拆掉一层[],把...后面的数组变成了元素,相当于是把1维数组变成了连续排列的一串元素
  //例如: [1,2,3]  使用...以后 就变成了:1,2,3

   List <int> list3 = [  ...[1,2,3], 4,5,6];
   // print(list3);
  var list4 = [7,8,9];
   List<int> list5 = [1,2,3,...list4];
   // print(list5);

   List <int> list6 = [...[1,2,3],4,5,6 ];

   List<int> list7 = [999,999, ...List.generate(10, (index) => index)  ];
   print(list7);
}