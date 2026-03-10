//在模块文件中使用part of 加上库名,代表是属于某一个库
part of poisonLib;
class P1{
  show(){
    print("P1 show执行了");
  }
}
class P1b{
  show(){
    print("P1b show执行了");
  }
}
test(){
  print("P1 test()执行了");
}