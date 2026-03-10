extension StringB on String{
  int parseInt() { //扩展方法
    try {
      return int.parse(this);
    }catch(e){
      print("发现异常e=$e");
      return -1;
    }
  }
}