main() {
  // bool类型可以赋值true真和false假
  bool r = true;//赋值真
  r = false;//赋值假

  //== 判断是否相等,如果相等返回ture
  r = (1 == 2);
  // print(r);

  r = (1 == 1);
  // print(r);

  // != 运算符,跟==相反,判断是否不相等
  r = (1!=1);
  print(r);

  //if判断,()表达式里面是ture,就执行第一个{}里面的内容,如果为false就执行else的内容
  if(true){
    print("真");
  }else{
    print("假");
  }
  if(1==1){
    print("真");
  }else{
    print("假");
  }

  //else if ,如果if()表达式判断为真,不会执行else if,如果if()判断为假,才会继续进行else if的判断.else if 可以连续多个
  if(1==1){
    print("1==1");
  }else if (2==2){

    print("2==2");
  }else if (3==3){
    print("3==3");
  }


}