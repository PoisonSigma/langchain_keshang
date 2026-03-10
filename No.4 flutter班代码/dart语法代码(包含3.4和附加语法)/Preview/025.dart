main(){
//is运算符可以判断一个变量是否属于一个类型或者他的子类型 ,is!跟is完全相反,当 运算符is!左边的变量不属于右边的类型,或者不属于右边的子类型,才返回ture
var str = "123";
if(str is String){
print("是String类型");
} else if (str is int) {
print("是int类型");
}
if(str is! String){
print("is!判断 str不是String");
} else if (str is! int) {
print("is!判断  str不是int");
}


//is运算符,左边如果是右边的子类,也返回true ,这里没有其他语言基础的可以理解为,类也是一个类型,而继承父类,父类是他的爸爸,听不懂,到后面也会讲
//在这里引入类的概念,是为了让大家先知道is可以判断类
var p1 = Person();
if (p1 is Person){
print("p1是Person类型");
}
if(p1 is Animal){  //Animal是Person的父类,所以is也返回true
print("p1是Animal类型");
}
if(p1 is Object){    //Object是所有类的父类,所以is返回true
print("p1是Object类型");
}
if(Person is Animal){
print("is可以判断Person是Animal的子类");
}else{
print("is不能可以判断Person是Animal的子类");
}


}


//定义一个类Animal动物,
class Animal{
}
//Person类继承自Animal动物 ,那么 Animal是Person的父类
class Person extends Animal{

}