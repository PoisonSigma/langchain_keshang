main(){
  //...3个点的作用是拆掉一层[],把...后面的数组变成了元素,相当于是把1维数组变成了连续排列的一串元素
  //例如: [1,2,3]  使用...以后 就变成了:1,2,3


//下面list1指定了泛型int,只能房int 而[1,2,3]本身也是一个List类型,不是int类型,所以不能直接放到list1中,需要用...给数组拆解成元素
  List <int> list1 = [  ...[1,2,3], 4,5,6];
  print(list1);
    List list2 = [1,2,3];
  list1 = [ ...list2,4,5,6 ];
  print(list1);

  // List.generate 生成数组
  //参数1,序号,自动生成的index是每次遍历出来的序号. =>右边是一个表达式, 表达式计算的值用来填充到List中
  //这个例子,序号是[0,1,2,3,4] ,右边表达式,把序号index*2, 那么就是 [0,2,4,6,8];
  var list3 = List.generate((5), (index) => index*2);
  print(list3);

  //这里面虽然序列生成了 [0,1,2],但是箭头函数右边的表达式,并没有使用index,而是每次运算结果都是固定的"str"字符串,所以生成[str, str, str] 类型是 List<String>
  var list4 =  List.generate(3, (index) => "str");
  print(list4);

  List<int> list5 = [999,999,... List.generate(10, (index) => index)];
  print(list5);
}