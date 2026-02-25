# from 关键字
# from 关键字通常和 import 搭配使用，它允许你从一个模块中导入特定的对象，而不是将整个模块导入。
# 使用 from ... import ... 语法导入对象后，在代码中可以直接使用这些对象，无需再加上模块名前缀。
from langchain.chat_models import ChatOpenAI

#python中 from包名langchain是顶级包，后面的点.分割子包（子文件夹），python2里面要从
#_init__.py 文件（Python 3.3 之后该文件不是必需的）的目录，而模块通常是一个 .py 文件
