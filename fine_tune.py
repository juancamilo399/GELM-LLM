from openai import OpenAI
from openai import types
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('OPENAI_API_KEY')


# Set the OPENAI_API_KEY environment variable
os.environ['OPENAI_API_KEY'] = key

client = OpenAI()


train_fine_tunning_file = client.files.create(
  file=open("./data/train_es.jsonl", "rb"),
  purpose="fine-tune"
)

validation_fine_tunning_file = client.files.create(
  file=open("./data/test_es.jsonl", "rb"),
  purpose="fine-tune"
)

print(f"The file {train_fine_tunning_file.id} was upload to train fine tunning")

print(f"The file {validation_fine_tunning_file.id} was upload to validate fine tunning")

fine_tunning_job = client.fine_tuning.jobs.create(
  training_file=train_fine_tunning_file.id,
  validation_file=validation_fine_tunning_file.id,
  model="gpt-4o-mini-2024-07-18"
)

print(f"The fine tunning job {fine_tunning_job.id} was created")
