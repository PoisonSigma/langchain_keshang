官网地址:
https://smith.langchain.com/
pip install -U langchain langchain-openai
在解释器中安装 langchain 和 langchain-openai   和 langsmith 和 openai
![](/i/4d399ece-9c44-4771-acfb-424eab7dc8f6.jpg)
![](/i/5cae3a1d-9891-440b-9356-9a57ad9d409a.jpg)
复制这段内容:

#下面这个等于true就开始追踪
LANGSMITH_TRACING=true  
#下面的保持不变,用平台生成的
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
#下面是项目名,可以随便自己写,没有这个项目名,那么项目名就是default
LANGSMITH_PROJECT="写自己的"

![](/i/52c58f0d-1940-4e3f-b0d2-6c6d8367ee56.jpg)

![](/i/305df5cf-bc96-4d45-842d-2c17704cf13b.jpg)
