import 'package:dio/dio.dart';

import 'common.dart';

main() async {
  /*
  final dio = Dio();
  var option = BaseOptions(baseUrl: baseUrl);
  dio.options = option;

   */
  /*
  var option = BaseOptions(baseUrl: baseUrl);
  final dio = Dio(option);

   */
  //BaseOptions设置基础选项,
  // baseUrl设置公共地址
  final dio = Dio(BaseOptions(baseUrl: baseUrl));
  var res = await dio.get("");
  //headers是服务器返回的header 请求头信息
  // print("headers = ${res.headers}");
  // print("res = $res");

  dio.put("put").then((res){
    print("res = $res");
  });
}
