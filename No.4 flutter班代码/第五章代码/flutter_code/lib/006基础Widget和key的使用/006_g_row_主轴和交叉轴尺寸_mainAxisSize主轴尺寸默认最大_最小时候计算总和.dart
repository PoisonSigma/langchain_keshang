
/*
mainAxisSize是主轴的尺寸
mainAxisSize:MainAxisSize.max,这个是默认值
mainAxisSize: MainAxisSize.min,//主轴最小值,如果父级限定了尺寸优先使用父级的尺寸,如果父级没有限定尺寸会取所有子控件尺寸总和
注意 crossAxisSize: ,交叉轴没有尺寸这个属性
因为交叉轴没有尺寸属性,所以永远取子控件中最大的值作为交叉轴的值
交叉轴拉伸,会改变子元素的尺寸到最大,直到撑满父级
如果子控件含有flex因子,例如Expanded控件,会消耗所有可用尺寸,扩展到父级的限定尺寸,这样MainAxisSize.min会失效
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
      // width: 400,
      // height: 300,
      color: Colors.green,
      child: Row(
        // mainAxisSize: MainAxisSize.max,//这个是默认值
        mainAxisSize:MainAxisSize.min,//主轴最小值,如果父级限定了尺寸优先使用父级的尺寸,如果父级没有限定尺寸会取所有子控件尺寸总和
        // crossAxisAlignment: CrossAxisAlignment.stretch,//交叉轴拉伸,会改变子元素的尺寸到最大,直到撑满父级
        //0元素会尺寸为最小
        children: <Widget>[
          Text("abc"),
          Container(
            color: Colors.yellow,
            width: 100,
            height: 100,
          ),
          Container(
            color: Colors.red,
            width: 150,
            height: 120,
          ),
          Expanded(
            flex: 1,
            child: Container(
              color: Colors.blue,
              width: 100,
              height: 100,
            ),
          ),
          Expanded(
            flex: 2,
            child: Container(
              color: Colors.pink,
              width: 100,
              height: 100,
            ),
          )
        ],
      ),
    );
  }
}