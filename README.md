# AzureRAG
RAG application using Azure Blob Storage, Azure AI Search, Azure AI Foundry. Hosted on Azure WebApp

## Project Structure

azure-rag-app/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── config.py              # All environment configs
│   ├── rag_chain.py           # LangChain RAG pipeline
│   ├── search_client.py       # Azure AI Search integration
│   ├── embeddings.py          # Azure OpenAI embeddings
│   └── llm.py                 # Azure OpenAI chat model
│
├── scripts/
│   └── test_query.py          # CLI test script
│
├── .env                       # Secrets (ignored in git)
├── requirements.txt
└── README.md