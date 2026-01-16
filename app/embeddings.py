from langchain_openai.embeddings.azure import AzureOpenAIEmbeddings
from app.config import *

def get_embeddings():
    return AzureOpenAIEmbeddings(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        azure_deployment=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_EMBEDDING_ENDPOINT,
    )

# print("embedding_details:", get_embeddings())

def text_to_embed(query:str):
    embed_client = get_embeddings()
    query_embed = embed_client.embed_query(query)
    return query_embed
