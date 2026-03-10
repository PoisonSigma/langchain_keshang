import 'package:dio/dio.dart';

import 'common.dart';

main(){
    var dio = Dio(BaseOptions(baseUrl: baseUrl));
    //请求类型设置成ResponseType.stream
    dio.get("/stream",options: Options(responseType: ResponseType.stream)).then((res){
      print("res.data.stream ${res.data.stream}");
      //读取流用 res.data.stream
      var s1 =   res.data.stream;
      /*
      if(s1 is Stream){
        //服务端发送的123abc的流,把每个字符按照ascii码表转换成数字发送过来item=[49, 50, 51, 97, 98, 99]

      }
       */
      s1.listen((v){
        print("v = $v");
      });
    });



}