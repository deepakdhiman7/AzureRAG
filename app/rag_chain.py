from langchain_community.retrievers.azure_ai_search import AzureAISearchRetriever
from app.llm import get_llm
from app.config import *
from app.search_client import retriever

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

def qa_chain(question):
    llm = get_llm()    

    prompt = ChatPromptTemplate.from_template(
        """Answer the question based only on the context provided.

    Context: {context}

    Question: {question}"""
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    response = chain.invoke(question)
    print(f"answer:\n{response}")

    return response
