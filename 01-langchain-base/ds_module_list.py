import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)
print(client.models.list())

'''
response:
SyncPage[Model](data=[Model(id='deepseek-chat', created=None, object='model', owned_by='deepseek'), 
Model(id='deepseek-reasoner', created=None, object='model', owned_by='deepseek')], object='list')
'''
