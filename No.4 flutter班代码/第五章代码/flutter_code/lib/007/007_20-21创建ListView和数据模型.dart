import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_code/007/ShoppingCartItem.dart';

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
  List<ShoppingCartItem> items = [];
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    loadData();
  }
  loadData(){
    items = [
      ShoppingCartItem(text: "南岗大呲花", img:  "images/70kg.png", selected: false, count: 1),
      ShoppingCartItem(text: "道里小鞭儿", img:  "images/70kg2.png", selected: false,count: 2),
      ShoppingCartItem(text: "香坊二踢脚", img: "images/wyz.jpeg", selected: false,count: 3),
      ShoppingCartItem(text: "吴彦祖1", img: "images/2024.jpeg", selected: false,count: 4),
      ShoppingCartItem(text: "吴彦祖2", img: "images/wyz.jpeg", selected: false,count: 10),
      ShoppingCartItem(text: "吴彦祖3", img: "images/wyz.jpeg", selected: false,count:6)
    ];
  }
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
        body:HomePage(items) ,
      ),
    );
  }
}
class HomePage extends StatefulWidget {
  List<ShoppingCartItem> items;
  HomePage(this.items);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  @override
  Widget build(BuildContext context) {
    return ListView.separated(itemBuilder: (context,  index){
          return Row(
            children:[
              Text(widget.items[index].text),
            ],
          );

    }, separatorBuilder: (context,  index){
          return Divider();
    }, itemCount: widget.items.length);
  }
}
