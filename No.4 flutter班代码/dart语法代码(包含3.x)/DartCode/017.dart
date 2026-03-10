main() {
  List list = [1, 2, 3, 4, 5, 6];
  list[0] = 11;
  list[1] = 22;
  list[5] = 55;

  // print(list);

  // for(int i=0;i<list.length;i++){
  //   print("list[$i]=${list[i]}" );
  // }

  // for(var item in list){
  //      item = 1000;
  // }
  // print(list);
  for (int i = 0; i < list.length; i++) {
    list[i] = i + 1000;
  }
  print(list);
}
