main(){
  var l1 = [1,2,3,4,5,6,77];
  //forin遍历删除的注意事项
  /*
  //错误的示范
  for(var item in l1){
          // l1.remove(3);//forin 中间的元素不能删除
    // l1.remove(77);//报错
    // l1.remove(78);//删除一个不存在的可以
    if(item == 88){
      l1.remove(item);
    }
  }
  */

  // var l2 = l1;//这样还是同一个队列
// var l2 = l1.toList().toList();//可以无限的toList()

// print(l1.hashCode);
//   print(l2.hashCode);
  var l2 = l1.toList();
  for(var item in l2){
    // l1.remove(3);//forin 中间的元素不能删除
    // l1.remove(77);//报错
    // l1.remove(78);//删除一个不存在的可以
    if(item == 3){
      l1.remove(item);
    }
  }
print(l1);
  print(l2);
/*
  //for循环可以删除
   for(int i = 0 ;i<l1.length;i++){
        l1.remove(1);
   }
   print(l1);

 */
}