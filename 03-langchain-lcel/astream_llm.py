import os
from dotenv import load_dotenv
import asyncio

from langchain_openai import ChatOpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

model = ChatOpenAI(
    model='deepseek-chat',
    max_tokens=1024,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

# 异步流处理
async def async_stream():
    chunks = []
    async for chunk in model.astream("宋词的前身是什么？"):
        chunks.append(chunk)
        # 判断chunks长度为1的时候，打印chunks[0]
        if len(chunks) == 2:
            print(chunks[1])
        print(chunk.content, end="|", flush=True)
# 运行异步流处理
asyncio.run(async_stream())
