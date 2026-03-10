// 连续2个点..是级联操作符,作用是把一个对象下面的方法或者成员连续使用出来.
// 级联操作返回的是对象
// 第一行的对象结尾不能加分号,最后一个成员或者方法结束再加分号,本质上是一行代码

class Person{
  String name = "张三";
  int age = 18;
  showInfo(){
    print("name = $name age = $age");
  }
  action(){
    print("action()执行 人类做了动作");
  }
}
main(){
  //级联操作符返回的是对象本身,返回..级联操作符左边的对象
  var p0 = Person();
  var result = p0..action();
  print("result = $result");
//用hashCode判断级联操作符返回的是否是左边的对象

  print("result = hashCode =  ${result.hashCode}");
  print("p0.hashCode = ${p0.hashCode}");
  //级联操作符右边的表达式不管是赋值还是方法,都返回左边的对象
  result = p0..age = 18;
  print("result = $result");

  //下面是不换行让大家看到级联操作的本质是一条语句,换行是为了看起来格式好看
  Person()..age=18..name="张三"..action()..showInfo();//

  //一般级联操作,都是换行使用,这样格式看起来清晰(推荐)
Person()
    ..name = "李四"
    ..age =30
    ..showInfo()
    ..action();



//可以连起来用,下面右边,因为用了级联,所以级联了3个操作,依然返回Person对象
var p2 = Person()
  ..name = "wang5"
  ..age = 30
  ..action();

//错误例子,中间有分号
var p3 = Person();
// ..name = "赵六";//错误上面有分号,已经不再是一条语句


}