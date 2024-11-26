from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('OPENAI_API_KEY')


# Set the OPENAI_API_KEY environment variable
os.environ['OPENAI_API_KEY'] = key

client = OpenAI()


fine_tunning_file = client.files.create(
  file=open("./data/train.jsonl", "rb"),
  purpose="fine-tune"
)

print(f"The file {fine_tunning_file.id} was upload to fine tunning")

fine_tunning_job = client.fine_tuning.jobs.create(
  training_file=fine_tunning_file.id,
  model="gpt-4o-mini-2024-07-18"
)

print(f"The fine tunning job {fine_tunning_job.id} was created")
