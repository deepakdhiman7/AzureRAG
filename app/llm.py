from langchain_openai.chat_models.azure import AzureChatOpenAI
from app.config import *

def get_llm():
    return AzureChatOpenAI(
        azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION,
        temperature=AZURE_OPENAI_CHAT_TEMP,
        max_completion_tokens=AZURE_OPENAI_CHAT_MAX_TOKENS
    )
