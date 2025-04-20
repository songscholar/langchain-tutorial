import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

llm = ChatOpenAI(
    model='deepseek-chat',
    max_tokens=1024,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

# 创建一个提示模板(prompt template)
# 这里以对话模型的消息格式为例子，不熟悉openai对话模型消息格式，建议先学习OpenAI的API教程
# 下面消息模板，定义两条消息，system消息告诉模型扮演什么角色，user消息代表用户输入的问题，这里用了一个占位符{input} 代表接受一个模版参数input。
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个著名的宋词研究学者"),
    ("user", "{input}")
])

# 基于LCEL 表达式构建LLM链，lcel语法类似linux的pipeline语法，从左到右按顺序执行
# 下面编排了一个简单的工作流，首先执行prompt完成提示词模板(prompt template)格式化处理， 然后将格式化后的prompt传递给llm模型执行，最终返回llm执行结果。
chain = prompt | llm

# 调用LLM链并设置模板参数input,  invoke会把调用参数传递给prompt提示模板，开始chain定义的步骤开始逐步执行。
result = chain.invoke({"input": "以怀才不遇，壮志难酬为主题写一首词牌名为”水调歌头“的词"})
print(result)
'''

'''
