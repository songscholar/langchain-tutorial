from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

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

example_prompt = PromptTemplate(input_variables=["question", "answer"], template="问题：{question}\\n{answer}")

# 提取examples示例集合的一个示例的内容，用于格式化模板内容
# examples[0] = {'name': '乔治·华盛顿的祖父母中的母亲是谁？', 'answer': 'Joseph Ball'}
# **examples[0] name='乔治·华盛顿的祖父母中的母亲是谁？', answer=Joseph Ball
#print(example_prompt.format(**examples[0]))


#接收examples示例数组参数，通过example_prompt提示词模板批量渲染示例内容
#suffix和input_variables参数用于在提示词模板最后追加内容， input_variables用于定义suffix中包含的模板参数
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="问题：{input}",
    input_variables=["input"]
)

print(prompt.format(input="《魔戒》的作者是谁？"))