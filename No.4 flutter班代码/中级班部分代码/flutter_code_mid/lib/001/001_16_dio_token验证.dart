import 'package:dio/dio.dart';
import 'package:flutter_code_mid/001/common.dart';

main() async {

  //发送给服务器的请求headers是  :   dio.options.headers (先执行)
  //读取服务器过来的相应的headers:    res.headers (后接收)
  var dio = Dio();
  dio.options.baseUrl = baseUrl;
  dio.options.headers = {
    "authorization":"Bearer abc123"//注意这个格式key和value是不是强制的,但是按照规范,大家都这么起名字
  };//要发送给服务器之前设置的headers
   var res = await dio.get("faketoken");
  print("res = $res");
  // res = await dio.get("faketoken");
  // print("res = $res");

  //下面演示一个服务器发过来的headers
  // print("服务器发来的相应的headers:\n${res.headers}");
}