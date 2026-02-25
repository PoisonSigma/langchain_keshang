中文路径下，无法直接通过uv init创建项目，因为中文无法创建项目名，规则是 英文字母数字-_.   减号，下划线，点才能当做项目名

uv init 项目名

```
uv init demo1
```

生成的pyproject.toml文件，手动进去修改项目名，然后再同步

```
[project]
name = "5demo-_-.55"  #这里自己修改名字
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.14"
dependencies = []
```

然后复制这个项目配置文件到新的目录，再同步，生成虚拟环境

生成虚拟环境之后使用pycharm 选择已经存在的虚拟环境，注意，类型选择uv,然后执行

```
uv pip install pip setuptools wheel
```





```
name = "demo5-_.5" #注意尽量不要起名带符号,因为虚拟环境不带
```



虚拟环境创建后pyvenv.cfg 文件里面虚拟环境的显示名如下：去掉了符号，只留下了字母数字

```
prompt = demo5-5
```

有时候pcharm选择错误虚拟环境会提示。有时候选择完虚拟环境，要等一会，或者重启以后才能找到，pycharm选择虚拟环境时，尽量不要用字母数字之外的符号当做项目名
