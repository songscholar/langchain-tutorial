import os
from dotenv import load_dotenv
import asyncio
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

prompt = ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话")
model = ChatOpenAI(
    model='deepseek-chat',
    max_tokens=1024,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)
parser = StrOutputParser()
chain = prompt | model | parser


async def async_stream():
    async for chunk in chain.astream({"topic": "工作"}):
        print(chunk, end="|", flush=True)

# 运行异步流处理
asyncio.run(async_stream())
'''
|好的|！|这是一个|关于|工作的|经典|笑话|：

|---

|**|老板|**|：|我们|公司|崇尚|平等|，|在这里|没有|等级|观念|！|  
|**|新|员工|**|：|太好了|！|那|我可以|直接|叫|您|名字|吗|？|  
|**|老板|**|：|当然|可以|。|  
|**|新|员工|**|：|好的|，|老王|。|  
|**|老板|**|：|……|叫我|王|总|。|  

|（|冷笑|话|Bonus|：|平等|的前提|是|“|总|”|得|有人|加班|。）|  

|---|

|希望|让你|会|心|一笑|～| 😄||
'''