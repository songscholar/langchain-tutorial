from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# 使用langchain定义的SystemMessage、HumanMessagePromptTemplate等工具类定义消息，跟前面的例子类似，下面定义了两条消息
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "你是一个乐于助人的助手"
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

# 使用模板参数格式化模板
messages = chat_template.format_messages(text="书生喜欢古诗词")
print(messages)