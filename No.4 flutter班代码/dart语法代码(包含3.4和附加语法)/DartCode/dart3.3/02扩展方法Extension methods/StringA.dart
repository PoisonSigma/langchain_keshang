extension StringA on String{
      int parseInt(){
        try {
          return int.parse(this);
        }catch(e){
          print("接收到异常 e = $e");
          return -1;
        }
      }
}
