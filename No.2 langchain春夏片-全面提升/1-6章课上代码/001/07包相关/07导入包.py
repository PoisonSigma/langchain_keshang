# from 关键字
# from 关键字通常和 import 搭配使用，它允许你从一个模块中导入特定的对象，而不是将整个模块导入。
# 使用 from ... import ... 语法导入对象后，在代码中可以直接使用这些对象，无需再加上模块名前缀。
# from langchain.chat_models import ChatOpenAI

#python中 from包名langchain是顶级包，后面的点.分割子包（子文件夹），python2里面要从
#_init__.py 文件（Python 3.3 之后该文件不是必需的）的目录，而模块通常是一个 .py 文件
import os

#注释用3个单引号 或者 双引号
"""
from dotenv import load_jdotenv
load_dotenv(dotenv_path="assets/openai.env")
"""



import dotenv
# from ps_chain.chat_models import add #从包和子包中 导入add方法
from ps_chain.chat_models import * # import* 会把 __all__中的全部导入
from ps_chain.chat_models import sub # 这个导入sub，是明确导入这个方法，所以不会报错
dotenv.load_dotenv("assets/openai.env")
print(os.getenv("NAME"))
print(add(1,2))
print(sub(100,50))




