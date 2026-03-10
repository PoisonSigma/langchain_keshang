add (int a,int b){
   print("add()执行 a+b= ${a+b}");
}
int add2 (int a,int b){
  print("add()执行 a+b= ${a+b}");
  return a+b;
}

//使用typedef 定义一个函数类型,c++的函数签名
typedef Add = int  Function  (int ,int );
main(){
     // add(1, 3);
     Function fn1 = add;
     fn1(1,5);
     // fn1(1,2,3);

     //给Function指定类型
     Function  (int,int) fn2 = add;
     // fn2(1,2,3);
    fn2(1,2);

     int  Function  (int,int) fn3 = add2;
    var result = add2(4, 5);
    print("result = $result");


     Add fn4 = add2;
     fn4(5,6);
}