/*
原生的 dart http请求  ,不讲了
官网的 http库,不讲了
dio 国人自己写的库,用的最多
pub.dev

pub.dev
pubspec.yaml文件复制  Installing 页面的安装内容:
dependencies:
dio: ^5.4.3+1
pubspec文件,添加,并且pub get
dio: ^5.4.3+1  这个 版本号要用官网最新版的
 */
import 'package:dio/dio.dart';
import 'package:flutter_code_mid/001/common.dart';
main() async {
  final dio = Dio();
   // dio.get("https://httpbin.org/get").then((value)=>print("value = $value"));
   var res = await dio.put(baseUrl);
   print("res = $res");
}