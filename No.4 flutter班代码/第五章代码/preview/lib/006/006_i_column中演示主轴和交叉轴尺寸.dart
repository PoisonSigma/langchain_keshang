/*
这个例子演示列column的主轴和交叉轴尺寸规则
 */
import 'package:flutter/material.dart';
main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text('标题栏'),
          ),
          body: const HomePage())));
}
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      // width: 300,
      height: 300,
      color: Colors.green,
      child: Column(
        mainAxisSize: MainAxisSize.min,//主轴最小值,如果父级限定了尺寸优先使用父级的尺寸,如果父级没有限定尺寸会取所有子控件尺寸总和
        // mainAxisSize: MainAxisSize.max,//默认值,取父级的最大值
        children: <Widget>[
            Text("abc"),
          Container(
            color: Colors.yellow,
            width: 100,
            child:Text("abc"),
          ),
          Container(
            color: Colors.red,
            width: 200,//列的交叉轴取了子控件中最大的尺寸200
            height: 50,
          ),
          //下面演示,如果子控件含有flex因子,例如Expanded控件,会消耗所有可用尺寸,扩展到父级的限定尺寸

          Expanded(
            flex: 1,
            child: Container(
              color: Colors.pink,
            width: 100,
            height: 100,
            ),
          ),
          Expanded(
            flex: 2,
            child: Container(
              color: Colors.blue,
              width: 150,
              height: 100,
            ),
          ),
        ],
      ),
    );
  }
}