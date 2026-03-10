/*
Image(image: NetworkImage("网址")
Image.network(网址)
  cacheWidth cacheHeight:  可以设置解码尺寸,如果不设置按照原始分辨率进行解码,图片分辨率太大的话耗费内存也大

 */

/*
官网文档
提供了几种构造函数，用于指定图像的不同方式：

Image.new，用于从 ImageProvider 获取图像。
Image.asset，使用键从 AssetBundle 获取图像。//本地图片,这节课不讲
Image.network，从 URL 获取图像。
Image.file，从文件获取图 像。
Image.memory，从 Uint8List 获取图像。
支持以下图像格式：JPEG、PNG、GIF、动画 GIF、WebP、动画 WebP、BMP 和 WBMP。底层平台可能支持其他格式。Flutter 将尝试调用平台 API 来解码未识别的格式，如果平台 API 支持解码图像，则 Flutter 将能够呈现它。

要自动执行像素密度感知的资源分辨率，请使用 AssetImage 指定图像，并确保 MaterialApp、WidgetsApp 或 MediaQuery widget 在 Image widget 上方存在于 widget 树中。

图像是使用 paintImage 进行绘制的，该类中的各个字段的含义在 paintImage 中有更详细的描述。
内存使用

图像以未压缩形式存储在内存中（以便渲染）。大型图像将使用大量内存：一个 4K 图像（3840×2160）将使用超过30MB的RAM（假设每像素32位）。

这个问题被图像在 ImageCache 中被缓存加剧了，所以大型图像可能会使用内存的时间比它们被显示的时间更长。

Image.asset、Image.network、Image.file 和 Image.memory 构造函数允许通过 cacheWidth 和 cacheHeight 参数指定自定义解码大小。然后引擎将以指定的大小解码和存储图像，而不是图像的自然大小。

这可以显著减少内存使用。例如，一个将以384×216像素（水平和垂直维度的十分之一）渲染的4K图像，如果使用 cacheWidth 和 cacheHeight 参数指定这些尺寸，只会使用330KB的内存，内存使用量减少了100倍。

Web平台考虑

在使用网络图像的Web平台上，仅当应用程序使用CanvasKit渲染器运行时，才支持 cacheWidth 和 cacheHeight 参数。当应用程序使用HTML渲染器时，Web引擎将网络图像的图像解码委托给Web，Web不支持自定义解码尺寸。

自定义图像提供者

在这个示例中，创建了 NetworkImage 的变体，它使用图像URL中的查询参数将所有 ImageConfiguration 信息（语言环境、平台、大小等）传递给服务器。
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
    String str1 =
        'https://flutter.github.io/assets-for-api-docs/assets/widgets/owl-2.jpg';
    String str2 =
        'https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg';
    return ListView(
      children: [
        //Image.network(网址)

        Image.network(
          str1,
          // cacheWidth: 100, //可以设置解码尺寸
          // cacheHeight: 100,
          width: 100,
          height: 100,
        ),

        // Image(image: NetworkImage("网址")
        Image(
          image: NetworkImage(str2),
        )
      ],
    );
    //
    // return  const
  }
}
