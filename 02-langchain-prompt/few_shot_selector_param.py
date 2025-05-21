from dotenv import load_dotenv
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings

load_dotenv()

examples = [
    {
        "question": "珠穆朗玛峰和富士山哪一座山的首次登顶时间更早？",
        "answer":
            """
            这里需要跟进问题吗：是的。
            跟进：珠穆朗玛峰的首次登顶时间是什么时候？
            中间答案：珠穆朗玛峰于1953年5月29日首次被登顶。
            跟进：富士山的首次登顶时间是什么时候？
            中间答案：富士山在公元663年已有朝圣者登顶记录。
            所以最终答案是：富士山
            """
    },
    {
        "question": "特斯拉和SpaceX的CEO是否曾就读于同一所大学？",
        "answer":
            """
            这里需要跟进问题吗：是的。
            跟进：特斯拉的CEO是谁？
            中间答案：特斯拉的CEO是Elon Musk。
            跟进：Elon Musk曾就读于哪所大学？
            中间答案：他曾在宾夕法尼亚大学学习。
            跟进：SpaceX的CEO是谁？
            中间答案：SpaceX的CEO也是Elon Musk。
            所以最终答案是：是
            """
    },
    {
        "question": "《哈利波特》系列和《魔戒》系列的作者是否都出生于英国？",
        "answer":
            """
            这里需要跟进问题吗：是的。
            跟进：《哈利波特》的作者是谁？
            中间答案：J.K. Rowling。
            跟进：J.K. Rowling的出生地是哪里？
            中间答案：她出生于英国格洛斯特郡。
            跟进：《魔戒》的作者是谁？
            中间答案：J.R.R. Tolkien。
            跟进：J.R.R. Tolkien的出生地是哪里？
            中间答案：他出生于南非奥兰治自由邦。
            所以最终答案是：不是
            """
    }
]

# 使用openai的embedding，也需要把openai的api-key加载到程序中
'''
example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 这是可供选择的示例列表。
    examples,
    # 这是用于生成嵌入的嵌入类，该嵌入用于衡量语义相似性。
    OpenAIEmbeddings(),
    # 这是用于存储嵌入和执行相似性搜索的VectorStore类。
    Chroma,
    # 这是要生成的示例数。
    k=1
)
'''

# 使用阿里embedding， 使用load_dotenv把.env中的api-key加载到程序中才可以访问
example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 这是可供选择的示例列表。
    examples,
    # 这是用于生成嵌入的嵌入类，该嵌入用于衡量语义相似性。
    DashScopeEmbeddings(
        model="text-embedding-v3",
        # other params...
    ),
    # 这是用于存储嵌入和执行相似性搜索的VectorStore类。
    Chroma,
    # 这是要生成的示例数。
    k=1
)

# 选择与输入最相似的示例。
question = "珠穆朗玛峰的首次登山时间？"
selected_examples = example_selector.select_examples({"question": question})
example_prompt = PromptTemplate(input_variables=["question", "answer"], template="问题：{question}\\n{answer}")

prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="问题：{input}",
    input_variables=["input"]
)

print(prompt.format(input="珠穆朗玛峰的首次登山时间？"))
