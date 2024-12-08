from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('OPENAI_API_KEY')


# Set the OPENAI_API_KEY environment variable
os.environ['OPENAI_API_KEY'] = key

client = OpenAI()


result = client.fine_tuning.jobs.retrieve("ftjob-wiVgjCq0TNQsN5uj1F5xAlnb")
content = client.files.content("file-KBpMockdayhm1ZRJZQ7mCo")
print(content)