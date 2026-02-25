# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
client = OpenAI(api_key="这里同学填写自己的apikey",
                base_url="https://api.deepseek.com")

# client.chat：这是 OpenAI Python SDK 里的一个对象或方法，
# 借助它可以向聊天模型发送请求并接收响应。
# 它是开发者与聊天模型进行交互的编程接口，本身并非模型。
response = client.chat.completions.create(
    model="deepseek-chat",
    # model是大模型的类型
    # system"：用于设置对话的初始指令或背景信息，帮助模型了解对话的场景和任务。例如，你可以用 "system": "你是一个健身教练" 来为模型设定身份。
    # "user"：代表用户发送的消息，即用户向模型提出的问题或输入的内容。
    # "assistant"：表示模型生成的回复消息。在多轮对话中，你可以将之前模型的回复作为历史消息以 "assistant" 角色添加到 messages 列表中，帮助模型了解对话上下文。
    # "tool"：这个角色是在使用工具调用功能时使用，模型可以根据需求调用外部工具，并将工具调用的结果以 "tool" 角色的消息呈现。
    messages=[
        {"role": "system", "content": "你是一个健身教练"},  # role角色,系统角色,让大模型llm知道自己是一个什么背景身份
        {"role": "user", "content": "你好,你太大我不想练了"},
        {"role": "assistant", "content": "别急帅哥,办张卡,你马上就能变帅"},  # assistant或者ai,是让 大模型知道,以往的聊天历史,让他对回答进行参考
        {"role": "user", "content": "对不起,我没有钱,我的钱都买steam和epic游戏了"},
        {"role": "assistant", "content": "我给你买游戏,只要你买课"},
        {"role": "user", "content": "不行,我的钱,都让我老爸用了"},  # 要用用户的输入为结尾
    ],
    # 常见情况
    # 一般在与大语言模型交互时，最后一条消息的 role 为 "user"。
    # 这是因为交互流程往往是用户提出问题（"user" 角色消息），
    # 然后模型给出回复（"assistant" 角色消息）。所以为了让模型生成新的回复，
    # 最后一条消息需要是用户的新输入，即 "user" 角色.
    # 特殊情况
    # 有些场景下，最后一条消息的 role 可以不是 "user"。
    # 例如，你可能只是想查看历史对话记录，或者在调试代码、
    # 模拟特定对话流程时，最后一条消息可以是 "assistant" 或者其他有效的 role。
    # 但这种情况下，模型不会再生成新的回复，因为它没有接收到用户的新请求。
    # 总之，虽然常见做法是最后一条消息为 "user" 角色以触发模型生成新回复，
    # 但根据具体需求和场景，messages 列表最后一条消息的 role 可以灵活设置。
    stream=False
)

print(response.choices[0].message.content)
