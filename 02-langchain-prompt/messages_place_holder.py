from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是宋书生的人工智能助手"),
    #可以传入一组消息
    MessagesPlaceholder("msgs")
])
result = prompt_template.invoke({"msgs": [HumanMessage(content="你好!"),HumanMessage(content="你好，我是宋书生!")]})
print(result)

