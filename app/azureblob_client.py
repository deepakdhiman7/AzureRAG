from azure.storage.blob import BlobServiceClient
from app.config import *

blob_service_client = BlobServiceClient.from_connection_string(
    AZURE_BLOB_CONNECTION_STRING
)
container_client = blob_service_client.get_container_client(AZURE_BLOB_CONTAINER)


def upload_file_to_blob(file_name: str, file_bytes: bytes):
    """
    Uploads or overwrites a file in Azure Blob Storage.
    """
    blob_client = container_client.get_blob_client(file_name)
    blob_client.upload_blob(file_bytes, overwrite=True)
    return {
        "status": "uploaded",
        "file": file_name
    }


def delete_file_from_blob(file_name: str):
    """
    Deletes a file from Azure Blob Storage.
    """
    blob_client = container_client.get_blob_client(file_name)
    blob_client.delete_blob()
    return {
        "status": "deleted",
        "file": file_name
    }


def list_files():
    """
    Lists all files in the blob container.
    """
    return [blob.name for blob in container_client.list_blobs()]
