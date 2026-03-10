import 'dart:convert';
//json在线解析网址:https://www.json.cn/#
import 'package:flutter_code/007/UserItemA1.dart';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main(){
runApp(MaterialApp(home: Scaffold(
  appBar: AppBar(title: Text("标题栏"),),
  body: HomePage(),
)));
}
class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}
class _HomePageState extends State<HomePage> {
  late UserItemA1 item;
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    readData();

  }
  @override
  Widget build(BuildContext context) {
    print("img = ${item.img}");
    return Container(
      child: Image.network(item.img),
    );

  }

  readData(){
    // var a1 = UserItemA1(img: "abc", userName: "zhang3", isSelected: true);
    // print(a1);
    String jsonstr = '''
  {
  "info": {
    "userName": "zhang3",
    "isSelected": false
  },
  "msg": 0
}
  ''';
    var map = jsonDecode(jsonstr);//json字符串,转map
    print(map.runtimeType);
    print(map["msg"]);
    print(map["info"]);
    // String img = map["info"]["img"];
    // print(img);
    // var item = UserItemA1(img: img, userName: map["info"]["userName"], isSelected: map["info"]["isSelected"]);
    // print(item);
    item =  UserItemA1.fromMap(map["info"]);
  }
}

