//构造函数中的[]和{} 跟普通函数一样,   [] 可选参数列表和 {} 命名参数列表,里面的参数都是 可选类型,或者是有默认值的非可选类型,
// {}大括号多了一个required 必填项
// 子类继承父类中的[]和{}的时候,也要加上括号

//{}大括号里面调用的时候要有 变量名:, {}里面定义的时候变量要有默认值,或者是必填项required,或者是可选类型的参数
class Person{
   String name;
   int age;
   double? height;//可选类型,可以接受null,因为{}里面需要接受null
   Person({required this.name, this.age = 18,this.height});
}
class Worker extends Person{
   int workId;
   //调用父类构造函数的简写也是外面加{}再用super
   Worker(this.workId,{required super.name,super.age,super.height});
}
//构造函数的[]可选参数列表,和普通函数可选参数列表一样,要求成员变量,要不是可选的参数,要不有默认值
class Person2{
   String? name;
   int age;//构造函数可选参数列表里面有默认值,所以可以不用可选类型?
   double? height;//可选类型,可以接受null,因为{}里面需要接受null
   Person2([this.name, this.age = 18,this.height]);
}
class Worker2 extends Person2{
   int workId;
   //调用父类构造函数的简写也是外面加{}再用super
   Worker2(this.workId,[ super.name,super.age,super.height]);
}

main(){
var p1 = Person(name: '张三',age: 30,height: 180.5);
Worker(10000,name: "李四",age: 31,height: 185.5);

}