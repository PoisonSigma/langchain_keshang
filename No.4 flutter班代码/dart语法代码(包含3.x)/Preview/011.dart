main(){
  /*
  //List通过中括号来创建数组,中括号中没有任何元素,并且不指定任何类型
  List<int> l0a = [];
  l0a.add(1);
  l0a.add(2);
  l0a.add(100);
  print("l0a=$l0a");

  var l0b = [];  //注意不写任何类型,相当于是<dynamic>类型:List<dynamic> l0
  l0b.add(1);
  l0b.add("abc");
  print(l0b);


  var l0c = <dynamic>[];  //上面写完整相当于<dynamic>的泛型, dart中 dynamic可以省略
  l0c.add(1);
  l0c.add("xyz");
  print(l0c);

  var l0d = [1,2,3];//这里右边都是int类型的元素,所以左边var会自动推导出List是int类型 List<int>
  print(l0d);
  //List 也可以创建的时候直接在[]中括号中设置元素
  var l1 = [1,"abc",true];
  l1.add("xyz");
  print(l1);


   //List创建并且指定类型下面的尖括号<>是泛型的意思,是可以指定类型,泛型在之后会讲到,指的是,List的类型可以被设置,但是需要通过泛型<类型>来手动设置
  var l2 = <int> [123,456,789];
  //add在List结尾添加元素
  l2.add(100);
  //l2.add("abc");//报错,因为指定了int的类型,所以不能add添加字符串类型的元素
  print(l2);

  var l2str = <String>["abc","bcd"];
  l2str.add("xyz");


  //addAll方法,批量添加
  var l3a =<dynamic> [1,2,3];  //注意这里之所以写<dynamic>是因为如果不写,右边因为是3个相同的int,l3a会被自动推导处事List<int>
  var l3b = ["abc","xyz"];
  l3a.addAll(l3b);
  print("l3a=$l3a");



  //filled 填充,第一个参数是填充多少个,第二个是填充元素,重复填充
  var l4 = List.filled(5, 1);
  print(l4);
  var l4str = List.filled(6, "A");
  print(l4str);


  //insert插入,参数一是序列,从0开始
  var l5 = [1,2,3,4];
  l5.insert(1, 999);//在第1的位置插入999,结果是1,999,2,3,4
  print(l5);


  //insertAll批量插入,参数1是插入位置,参数而是被插入的数组
  var l6a = [1,2,3,4];
  var l6b = [7,8,9,10];
  l6a.insertAll(1, l6b); //在数组1的位置插入整个的l6b
  print(l6a);

  //remove删除指定的值
  var l7 = [1,2,3,4,5];
  l7.remove(3);
  print(l7);

  var l8 = [1,2,3,4,5];
  l8.removeAt(2);//删除序列2的元素,从0开始数,0,1,2,就是删掉元素3,剩下:1,2,4,5
  print(l8);

  //removeRange,参数1,开始删除的序列,参数2,直到删除到参数2的前一个序列
  var l9 = [1,2,3,4,5];
  l9.removeRange(1, 3);//删掉序列 1, 到 3-1 ,那么就是删除掉序列 1,2 :剩下1,4,5
  print(l9);

  //删掉最后一个
  var l10= [1,2,3,4,5];
  l10.removeLast();
  print(l10);

  //isEmpty判断是否为空
  //isNotEmpty判断是否不为空
  var l11 = [];
  print(l11.isEmpty);
  print(l11.isNotEmpty);

  //reversed,返回倒叙的迭代器Iterable<int>,可以理解为就是一个排序,一般不直接使用,用到的时候会告诉大家,我们只需要记住,List.reversed改变顺序的时候,再用toList就可以了
  var l12 = [1,2,3];
   var l12b = l12.reversed;
   print("l12b=$l12b");
   //toList方法把迭代器Iterable转换为List
   var l12c = l12b.toList();
   print("l12c=$l12c");
   //下面是通常用法把reversed.toList()连用,只需要注意迭代器,打印出来的是()小括号,我们使用的数组List是中括号[],把()小括号转换为[]中括号的方法是使用toList方法

  var l12d = l12.reversed.toList();
  */
  
  //map方法,等我们讲完匿名函数和箭头函数会对map后面的(){}这种匿名函数更加理解,现在只需要记住这种固定格式,这个List.map之所以放在这里,是为了大家以后复习或者查找list方法的时候可以直接在这里找到
  //List.map()方法,映射, ()括号里面的参数,是每次遍历数组里的元素,而右边的 =>箭头符号 右边的表达式是 一个闭包的缩写方法: 意思是return e+1
  //注意map()方法返回的也是一个迭代器操作Iterable,要把他存到新的list中要使用toList()方法
  var l14 = [1,2,3];
  l14.map((e){
    return e+1;
  });
  print(l14); //注意,直接打印l14,发现并没有变化,因为.map方法是有返回值的
  var l14b = l14.map((e){
    return e+1; //这局话的意思是每次从数组里面遍历,取出一个1,2,3的一个数字,例如第一次取出来1,那么把1当做参数e,
    // 进行计算 e+1 就是1+1,return回去,存入到左边的数组l13中,
    // 下次遍历到2,就是return 2+1 =3 ,返回到左边的数组中,最后遍历到3,3+1,返回到左边的数组中,最终左边的l13的数组变成了[2,3,4]

  });
  //
  print(l14b);//l14b是迭代器()小括号
  var l14c = l14b.toList();
  print(l14b.toList());//返回的是

  //当=>箭头右边只有一句话的时候可以省略{ } 和 里面的return关键字

  /*
  (){
    return a;
  };
  等价于
  ()=>a;
   */

  var l14d = l14.map((e) => e+2);

  //
  var l15 = [1,2,3];
   l15.map((e){
    print("l5的map方法执行了");
    return e+1;
  });//这里因为map是放回的迭代操作,不会被执行,需要遇到toList才会执行
  var l16 = [1,2,3];
  l15.map((e){
    print("l16的map方法执行了");
    return e+1;
  }).toList();//只要遇到toList就会执行

}