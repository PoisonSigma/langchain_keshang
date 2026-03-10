/*
1.
 pubspec.yaml文件找找到 flutter: 和 assets: 默认他使用 # 注释上的,打开注释,注意tab缩进问题
 如果遇到缩进问题,删除再自己按tab键
 flutter:
  assets:
    - images/2024.jpg
    - images/2x/2024.jpg
    - images/3.5x/2024.jpg

    别忘了在 pubspec.yaml 点击 get

2.
自己创建文件夹
images文件夹和  2x 3.5x文件夹要自己建立,层级是项目目录下
设备像素比不是自己指定的
    在设备像素比为 4.0 的设备上，将使用 images/3.5x/cat.png 资源。
    在设备像素比为 1.0 的设备上，将使用 images/cat.png 资源。

    如果1.0的图片在磁盘中没有，那么在设备像素比为 1.0 的设备上，
    将使用 images/2x/cat.png 图像。


3. 调用的时候图片名要带着images文件夹名字
  Image.asset( "images/2024.jpg");






 */

/*
官方文档:
创建一个从资源包获取的 ImageStream 的小部件。图像的键由 name 参数给出。

当显示来自包的图像时，package 参数必须非空，否则为 null。有关详细信息，请参阅“包中的资源”部分。

如果省略或为 null，则将使用 DefaultAssetBundle。

默认情况下，将尝试像素密度感知的资源分辨率。此外：

如果提供了 scale 参数且不为 null，则将使用指定的确切资源。要显示具有特定密度的图像变体，必须提供确切的路径（例如，images/2x/cat.png）。
如果 excludeFromSemantics 为 true，则将忽略 semanticLabel。
如果提供了 cacheWidth 或 cacheHeight，则它们表示引擎必须在指定大小解码图像。无论这些参数如何，图像都将呈现到布局或宽度和高度的约束中。这些参数主要用于减少 ImageCache 的内存使用。

应该指定 width 和 height 参数，或者将小部件放置在设置了紧密布局约束的上下文中。否则，图像尺寸将随着图像加载而改变，这将导致丑陋的布局更改。

使用 filterQuality 来指定图像的渲染质量。
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
    //注意文件名的images不能省略,否则报错,
    String str1 = "images/2024.jpg";
    return  ListView(
      children: [
        Image.asset(str1,
          // width: 200,//可以指定大小
          // height: 200,
        )
      ]
    );
  }
}