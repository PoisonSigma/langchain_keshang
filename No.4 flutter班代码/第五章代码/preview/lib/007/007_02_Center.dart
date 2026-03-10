/*
我们自己的总结:
1.父控件有尺寸约束,优先用父控件的尺寸,Center会自动扩充到最大填充满父控件.
2.父控件没有尺寸约束,那么才看倍率因子,不能给负数 widthFactor 或 heightFactor
3.上下左右都居中,不能像Align那样可以随意改变对其方式
4.如果外层没有container这种尺寸的约束,而是直接放在body的子控件,那么直接把center最大化
 */
/*
官方解释:
1.Center 是一个用于将其子部件在其内部居中的部件（widget）。
2.如果 Center 的尺寸受到限制，且 widthFactor 和 heightFactor 为 null，那么它会尽可能大。
这种情况下，Center widget 的尺寸将由其外部约束决定，而不是由其子组件的尺寸决定。
这个属性可以用于创建具有特定宽度比例关系的布局
3.如果尺寸因子非 null，则此部件的相应维度将是其子部件的维度与尺寸因子的乘积
4.如果 Center  的某个维度（宽度或高度）没有受到外部约束，
且对应的 widthFactor 或 heightFactor为 null，
那么 Center widget 在那个维度上的尺寸会与其子组件的对应
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
    // 1.Center 是一个用于将其子部件在其内部居中的部件（widget）。
    // 2.如果 Center 的尺寸受到限制，且 widthFactor 和 heightFactor 为 null，那么它会尽可能大。
    // 这种情况下，Center widget 的尺寸将由其外部约束决定，而不是由其子组件的尺寸决定。
    // 这个属性可以用于创建具有特定宽度比例关系的布局
    return Container( //外面这个container限制了center,并且没有倍率因子
      // width: 300,
      // height: 300,
      color: Colors.green,
      child: Center(


        widthFactor: 2,  //    3.外部有尺寸限制,内部的倍率因子就失效了,,外面尺寸限制有限极大
        heightFactor: 2,
        child: Container(
          width: 100,
          height: 100,
          color: Colors.yellow,
        ),

      ),
    );
  }
}