main() {
  List list = [1, 2, 3, 4, 5];
  for(var item in list){
       print("遍历数组:$item");
  }

  //
  list[0] = 11;
  list[4] = 99;
  // list[5] = 100;//报错,超过长度了
  for(int i=0;i<list.length;i++){
    print(list[i]);
  }

  // for(var item in list){
  //   item = 11;//不会改变list的值
  //   // print("item=$item");
  // }
  // print(list);
  for(int i=0;i<list.length;i++){
    list[i] = i+1000;//改变list的值
  }
  print(list);
}