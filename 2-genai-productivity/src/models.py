import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

try:
    from google.colab import userdata
    os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')
except ImportError:
    # Not executed in Google Colab
    pass

gpt35 = ChatOpenAI(model_name="gpt-3.5-turbo")
gpt4 = ChatOpenAI(model_name="gpt-4o")
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
