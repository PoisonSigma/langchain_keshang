/*
Spacer(),//弹簧效果,沾满剩余空间
 */
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

main() {
  runApp(ShoppingCartApp());
}

class ShoppingCartApp extends StatefulWidget {
  const ShoppingCartApp({super.key});

  @override
  State<ShoppingCartApp> createState() => _ShoppingCartAppState();
}

class _ShoppingCartAppState extends State<ShoppingCartApp> {
  bool isEditting = false; //是否是编辑模式
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
            appBar: AppBar(
              centerTitle: true, //AppBar title标题居中
              title: const Text('标题栏'),
              actions: isEditting
                  ? [
                GestureDetector(
                  onTap: () {
                    setState(() {
                      print("点击了退出管理");
                      isEditting = !isEditting;
                    });
                  },
                  child: Container(
                      alignment: Alignment.centerRight,
                      height: 44,
                      width: 100,
                      // color: Colors.green,
                      child: Text("退出管理")),
                )
              ]
                  : [
                IconButton(
                    onPressed: () {
                      print("点击了搜索");
                    },
                    icon: Icon(Icons.search)),
                GestureDetector(
                  onTap: () {
                    setState(() {
                      print("点击了管理");
                      isEditting = !isEditting;
                    });
                  },
                  child: Container(
                      alignment: Alignment.centerRight,
                      height: 44,
                      width: 40,
                      // color: Colors.yellow,
                      child: Text("管理")),
                ),
              ],
            ),
            body: HomePage(isEditting: isEditting)));
  }
}

class HomePage extends StatefulWidget {
  HomePage({super.key, required this.isEditting});

  bool isEditting = false;

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var items = List.generate(4, (index) => false);
  String str1 = "images/pyy.jpeg";

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
        itemBuilder: (context, index) {
          return Row(
            children: <Widget>[
              widget.isEditting
                  ? Container(
                // color: Colors.green,
                child: Checkbox(
                    value: items[index],
                    onChanged: (value) {
                      setState(() {
                        // items[index] = value!;
                        items[index] = !items[index];
                      });
                    }),
              )
                  : Container(),


              GestureDetector(
                  onTap: (){
                    print("点击了$index 进入详情页面" );
                  },
                  child: MiddlePage(str1: str1,)),
              Spacer(),
              widget.isEditting ? IconButton(onPressed: () {
                setState(() {
                  items.removeAt(index);
                });

              },
                  icon: Icon(Icons.remove_circle, color: Colors.red,)): Container(
              ),
            ],
          );
        },
        separatorBuilder: (context, index) {
          return Divider();
        },
        itemCount: items.length);
  }
}
class MiddlePage extends StatefulWidget {
  MiddlePage({super.key,
    required this.str1
  });
  final String str1;
  @override
  State<MiddlePage> createState() => _MiddlePageState();
}

class _MiddlePageState extends State<MiddlePage> {
  @override
  Widget build(BuildContext context) {
    return Container(
      // color: Colors.yellow,
      child: Row(
        children: [
          Container(
            // height: 100,
            // width: 100,
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                color: Colors.black12),
            child: Image.asset(
              widget.str1,
              width: 100,
              height: 100,
              fit: BoxFit.contain,
            ),
          ),
          /*
          Placeholder(
            fallbackWidth: 50,
            fallbackHeight: 50,
          ),

           */
          Container(
            height: 200,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Expanded(
                  flex: 2,
                  child: Container(
                    // color: Colors.green,
                      height: 40,
                      child: Text("桥北吴彦祖",style: TextStyle(fontSize: 33,color: Colors.black87))),
                ),
                Expanded(
                  flex: 1,
                  child: Container(
                    height: 30,
                      // color: Colors.red,
                      child: Text("东北大呲花",style: TextStyle(fontSize: 14,color: Colors.black87))),
                ),
                Expanded(
                  flex: 1,
                  child: Container(
                      height: 30,
                      // color: Colors.blueGrey,
                      child: Row(
                      children: <Widget>[
                        Text("9999999元",style: TextStyle(fontSize: 18,color: Colors.black87)),
                        Text("x1",style: TextStyle(fontSize: 14,color: Colors.red)),

                      ]
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
