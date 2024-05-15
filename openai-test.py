from dotenv import load_dotenv
from openai import OpenAI
import os

# 加载.env文件中的环境变量
load_dotenv()

# client = OpenAI()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# 或者：
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 发起请求
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)