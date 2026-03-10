import 'dart:io';




main(){
  print("1111111");
  getData();

  print("2222222");
}

getData() {
  Future(() {
    print("start");
    sleep(Duration(seconds: 2));
    print("end");
  });
}
