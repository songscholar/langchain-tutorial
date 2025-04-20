import os
from dotenv import load_dotenv
# 引入langchain聊天场景的提示词模版
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model='deepseek-chat',
    max_tokens=1024,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

# 根据message生成提示词模版
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个著名的宋词研究学者"),
    ("user", "{input}")
])
# 创建一个字符串输出解析器
output_parser = StrOutputParser()

# 通过langchain的链式调用，生成一个chain
chain = prompt | llm | output_parser

result = chain.invoke({"input": "以怀才不遇，壮志难酬为主题写一首词牌名为”水调歌头“的词"})
print(result)
'''
《水调歌头·书愤》
（依毛滂体）

长剑倚天啸，孤影对残灯。
十年磨就霜刃，无处试锋棱。
欲驾长鲸碧海，却困蓬蒿荻苇，
风雨暗相惊。
醉眼挑灯看，匣底作龙鸣。

射斗牛，光焰动，为谁明？
男儿意气，空负燕颔虎头形。
纵使封侯有骨，无奈时乖命蹇，
白发已丛生。
且尽杯中物，卧听晚潮声。

注：本词通过"长剑"、"霜刃"等意象，表现志士的英武气概；以"困蓬蒿"、"白发丛生"等语，道出英雄失路的悲愤。下阕连用"射斗牛"、"燕颔虎头"典故，强化怀才不遇主题。结句"卧听晚潮"以景结情，留下苍凉余韵。全词跌宕起伏，符合词牌声情特点。
'''
