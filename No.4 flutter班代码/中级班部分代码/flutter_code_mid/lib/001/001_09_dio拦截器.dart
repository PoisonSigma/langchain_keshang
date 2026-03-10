import 'package:dio/dio.dart';

import 'common.dart';


main() {
    var iw = InterceptorsWrapper(
      onRequest: (RequestOptions options, RequestInterceptorHandler handler) {
        //拦截请求,并且向下传递
        print("拦截到信息,同时给up发了10条软中华");
        return handler.next(options);//这个是向下流转
        /*
        return handler.resolve(  //做一个假数据,改变了请求结果
          Response(requestOptions: options, data: '这是一条假数据'),
        );
         */
      },
      onResponse: (Response response, ResponseInterceptorHandler handler) {
        print("拦截到信息 response = $response");
        // 如果你想终止请求并触发一个错误，你可以使用 `handler.reject(error)`。
        return handler.next(response);
      },
      onError: (DioException error, ErrorInterceptorHandler handler) {
        print("拦截到信息 error = $error");
        // 如果你想完成请求并返回一些自定义数据，你可以使用 `handler.resolve(response)`。
        // return handler.next(error);//注释以后不让他把请求向下传递
      },
    );

  try {
    final dio = Dio();
    var option = BaseOptions(baseUrl: baseUrl);
    dio.options = option;
    dio.interceptors.add(iw);
    // dio.interceptors.addAll([iw]);//要一组拦截器
    dio.interceptors.addAll([iw,
      // LogInterceptor(
      //   logPrint: (o) => print("日志拦截器:${o.toString()}"),
      // ),
    ]);//要一组拦截器

    dio.get("get").then((res) {
      print("res1=$res");
    });
    dio.put("put").then((res) {
      print("res2=$res");
    });
  } catch (e) {
    print("e = $e");
  }
}
