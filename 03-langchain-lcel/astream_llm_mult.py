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


async def task1():
    chat_model = ChatOpenAI(
        model='deepseek-chat',
        max_tokens=1024,
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL")
    )
    # 第一个任务的逻辑代码
    chunks = []
    async for chunk in chat_model.astream("宋词的前身是什么？"):
        chunks.append(chunk)
        # 判断chunks长度为1的时候，打印chunks[0]
        if len(chunks) == 2:
            print(chunks[1])
        print(chunk.content, end="|", flush=True)


async def task2():
    reasoner_model = ChatOpenAI(
        model='deepseek-reasoner',
        max_tokens=1024,
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL")
    )
    # 第二个任务的逻辑代码
    chunks = []
    async for chunk in reasoner_model.astream("苏东坡是谁？"):
        chunks.append(chunk)
        # 判断chunks长度为1的时候，打印chunks[0]
        if len(chunks) == 2:
            print(chunks[1])
        print(chunk.content, end="|", flush=True)


async def main():
    #同步调用
    #await task1()
    #await task2()
    #异步调用：并发运行两个任务
    await asyncio.gather(task1(), task2())


# 运行主函数
asyncio.run(main())
