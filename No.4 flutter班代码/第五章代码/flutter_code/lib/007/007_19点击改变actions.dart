import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

main() {
  runApp(ShoppingcartApp());
}

class ShoppingcartApp extends StatefulWidget {
  const ShoppingcartApp({super.key});

  @override
  State<ShoppingcartApp> createState() => _ShoppingcartAppState();
}

class _ShoppingcartAppState extends State<ShoppingcartApp> {
  bool isEditting = false;
   List<Widget> makeActions(){
   var list = isEditting ?  [
     IconButton(
         onPressed: () {
         },
         icon: Icon(Icons.delete)),
     GestureDetector(
       onTap: () {
         setState(() {
           isEditting = !isEditting;
           print(" $isEditting");
         });
       },
       child: Container(
         height: 44,
         width: 60,
         color: Colors.transparent,//透明颜色,为了给Container使用ColoredBox,可以扩大点击区域
         alignment: Alignment.centerRight,
         child: Text('删除选中'),
       ),
     )
   ] : [
     IconButton(
         onPressed: () {
         },
         icon: Icon(Icons.search)),
     GestureDetector(
       onTap: () {
         setState(() {
           isEditting = !isEditting;
           print(" $isEditting");
         });
       },
       child: Container(
         height: 44,
         width: 60,
         color: Colors.transparent,//透明颜色,为了给Container使用ColoredBox,可以扩大点击区域
         alignment: Alignment.centerRight,
         child: Text('退出管理'),
       ),
     )
   ];
   return list;
     // return [];
  }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('购物车例子'),
          centerTitle: true,
          actions: makeActions()
        ),
      ),
    );
  }
}
