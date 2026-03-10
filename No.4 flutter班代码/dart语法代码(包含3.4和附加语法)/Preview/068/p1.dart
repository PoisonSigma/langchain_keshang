//在模块文件中使用part of 加上库名,代表是属于某一个库
part of poisonLib; //当前模块属于poisonLib 库
class P1{
  show(){
    print("P1 show()");
  }
}
class P1b{
  show(){
    print("P1b show()");
  }
}
//一个模块下可以有多个类和方法
test(){
  print("p1 test()执行");
}