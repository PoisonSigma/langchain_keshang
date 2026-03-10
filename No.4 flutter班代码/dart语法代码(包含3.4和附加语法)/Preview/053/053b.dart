class ListPoison<T>{
  var _l1 = [];//私有属性,让文件外的类外不能访问
  add(T value){
    _l1.add(value);
  }
  //重写getter方法,让=赋值符号可以获取值
  get values{
    return _l1;
  }

}