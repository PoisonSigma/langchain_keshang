from langchain_core.output_parsers import BaseOutputParser
import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

class PsParser(BaseOutputParser):
    # def parse(self, ai_msg):#这个是直接外面调用parse,需要自己获取content
    #     print("函数内部ai_msg=",ai_msg)
    #     print("函数内部 type(ai_msg)=", type(ai_msg))
    #     content = ai_msg.content
    #     print("content=", content)
    #     return content
    def parse(self, content):#这个是invoke调用的parse
        print("函数内部ai_msg=",ai_msg)
        print("函数内部 type(ai_msg)=", type(ai_msg))
        print("content=", content)
        return content
load_dotenv("../assets/openai.env")
llm = ChatDeepSeek(
    stop="好",
    model=os.getenv("MODEL_NAME"), temperature=0.8)
ai_msg = llm.invoke("你好")#invoke会把AiMessage里的content就是字符串,直接赋值给parse
#如果要是外面调用invoke,就不要把自定义的parse方法,在里面再取一次ai_msg.content了,
#因为传进来的ai_msg已经是invoke调用后再调用parse插入的字符串了

# text = PsParser().parse(ai_msg)#自定义的解析器,需要自己写parse
# text = PsParser().parse(ai_msg)

# text = StrOutputParser().invoke(ai_msg)#
text =  PsParser().invoke(ai_msg)
print("text=",text)