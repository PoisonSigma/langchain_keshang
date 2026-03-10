import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  runApp(ShopCartApp());
}

class ShopCartApp extends StatefulWidget {
  const ShopCartApp({super.key});

  @override
  State<ShopCartApp> createState() => _ShopCartAppState();
}

class _ShopCartAppState extends State<ShopCartApp> {
  bool isEditting = false;

  //创建右上角的action
  List<Widget> makeActions() {
    List<Widget> list =
    isEditting ?
    [
      IconButton(
          onPressed: () {
            print("删除选中");
          },
          icon: Icon(Icons.delete)),
      GestureDetector(
        onTap: () {
          setState(() {
            isEditting = !isEditting;
            print("编辑模式 $isEditting");
          });
        },
        child: Container(
            alignment: Alignment.centerRight,
            color: Colors.green,
            width: 100,
            height: 44,
            child: Text('退出管理')),
      )
    ]:[
      IconButton(
          onPressed: () {
            print("搜索");
          },
          icon: Icon(Icons.search)),
      GestureDetector(
        onTap: () {
          setState(() {
            isEditting = !isEditting;
            print("编辑模式 $isEditting");
          });
        },
        child: Container(
            alignment: Alignment.centerRight,
            color: Colors.green,
            width: 100,
            height: 44,
            child: Text('管理')),
      )
    ]
    ;
    return list;
  }



  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(

          actions: makeActions()
        ),
      ),
    );
  }
}
