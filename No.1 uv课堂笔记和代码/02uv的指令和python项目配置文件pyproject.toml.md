

#直接在一个python项目目录下直接在终端执行：

# uv add 加上包名，会自动下载相关包所以来的包：

例如安装langchain,会自动安装虚拟环境，并且在里面安装包，但是有的时候会下载失败

```
uv add langchain
```





打开虚拟环境下的文件pyvenv.cfg文件如下：

```
home = /Library/Frameworks/Python.framework/Versions/3.13/bin
#原始 Python 解释器所在目录

implementation = CPython
	#虚拟环境使用的 Python 解释器实现类型是CPython
uv = 0.9.16
#uv版本号

version_info = 3.13.7
#虚拟环境python版本

include-system-site-packages = false
#false是不使用系统的python包，意思是，当前虚拟环境是否包含系统的包，=false是不包含，当前虚拟环境只使用自己安装的包

prompt = 02uv
#拟环境激活后，终端前缀显示的「环境名称」
```





# pyproject.toml 项目文件

`pyproject.toml` 是 Python 生态的**通用配置标准**，除了`uv、pip`、poetry 外，**几乎所有现代 Python 工具都原生支持**它

当我们执行了uv add langchain，以后，这个文件里面的依赖dependencies只有一个langchain，比传统venv里的pip freeze > requirements.txt导出的包少很多，而且不用某一个包，例如langchain以后，传统的venv，删除了langchain,其他20多个包，不会跟着删除，需要手动删除其他。但是dependencies这里面只需要删除uv add自己添加的langchain包，其他的依赖的包不需要自己添加和删除

```
name = "02uv"

version = "0.1.0"

description = "Add your description here"

readme = "README.md"

requires-python = ">=3.13"

dependencies = [

  "langchain>=1.1.2",

]
```





# uv sync 同步

把pyproject.toml，放到某一个文件夹下，进入命令行以后执行 uv sync会自动创建虚拟环境，并且安装pyproject.toml，里面dependencies的包和它的依赖包

```
uv sync
```





在项目目录下没激活虚拟环境但是可以使用uv pip list指令查看安装了什么包

```
uv pip list
```

Package    Version
---------- -------
pip        25.3
setuptools 80.9.0



# uv init 创建项目

```
uv init
```

如果遇到文件夹是中文的无法使用uv init进行创建项目，可以指定项目名如下：uv init 项目名

```
uv init 项目名
```

uv init -p python版本号

```
uv init -p 3.14
```

这个3.14版本目前没有，目前最高3.13 故意写高版本，目的演示可以修改

此时文件夹下生成3个文件

main.py

pyproject.toml

README.md

项目配置文件pyproject.toml文件如下：

```
[project]
name = "demo1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.14"
dependencies = []
```

当执行

uv add langchain

的时候会报错。

此时手动修改pyproject.toml文件中的requires-python = ">=3.14" 为3.13

再执行

```
uv add langchain
```

可以正常安装



# 使用sync降低版本

如果已经安装了项目，想要降低版本，可以手动修改项目配置文件版本号，然后选择同步





```
uv remove 包名，删除一个包
```

```
uv remove langchain
```

也可以通过手动删除pyproject.toml文件中的dependies里面的langchain，再执行uv sync进行删除,相当于flutter里面的pub get读取配置文件，然后安装或者删除包

# uv tree 列出树形结构的依赖关系

```
uv tree
```

```
demo1 % uv tree
Resolved 33 packages in 10ms
demo1 v0.1.0
└── langchain v1.1.3
    ├── langchain-core v1.1.2
    │   ├── jsonpatch v1.33
    │   │   └── jsonpointer v3.0.0
    │   ├── langsmith v0.4.56
    │   │   ├── httpx v0.28.1
    │   │   │   ├── anyio v4.12.0
    │   │   │   │   └── idna v3.11
    │   │   │   ├── certifi v2025.11.12
    │   │   │   ├── httpcore v1.0.9
    │   │   │   │   ├── certifi v2025.11.12
    │   │   │   │   └── h11 v0.16.0
    │   │   │   └── idna v3.11
    │   │   ├── orjson v3.11.5
    │   │   ├── packaging v25.0
    │   │   ├── pydantic v2.12.5
    │   │   │   ├── annotated-types v0.7.0
    │   │   │   ├── pydantic-core v2.41.5
    │   │   │   │   └── typing-extensions v4.15.0
    │   │   │   ├── typing-extensions v4.15.0
    │   │   │   └── typing-inspection v0.4.2
    │   │   │       └── typing-extensions v4.15.0
    │   │   ├── requests v2.32.5
    │   │   │   ├── certifi v2025.11.12
    │   │   │   ├── charset-normalizer v3.4.4
    │   │   │   ├── idna v3.11
    │   │   │   └── urllib3 v2.6.1
    │   │   ├── requests-toolbelt v1.0.0
    │   │   │   └── requests v2.32.5 (*)
    │   │   ├── uuid-utils v0.12.0
    │   │   └── zstandard v0.25.0
    │   ├── packaging v25.0
    │   ├── pydantic v2.12.5 (*)
    │   ├── pyyaml v6.0.3
    │   ├── tenacity v9.1.2
    │   ├── typing-extensions v4.15.0
    │   └── uuid-utils v0.12.0
    ├── langgraph v1.0.4
    │   ├── langchain-core v1.1.2 (*)
    │   ├── langgraph-checkpoint v3.0.1
    │   │   ├── langchain-core v1.1.2 (*)
    │   │   └── ormsgpack v1.12.0
    │   ├── langgraph-prebuilt v1.0.5
    │   │   ├── langchain-core v1.1.2 (*)
    │   │   └── langgraph-checkpoint v3.0.1 (*)
    │   ├── langgraph-sdk v0.2.14
    │   │   ├── httpx v0.28.1 (*)
    │   │   └── orjson v3.11.5
    │   ├── pydantic v2.12.5 (*)
    │   └── xxhash v3.6.0
    └── pydantic v2.12.5 (*)
```









# uv build打包

```
uv build
```

![image-20251209124832812](./i/image-20251209124832812.png)

# uv pip install安装包

安装完以后会在当前虚拟环境.venv文件夹下的site-packages下多出一个文件夹demo1-0.1.0.dist-info ，就是刚才打的包





# uv pip list列出安装的包

```
uv pip list
```



uv.lock + pyproject.toml文件 加uv sync 进行精确版本控制，虚拟环境从一个机器转移到另外一台机器

# uv venv创建虚拟环境
