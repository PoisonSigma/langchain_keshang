```
[[package]]

name = "annotated-types"  //包的名字

version = "0.7.0"  //版本号

source = { registry = "https://pypi.tuna.tsinghua.edu.cn/simple" } //声明「包的归属仓库」registry：指定 uv 下载该包时优先访问的「根仓库」（这里是清华 PyPI 镜像）；

sdist = { url = "https://pypi.tuna.tsinghua.edu.cn/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }  //sdist 源码包

wheels = [

  { url = "https://pypi.tuna.tsinghua.edu.cn/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },

]//预编译包
```

**优先装 wheel**：uv 会优先下载 `wheels` 里的预编译包，只有当 wheel 不可用（比如包没有提供 wheel）时，才会下载 `sdist` 源码包并本地编译；

### `source` vs `sdist`/`wheels`：核心差异（用通俗例子理解）

| 字段     | 层级   | 作用                                   | 类比                                             |
| -------- | ------ | -------------------------------------- | ------------------------------------------------ |
| `source` | 仓库级 | 声明「该去哪个超市买东西」（清华镜像） | 超市的地址（比如「北京市海淀区清华超市」）       |
| `sdist`  | 文件级 | 声明「超市里具体的源码商品路径」       | 超市货架上「annotated-types 源码包」的具体位置   |
| `wheels` | 文件级 | 声明「超市里具体的预编译商品路径」     | 超市货架上「annotated-types 预编译包」的具体位置 |

例如这个例子annotated-types包里面 sdist 和 wheels 都能复制出来点击下载，他们开头都是https://pypi.tuna.tsinghua.edu.cn/ 的清华源的网址开头

```
[[package]]

name = "langchain"

version = "1.1.2"

source = { registry = "https://pypi.tuna.tsinghua.edu.cn/simple" }

dependencies = [

  { name = "langchain-core" },

  { name = "langgraph" },

  { name = "pydantic" },

]

sdist = { url = "https://pypi.tuna.tsinghua.edu.cn/packages/53/7c/127a4b15434bed166c1d81ff3ae7c86d19d41c27ca92b42fbbed0c9bb2a3/langchain-1.1.2.tar.gz", hash = "sha256:5d59557cf9939ff6db60c09bbfca80742865c511ddc33b24fc27920b2bb6157b", size = 530827, upload-time = "2025-12-04T17:59:46.419Z" }

wheels = [

  { url = "https://pypi.tuna.tsinghua.edu.cn/packages/b8/50/7413db85fab5f1b16523d3353ac45ecd83c439b4b7ffad7681d14f0eb55b/langchain-1.1.2-py3-none-any.whl", hash = "sha256:b8154e1ff090093ab5b3d6eee0e51ac91d83b5f42af0258700594a47a3a6b089", size = 102147, upload-time = "2025-12-04T17:59:45.466Z" },

]
```



dependencies 直接依赖包，这个例子langchain要运行必修直接依赖3个包langchain-core 和langgraph和 pydantic

