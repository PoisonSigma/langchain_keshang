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

  loadData() {
    items = [
      ShoppingCartItem(text: "南岗大呲花", img:  "images/70kg.png", selected: false, count: 1),
      ShoppingCartItem(text: "道里小鞭儿", img:  "images/70kg2.png", selected: false,count: 2),
      ShoppingCartItem(text: "香坊二踢脚", img: "images/wyz.jpeg", selected: false,count: 3),
      ShoppingCartItem(text: "吴彦祖1", img: "images/2024.jpeg", selected: false,count: 4),
      ShoppingCartItem(text: "吴彦祖2", img: "images/wyz.jpeg", selected: false,count: 10),
      ShoppingCartItem(text: "吴彦祖3", img: "images/wyz.jpeg", selected: false,count:6)
    ];
  }

  List<Widget> makeActions() {
    var list = isEditting
        ? [
      IconButton(onPressed: () {}, icon: Icon(Icons.delete)),
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
          color: Colors.transparent,
          //透明颜色,为了给Container使用ColoredBox,可以扩大点击区域
          alignment: Alignment.centerRight,
          child: Text('删除选中'),
        ),
      )
    ]
        : [
      IconButton(onPressed: () {}, icon: Icon(Icons.search)),
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
          color: Colors.transparent,
          //透明颜色,为了给Container使用ColoredBox,可以扩大点击区域
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
            title: Text('购物车例子'), centerTitle: true, actions: makeActions()),
        body: HomePage(isEditting: isEditting, items: items),
      ),
    );
  }
}

class HomePage extends StatefulWidget {
  bool isEditting;
  List<ShoppingCartItem> items;

  HomePage({required this.isEditting, required this.items});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return ListView.separated(
        itemBuilder: (context, index) {
          return Row(
            children: [
              // Text(widget.items[index].text),
              widget.isEditting
                  ? Checkbox(
                  checkColor: Colors.red,
                  fillColor:
                  WidgetStateProperty.resolveWith(getColor), //填充颜色
                  value: widget.items[index].selected,
                  onChanged: (value) {
                    setState(() {
                      widget.items[index].selected =
                      !widget.items[index].selected;
                      print(widget.items[index].selected);
                    });
                  })
                  : Container(),
              GestureDetector(
                  onTap: () {
                    print("进入详情");
                  },
                  child: MidPage(widget.items[index])),
              Spacer(),
              widget.isEditting
                  ? IconButton(
                  onPressed: () {
                    print("删除");
                  },
                  icon: Icon(
                    Icons.remove_circle,
                    color: Colors.red,
                  ))
                  : Container(),
            ],
          );
        },
        separatorBuilder: (context, index) {
          return Divider();
        },
        itemCount: widget.items.length);
  }
}

class MidPage extends StatefulWidget {
  ShoppingCartItem item;

  MidPage(this.item);

  @override
  State<MidPage> createState() => _MidPageState();
}

class _MidPageState extends State<MidPage> {
  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Container(
          height: 100,
          width: 100,
          decoration: BoxDecoration(//这个是给container背景切圆角
              color: Colors.black12,
              borderRadius: BorderRadius.circular(10)),
          child: ClipRRect(//用于将其子控件剪裁为圆角
              borderRadius:BorderRadius.circular(10),
              child: Image.asset(widget.item.img)),
        ),
        Container(
          height: 100,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Expanded(
                  flex: 2,
                  child: Text(widget.item.text,style: TextStyle(fontSize: 20),)),
              Expanded(child: Row(
                children: [
                  Text("999999元",style: TextStyle(fontSize: 16,color: Colors.black54),),
                  Text(" x${widget.item.count}",style: TextStyle(fontSize: 14,color: Colors.red),),
                ],
              )),
            ],
          ),
        ),
      ],
    );
  }
}

//填充颜色
Color getColor(Set<WidgetState> states) {
  const Set<WidgetState> interactiveStates = <WidgetState>{
    WidgetState.pressed,
    WidgetState.hovered,
    WidgetState.focused,
  };
  if (states.any(interactiveStates.contains)) {
    return Colors.blue;
  }
  return Colors.black12; //修改填充颜色
}
