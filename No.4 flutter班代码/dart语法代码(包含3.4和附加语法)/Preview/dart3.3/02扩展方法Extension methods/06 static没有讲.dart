  extension StringC on String{
    //静态属性和方法需要使用扩展名称调用 StringC.name  StringC.show()
      static String name = "字符串";
      static show(){
        print("show()");
      }
    get length2 => length;
    set name2 (String str){
      name = str;
      print("setter执行");
    }
    
}
main(){

    var str = "abc";
    print(str.length2);//getter
    str.name2 = "bcd";
    print(StringC.name);

    "xxx".name2 = "777";
    print(StringC.name);//不同变量的setter写入相同的static 属性,static属性是属于整个扩展的,不是属于某一个变量的
    StringC.name = "新的字符串";
    // String.show();//错误

    StringC.show();//正确
}