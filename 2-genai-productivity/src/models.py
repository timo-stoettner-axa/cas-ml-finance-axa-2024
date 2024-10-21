from langchain_openai import ChatOpenAI, OpenAIEmbeddings

gpt4o_mini = ChatOpenAI(model_name="gpt-4o-mini")
gpt4 = ChatOpenAI(model_name="gpt-4o")
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
