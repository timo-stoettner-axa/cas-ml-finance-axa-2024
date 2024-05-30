from langchain_openai import ChatOpenAI, OpenAIEmbeddings

gpt35 = ChatOpenAI(model_name="gpt-3.5-turbo")
gpt4 = ChatOpenAI(model_name="gpt-4o")
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
