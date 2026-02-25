![image-20251223123308792](/Users/poison/Library/Application Support/typora-user-images/image-20251223123308792.png)

External Libraries

外部库里面是项目真正使用的虚拟环境的包和对应版本，如果自己虚拟环境选择错了，可以点击这个来查看自己是否选错

而目录下面的.venv是默认uv读取的虚拟环境，但是在pycharm里面需要自己手动选择，有时候会选错，可以通过External Libraries去核实是否选择对了应对的版本

![image-20251223123937021](/Users/poison/Library/Application Support/typora-user-images/image-20251223123937021.png)

例如：External Libraries里的site-packages 的langgraph是1.0.2

上面的是真正的源代码文件，下面带版本号的是其他信息。

![image-20251223124129552](/Users/poison/Library/Application Support/typora-user-images/image-20251223124129552.png)

这里面.venv的langgraph是1.0.5是包含sqlite,1.0.2就不包含

![image-20251223124249417](/Users/poison/Library/Application Support/typora-user-images/image-20251223124249417.png)

![image-20251223124335053](/Users/poison/Library/Application Support/typora-user-images/image-20251223124335053.png)