from app.embeddings import *
# from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_community.retrievers.azure_ai_search import AzureAISearchRetriever
from app.config import *


# embeddings = get_embeddings()

# vector_store = AzureSearch(
#     embedding_function=embeddings.embed_query,
#     azure_search_endpoint=AZURE_SEARCH_ENDPOINT,
#     azure_search_key=AZURE_SEARCH_KEY,
#     index_name=AZURE_SEARCH_INDEX,
# )

retriever = AzureAISearchRetriever(
        api_key=AZURE_SEARCH_KEY,
        content_key="chunk", 
        top_k=5, 
        service_name=os.getenv("AZURE_AI_SEARCH_SERVICE_NAME"),
        index_name=AZURE_SEARCH_INDEX
        )
