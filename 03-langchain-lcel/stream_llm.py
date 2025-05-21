import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

model = ChatOpenAI(
    model='deepseek-chat',
    max_tokens=1024,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

chunks = []
for chunk in model.stream("宋词的前身是什么？"):
    chunks.append(chunk)
    print(chunk.content, end="|", flush=True)
