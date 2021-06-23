from fastapi import APIRouter, Depends, HTTPException

# from client.api.schema.data_collection import Data
from client.api.controller.register_user import register_user

register_user_router = APIRouter()


@register_user_router.post("/create_user")
def register_user_endpoint(username: str, name: str, app_id: int, email_id: str):
    return register_user(
        {"username": username, "name": name, "app_id": app_id, "email_id": email_id}
    )
