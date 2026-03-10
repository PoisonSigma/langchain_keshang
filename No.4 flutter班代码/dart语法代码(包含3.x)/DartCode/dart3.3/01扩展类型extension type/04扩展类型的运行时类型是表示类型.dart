// 扩展类型的运行时类型是它的表示类型
// 通过下面语法调用表示类型的方法
// is
// if case
// switch case

extension type IntId(int value){

}
main(){
      var i = IntId(100);
      // i + 10;//报错,静态分析期间, i不会被发现是它的表示类型
      if (i is int ){
        print( i.runtimeType);
        int t1 = i as int;
        t1 + 10;
      }

      if(i case int x ){ //i 运行时候的类型是int  ,x匹配到的值也是 int类型的值
         x + 10;//可以调用int下的+操作符
        print(x+100);
         print( i.runtimeType);
      }
      switch (i){
        case int x:
          print(x + 10);
          print( i.runtimeType);
      }
}