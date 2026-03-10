extension StringC on String{
     static String name = "字符串";
     static show(){
       print("show()");
     }

    int get length2 =>length;
    set name2(String str){
      print("调用setter");
      name = str;
    }
}
main(){
  /*
  //静态属性和方法需要使用扩展名称调用 StringC.name  StringC.show()
    StringC.name = "abc";//setter
    print(StringC.name);//getter

   */

  String str = "abcd";
    // print(str.length2);
  str.name2 = "777";
  print(StringC.name);
  "12345".name2 = "123456";//不同变量的setter写入相同的static 属性,static属性是属于整个扩展的,不是属于某一个变量的
  print(StringC.name);




}