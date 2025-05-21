import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import JsonOutputParser

# 加载 .env 文件中的环境变量
load_dotenv()

model = ChatOpenAI(
    model='deepseek-chat',
    max_tokens=1024,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)
chain = (
        model | JsonOutputParser()
    # 由于Langchain旧版本中的一个错误，JsonOutputParser未能从某些模型中流式传输结果
)

async def async_stream():
    async for text in chain.astream(
            "以JSON 格式输出中国、美国和印度的国家及其人口列表。"
            '使用一个带有“countries”外部键的字典，其中包含国家列表。'
            "每个国家都应该有键`name`和`population`"
    ):
        print(text, flush=True)

# 运行异步流处理
asyncio.run(async_stream())

# 输出
'''
{}
{'countries': []}
{'countries': [{}]}
{'countries': [{'name': ''}]}
{'countries': [{'name': '中国'}]}
{'countries': [{'name': '中国', 'population': 141}]}
{'countries': [{'name': '中国', 'population': 141175}]}
{'countries': [{'name': '中国', 'population': 141175000}]}
{'countries': [{'name': '中国', 'population': 1411750000}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': ''}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国'}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}, {}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}, {'name': ''}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}, {'name': '印度'}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}, {'name': '印度', 'population': 138}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}, {'name': '印度', 'population': 138000}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}, {'name': '印度', 'population': 138000000}]}
{'countries': [{'name': '中国', 'population': 1411750000}, {'name': '美国', 'population': 331000000}, {'name': '印度', 'population': 1380000000}]}
'''