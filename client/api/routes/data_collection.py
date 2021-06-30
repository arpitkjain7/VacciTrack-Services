from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from client.api.schema.data_collection import Data
import os
from datetime import datetime
from typing import List
import uuid
from client.api.controller.authentication import validate_token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

data_import_router = APIRouter()


@data_import_router.post("/data_import")
async def data_import(
    cowin_data: List[UploadFile] = File(...),
    token: str = Depends(oauth2_scheme),
):
    if len(validate_token(token=token)) == 0:
        raise HTTPException(status_code=403, detail=f"Not authorized.")
    id = str(uuid.uuid1().int)
    UUID = str(int(datetime.now().timestamp() * 1000))
    batch_id = f"{UUID}{id[-4:]}"
    file_path = f"data/cowin_data/{batch_id}"
    os.makedirs(file_path, exist_ok=True)
    print(id, UUID)
    print(batch_id)
    for _, file in enumerate(cowin_data):
        file_type = file.filename.split(".")[-1]
        if file_type != "json":
            raise HTTPException(
                status_code=400,
                detail=f"{file_type} is not allowed. Please try uplaoding json file",
            )
        file_name = file.filename
        contents = await file.read()
        with open(f"{file_path}/{file_name}", "wb") as f:
            f.write(contents)
            f.close()
    return {"upload_id": batch_id}
