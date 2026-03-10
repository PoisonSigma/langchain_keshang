import '16类修饰符base.dart';

main(){
    var t1 = Test17();

    var w1 = Worker();
    // w1._name;
    w1.name2;


}
base class Worker extends Person17{
        // String _name  = "文件之外的名字";
}
/*
base class S17 implements Person17{//报错,文件之外,base 类不能被implements
//不能在文件之外使用implements 继承base的原因是:implements 会要求强制重写 所有属性和方法,那么私有属性也会被重写,在当前文件,就是父类之外的
//这个文件私有属性被重写之后,那么,这个文件,就可以访问父类的私有方法了,这样是不符合逻辑的.
}
 */