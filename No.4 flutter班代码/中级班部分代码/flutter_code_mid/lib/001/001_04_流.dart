main(){
  //通过迭代操作,创建一个流
   var s1 = Stream.fromIterable([1,2,3,"a","张三"]);//通过迭代操作,创建一个流,fromIterable 创建的流，它会立即完成，
  // 所以 "Stream is done" 会在 "Subscription canceled" 之前打印。
  print(s1);
  s1.listen((v){
    print("v=$v");
  },
    onDone: (){
      print("结束,订阅被取消");
    }
  );
}