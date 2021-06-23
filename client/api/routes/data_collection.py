from fastapi import APIRouter, Depends, HTTPException
from client.api.schema.data_collection import Data

data_import_router = APIRouter()


@data_import_router.post("/data_import")
def data_import(Data):
    """
    Retrieve items.
    """
    return "items"
