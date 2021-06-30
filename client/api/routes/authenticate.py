from fastapi import APIRouter, Depends, HTTPException

# from client.api.schema.data_collection import Data
from client.api.controller.authentication import generate_token
from client.crud.user import get_user

auth = APIRouter()


@auth.post("/generate_token")
def get_token(username: str, password: str):
    user_data = get_user({"username": username})
    if len(user_data) == 0:
        raise HTTPException(status_code=400, detail=f"{username} doesnot exist.")
    _, _, _, user_password, _, _ = user_data[0]
    print(user_password)
    if user_password != password:
        raise HTTPException(
            status_code=403, detail=f"usename and password doesnot match"
        )
    return generate_token(username=username, password=password)
