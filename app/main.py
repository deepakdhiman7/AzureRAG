from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.rag_chain import qa_chain
from app.embeddings import *
from app.azureblob_client import upload_file_to_blob, delete_file_from_blob, list_files

app = FastAPI()
# qa_chain = get_rag_chain()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "Azure RAG API running"}

@app.post("/ask")
def ask_question(req: QueryRequest):
    result = qa_chain(req.question)

    return {
        "question": req.question,
        "answer": result,
    }

@app.get("/documents")
def get_documents():
    """
    List all documents in Blob Storage.
    """
    return {
        "documents": list_files()
    }


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document to Azure Blob Storage.
    Triggers Azure AI Search indexer automatically.
    """
    try:
        file_bytes = await file.read()
        result = upload_file_to_blob(file.filename, file_bytes)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/documents/{file_name}")
def delete_document(file_name: str):
    """
    Delete a document from Azure Blob Storage.
    Azure AI Search will automatically remove all related chunks.
    """
    try:
        result = delete_file_from_blob(file_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))