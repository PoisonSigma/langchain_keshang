import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

//这个例子演示主轴mainAsix 会取外面传进来的最大值,列取最大高,行取最大宽
//列取了外面传进来的最大高300
//行因为外面没有设置尺寸,所以取最大宽度,屏幕宽度
main() {
  runApp(MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: Text('列里面嵌套行  Colum+Row'),
          ),
          body: Body())));
}

class Body extends StatelessWidget {
  const Body({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 300, //给一个固定高度,
      // width: double.maxFinite, //给最大宽度,如果给了尺寸,
      // 交叉轴居中的时候正好在屏幕宽度上居中,不给尺寸,整个Column都靠左侧,
      //按照里面元素的最大宽度设置宽度,所以看着,居中也是靠左
      color: Colors.green,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        //这个居中是默认值/// This is the default cross-axis alignment.
        // 拥有每个均匀间隔图像的行
        children: [
          Text("abc1234567890123",
              style: TextStyle(fontSize: 40, backgroundColor: Colors.yellow)),
          Text("abc1234567890",
              style: TextStyle(fontSize: 40, backgroundColor: Colors.yellow)),
          Text("abc1234567890",
              style: TextStyle(fontSize: 40, backgroundColor: Colors.yellow)),
        ],
      ),
    );
  }
}
