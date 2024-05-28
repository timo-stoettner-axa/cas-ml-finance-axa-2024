import os

from google.colab import userdata
from langchain_openai import OpenAI

os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')

gpt35 = OpenAI(model_name="gpt-3.5-turbo")
gpt4 = OpenAI(model_name="gpt-4o")
