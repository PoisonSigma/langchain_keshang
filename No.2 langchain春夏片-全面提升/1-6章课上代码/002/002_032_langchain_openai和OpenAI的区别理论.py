# OpenAI：主要用于传统的文本生成任务，例如撰写文章、生成故事、描述场景等，适用于只需单向文本生成的简单场景。
# ChatOpenAI：专门为对话式交互设计，适合构建聊天机器人、问答系统等需要多轮对话的场景，能更好地处理上下文信息。
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
#在 langchain 库中，OpenAI 和 ChatOpenAI 都是用于与 OpenAI 模型进行交互的类，但它们在使用场景、输入输出格式、适用模型等方面存在明显区别，以下是详细介绍：
#langchain的 OpenAI输入字符串,返回字符串,但是ChatOpenAI,是可以对话形式,输出一堆臭氧层子,返回一堆臭氧层子,建议使用


# LangChain 并非完全基于 OpenAI 的 API 开发，而是一个独立的人工智能应用开发框架。
# 它通过封装和集成多种大语言模型（LLM）的 API（包括 OpenAI、Anthropic、Cohere 等），
# 为开发者提供统一的接口来构建复杂的 AI 应用。

# langchain的方法支持大模型的网址:
# https://python.langchain.com/v0.1/docs/integrations/llms/