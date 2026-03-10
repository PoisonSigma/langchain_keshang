

/*
extension ListB on List{

  int get length2 => length +1;

  add2( value){
    this.add(value);
  }
}

 */
//如果想要加上泛型,格式如下:
/*
extension 扩展名<类型> on List<类型>

 */
extension ListA<T> on List<T>{
  int get length2 => length +1;
  init(T list){
    this = list;
  }
  add2(T value){ //通过参数类型进行绑定, T 变成传入的静态类型
    this.add(value);
  }
}

main(){
  List l1 = [];//当编译器无法推断出List的类型的时候,把List设置成dynamic
  var l2 = [1,2,3];//有明确类型注释,推断出是int


    // var l1 = [1,2,3,4];
    var  l3 = [1,2,3,4]; //直接给泛型设定为<Object> 可以解决类型不匹配问题
    print(l3.length2);



    l3.add2(3);//执行完这行以后,编译器知道泛型的类型T是int,后续再赋值的时候不会改变类型
    l3.add2("abc");//因为类型被add2第一次调用绑定了类型int,所以这里报错
  print(l3);
}