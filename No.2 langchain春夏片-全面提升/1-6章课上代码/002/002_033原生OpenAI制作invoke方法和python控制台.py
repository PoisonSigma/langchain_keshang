import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../assets/openai.env")
# OPENAI_API_KEY=sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO
# OPENAI_API_BASE=https://api.hunyuan.cloud.tencent.com/v1
# MODEL_NAME=hunyuan-turbo
print(os.getenv("MODEL_NAME"))
model_name = os.getenv("MODEL_NAME")
base_url = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("OPENAI_API_KEY")
print(model_name)
print(base_url)
print("当前目录:", os.getcwd())  # 打印当前目录,


# 使用 option+shift+e运行局部代码块的时候, python console的目录是根目录,不是当前文件所在目录
# 如果更改python console的当前目录使用命令os.chdir("完整路径") ,python console可以执行普通的python 代码,例如打等
# 构造 client
# client = OpenAI(
#     # api_key=os.environ.get("HUNYUAN_API_KEY"), # 混元 APIKey
#     api_key="sk-ISnpn1p7Q8RkOf1pHWKZb8Z6jjMZ0yXTwnsnIONRUOFrPhxO",
#
#     base_url="https://api.hunyuan.cloud.tencent.com/v1", # 混元 endpoint
# )
class PsLian(OpenAI):
    def __init__(self):
        # self.llm 在init方法里面self.变量名是
        # 使用 self.变量名 赋值时，就会在实例对象上创建一个新的属性，也就是成员变量。
        self.llm = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def invoke(self,msg)->str:
        response = self.llm.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": msg,
                },
            ],
        )
        print("铭刻:义父追魂戟,把离手越进义父离你越远>---红字增幅+26----------)三(--> ")
        return response.choices[0].message.content

llm = PsLian()
print("abc")
res = llm.invoke("你好,我们中国人民很行")
print(res)

