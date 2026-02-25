
用Google Chrome浏览器打开要获取网页
# 这篇文章先显示源代码,cmd+f搜索"本文结合反汇编pc版植物大战僵尸",注意不要有逗号, 因为逗号变成了:&#xff0c,&#xff0c;对应的是 UTF - 8 编码下逗号的十六进制表示形式（0xFF0C）
1.使用账号密码登录。
2. 按F12 ,打开浏览器开发者模式
或者鼠标右键 点击 检查
![](/i/ac50e2a8-ebfc-4b8b-a817-b196c33d8827.jpg)
![](/i/41357fd4-cac1-4968-91ec-b342dad58776.jpg)






点击 “Application” 选项卡，打开 “Storage” 目录，再点击左侧的 “Cookies” 子目录。
在 Cookies 子目录中，找到 “https://www.bilibili.com” 这个域名下的 Cookie 信息。
查找并复制 sessdata、bili_jct 和 buvid3 这几个 Cookie 参数的值

![](/i/b6e205b3-a1ef-4f0b-8225-fa77560476ab.jpg)

复制这3个value 如下图,选择value 后双击一下,就全选了,然后复制
![](/i/e76f017a-1ef5-4279-88c9-fb149cec2339.jpg)
SESSDATA
2f729d39%2C1760267094%2C864de%2A41CjAG8RnGmsb4qKsb8lVsEskVlBpB2WEutNfv6RMZETCRyFANcbPMEvAsEwg_NHuIr-MSVnd1WHFSbEtybDM4Uzg0OHZyRTlxcWJjZlFTMzg2V2pCalctUE5Yd2ZkcGJQd0FxU3ZtdVBUQkV5Wm5jYTY3WFZxRlIyU2wwTGwtaWJDSXFmZkt3U2R3IIEC
buvid3
F9CDE392-32DF-7ADE-20A3-F3930F5136B639898infoc

bili_jct
4848c15a6bb3f35aee77521258045a60




B站up主如何手动给不能自动ai生成字幕的视频上传字幕?例如纯音乐,没有语言对白的视频?
1.创作者中心,内容管理,编辑
![](/i/c847b410-d7b5-4d68-85a1-e411241e5e86.jpg)
2.更多设置->上传字幕

SRT 字幕文件是一种纯文本格式的字幕文件，每行内容包含字幕序号、时间码和字幕文本，以空行分隔不同的字幕段落。以下是按照你的要求编写的 SRT 字幕文件内容：
1
00:00:00,000 --> 00:00:01,000
ai班测试字幕1：心中无女人

2
00:00:05,000 --> 00:00:06,000
ai班测试字幕2：拔刀自然神
![](/i/ec8bfa7e-f480-4b65-a868-1ad015a420da.jpg)


点击上传字幕,把 自己制作的srt文件选择进去,然后点击立即投稿